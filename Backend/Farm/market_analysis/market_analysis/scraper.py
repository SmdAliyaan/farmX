import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import pandas as pd
from prophet import Prophet
from .models import CropPrice

BASE_URL = "https://agmarknet.gov.in"

def scrape_crop_price(crop_name):
    # Fetch the crop prices from Agmarknet
    search_url = f"{BASE_URL}/SearchCmmMkt.aspx?cname={crop_name}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'tablePrice'})
    rows = table.find_all('tr')[1:]  # Skip header row
    
    historical_data = []

    for row in rows:
        columns = row.find_all('td')
        market = columns[1].text.strip()
        price = float(columns[3].text.strip())
        date_str = columns[0].text.strip()
        price_date = pd.to_datetime(date_str, format='%d-%b-%Y').date()
        
        # Store historical prices
        historical_data.append({
            'date': price_date,
            'price': price
        })

        # Save the current crop price to the database
        CropPrice.objects.update_or_create(
            crop_name=crop_name,
            market=market,
            date=price_date,
            defaults={'price': price}
        )
    
    # Predict prices for the next week using Prophet
    predict_prices_for_next_week(historical_data, crop_name)

def predict_prices_for_next_week(historical_data, crop_name):
    # Prepare the data for Prophet
    df = pd.DataFrame(historical_data)
    df.rename(columns={'date': 'ds', 'price': 'y'}, inplace=True)

    # Create and fit the Prophet model
    model = Prophet()
    model.fit(df)

    # Make future predictions (7 days)
    future = model.make_future_dataframe(df, periods=7)
    forecast = model.predict(future)

    # Extract the predicted prices for the next week
    predicted_prices = forecast[['ds', 'yhat']].tail(7)  # Last 7 days
    
    # Print or log the predicted prices
    print(f"Predicted prices for {crop_name} for the next week:")
    for i, row in predicted_prices.iterrows():
        print(f"Date: {row['ds'].date()}, Predicted Price: ₹{row['yhat']:.2f}")

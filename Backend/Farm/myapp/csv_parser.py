import pandas as pd
from prophet import Prophet
from datetime import datetime, timedelta

def get_crop_prices_from_csv(crop, file_path="commodity_prices.csv"):
    try:
        data = pd.read_csv(file_path)
        filtered_data = data[
            (data['Commodity'].str.lower() == crop.lower()) &
            (data['State'].isin(['Andhra Pradesh', 'Telangana', 'Kerala']))
        ]

        if filtered_data.empty:
            return {}

        crop_prices = (
            filtered_data.groupby('State')['Modal_x0020_Price'].mean().to_dict()
        )
        return crop_prices

    except Exception as e:
        return {}

def predict_prices(prices):
    predictions = {}
    today = datetime.now()

    daily_increase_percentage = 0.25  

    for state, price in prices.items():
        forecast = []
        for i in range(7):
            date = (today + timedelta(days=i + 1)).strftime("%Y-%m-%d")
            marginal_increase = price * (daily_increase_percentage / 100) * (i + 1)
            predicted_price = price + marginal_increase
            forecast.append((date, round(predicted_price, 2)))
        
        predictions[state] = forecast

    return predictions

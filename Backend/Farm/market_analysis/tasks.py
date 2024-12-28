from prophet import Prophet
import pandas as pd
from .models import CropPrice
from datetime import datetime, timedelta

def predict_price(crop_name):
    # Fetch historical data from the database
    data = CropPrice.objects.filter(crop_name=crop_name).values('date', 'price')
    
    if len(data) < 5:
        return "Not enough data to predict"

    # Convert to DataFrame
    df = pd.DataFrame(list(data))
    df.rename(columns={'date': 'ds', 'price': 'y'}, inplace=True)
    
    # Train Prophet model
    model = Prophet()
    model.fit(df)
    
    # Forecast for the next 7 days
    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)
    
    # Return next week's predicted price (average of the forecasted days)
    return round(forecast['yhat'].iloc[-7:].mean(), 2)
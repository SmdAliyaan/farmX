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
    for state, price in prices.items():
        data = pd.DataFrame({
            "ds": pd.date_range(start=today - timedelta(days=10), periods=10),
            "y": [price] * 10
        })

        model = Prophet()
        model.fit(data)
        future = model.make_future_dataframe(periods=7)
        forecast = model.predict(future)

        predictions[state] = list(zip(forecast["ds"].tail(7).dt.strftime("%Y-%m-%d"), forecast["yhat"].tail(7)))

    return predictions

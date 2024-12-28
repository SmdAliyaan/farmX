import pandas as pd
from prophet import Prophet

def get_crop_prices_from_csv(crop, file_path="commodity_prices.csv"):
    try:
        # Load the CSV file
        data = pd.read_csv(file_path)

        # Filter data for the specified crop and relevant states
        filtered_data = data[
            (data['Commodity'].str.lower() == crop.lower()) &
            (data['State'].isin(['Andhra Pradesh', 'Telangana', 'Kerala']))
        ]

        if filtered_data.empty:
            print(f"No data found for crop: {crop}")
            return {}

        # Group by state and calculate the average modal price
        crop_prices = (
            filtered_data.groupby('State')['Modal_x0020_Price'].mean().to_dict()
        )
        return crop_prices

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return {}

def predict_prices(prices):
    predictions = {}
    for state, price in prices.items():
        # Create a dataframe for Prophet
        data = pd.DataFrame({
            "ds": pd.date_range(start="2024-01-01", periods=10),
            "y": [price] * 10
        })

        model = Prophet()
        model.fit(data)
        future = model.make_future_dataframe(periods=7)
        forecast = model.predict(future)

        predictions[state] = list(zip(forecast["ds"].tail(7).dt.strftime("%Y-%m-%d"), forecast["yhat"].tail(7)))

    return predictions

# Example usage
if __name__ == "__main__":
    crop_name = "Tomato"  # Example crop
    prices = get_crop_prices_from_csv(crop_name)
    if prices:
        print("Current Crop Prices:")
        for state, price in prices.items():
            print(f"{state}: {price} per quintal")

        print("\nPredicted Prices for the Next 7 Days:")
        predictions = predict_prices(prices)
        for state, forecast in predictions.items():
            print(f"\n{state}:")
            for date, pred_price in forecast:
                print(f"{date}: {pred_price:.2f} per quintal")
    else:
        print(f"No data found for crop: {crop_name}")

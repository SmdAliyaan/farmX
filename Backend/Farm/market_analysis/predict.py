from prophet import Prophet
import pandas as pd
from .models import CropPrice

def predict_prices(crop_name):
    data = CropPrice.objects.filter(crop_name=crop_name).values('date', 'price')
    if not data:
        return pd.DataFrame()  
    
    df = pd.DataFrame(data)
    df.columns = ['ds', 'y']

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)
    
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
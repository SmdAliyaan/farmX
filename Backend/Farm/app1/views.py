from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta
import pandas as pd
from prophet import Prophet
from .models import CropPrice, PricePrediction

def index(request):
    return render(request, 'crop_predictor/index.html')

def get_crop_prices(request, crop):
    print("Received crop:", crop)  # Add this line to check the received data
    prices = CropPrice.objects.filter(
        commodity__iexact=crop,
        state__in=['AP', 'TG', 'KL'],
        date=datetime.now().date()
    ).values('state', 'modal_price')
    
    if not prices:
        return JsonResponse({"error": f"No data found for crop: {crop}"})
    
    return JsonResponse({
        price['state']: float(price['modal_price']) 
        for price in prices
    })

def predict_prices(request, crop):
    today = datetime.now().date()
    predictions = {}
    
    for state in ['AP', 'TG', 'KL']:
        try:
            current_price = CropPrice.objects.get(
                commodity__iexact=crop,
                state=state,
                date=today
            ).modal_price
            
            data = pd.DataFrame({
                "ds": pd.date_range(start=today - timedelta(days=10), periods=10),
                "y": [float(current_price)] * 10
            })
            
            model = Prophet()
            model.fit(data)
            future = model.make_future_dataframe(periods=7)
            forecast = model.predict(future)
            
            prediction_data = []
            for date, price in zip(
                forecast["ds"].tail(7).dt.date,
                forecast["yhat"].tail(7)
            ):
                PricePrediction.objects.update_or_create(
                    crop_price=CropPrice.objects.get(
                        commodity__iexact=crop,
                        state=state,
                        date=today
                    ),
                    predicted_date=date,
                    defaults={'predicted_price': price}
                )
                prediction_data.append({
                    'date': date.strftime("%Y-%m-%d"),
                    'price': round(price, 2)
                })
            
            predictions[state] = prediction_data
            
        except CropPrice.DoesNotExist:
            predictions[state] = []
    
    return JsonResponse(predictions)

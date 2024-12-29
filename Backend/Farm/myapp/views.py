from django.shortcuts import render
from .csv_parser import get_crop_prices_from_csv, predict_prices

def crop_analysis(request):
    context = {}
    if request.method == "POST":
        crop_name = request.POST.get("crop_name")
        prices = get_crop_prices_from_csv(crop_name)

        if prices:
            predictions = predict_prices(prices)
            current_prices = {}
            for state in prices:
                if isinstance(prices[state], list):
                    current_prices[state] = prices[state][-1]
                else:
                    current_prices[state] = prices[state]
            
            context = {
                "crop_name": crop_name,
                "current_prices": current_prices,
                "predictions": predictions
            }
        else:
            context = {"error": f"No data found for crop: {crop_name}"}

    return render(request, "crop_analysis.html", context)

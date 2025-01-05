from django.shortcuts import render
import google.generativeai as genai
import re

r = dict()

# Parser to ensure LLM output consistency
def parse_response(response):
    # Standardize formatting by removing unwanted characters and normalizing structure
    response = response.replace('*', '').strip()
    lines = response.split('\n')
    parsed_data = {}
    
    for line in lines:
        # Ensure line follows format: "Resource: Quantity Unit"
        match = re.match(r"^(\w+):\s+(\d+\s+\w+)", line)
        if match:
            resource, quantity = match.groups()
            parsed_data[resource] = quantity
    return parsed_data


def chat_with_ai(request):
    global r
    if request.method == 'POST':
        cropType = request.POST.get('cropType')
        landArea = request.POST.get('landArea')
        season = request.POST.get('season')
        soilquality = request.POST.get('soilquality')

        response = get_ai_response(cropType, landArea, season, soilquality)
        parsed_response = parse_response(response)
        r = parsed_response
        
        return render(request, 'resources/ai.html', {
            'cropType': cropType,
            'landArea': landArea,
            'season': season,
            'response': response,
            'resources': parsed_response  # Pass parsed resources to the template
        })
    
    return render(request, 'resources/ai.html', {})


def get_ai_response(cropType, landArea, season, soilquality):
    genai.configure(api_key="AIzaSyBbJRmC40mbGcc_7vi7cJLU9vDHG_0RDI4")  # API Key
    
    generation_config = {
        "temperature": 0.1,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    
    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.0-pro",
        generation_config=generation_config,
        safety_settings=safety_settings
    )

    convo = model.start_chat(history=[])
    context = (
       "You are an experienced agricultural assistant helping a farmer plan their crop cultivation. The farmer will provide details about the crop type they want to plant, the land area in square meters, the soil quality, and the season (summer, spring, autumn, or winter). Based on this information, you will provide a detailed list of resources required, including the quantity of seeds (in kilograms) needed to cover the specified area. Additionally, outline the necessary fertilizers, water requirements, and any essential tools or equipment. Ensure the response is specific to the crop type, season, and soil conditions to maximize yield and efficiency. Include all tools the farmer will need throughout the planting and growing process."
    )

    message = (
        f"{context} Croptype: {cropType}, LandArea: {landArea}, "
        f"Soil Quality: {soilquality}, Season: {season}."
    )

    response = convo.send_message(message)
    answer = convo.last.text

    return answer.strip()  # Return clean response


def order_view(request):
    global r
    return render(request, 'resources/order.html', {"resources": r})

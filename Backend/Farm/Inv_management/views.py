from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from .forms import ProductForm
from django.contrib import messages
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inventory_report')  # Redirect to inventory report after adding product
    else:
        form = ProductForm()
    
    categories = Category.objects.all()
    return render(request, 'add_inv.html', {'form': form, 'categories': categories})

def inventory_report(request):
    products = Product.objects.all()
    return render(request, 'inv.html', {'products': products})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect('inventory_report')
    return render(request, 'confirm_delete.html', {'product': product})
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Retrieve the product by its primary key
    categories = Category.objects.all()  # Fetch all categories to pass to the template
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)  # Pass the existing product to the form
        if form.is_valid():
            form.save()  # Save the updated product
            return redirect('inventory_report')  # Redirect back to the inventory page after saving
    else:
        form = ProductForm(instance=product)  # Pre-fill the form with the existing product data

    # Pass form, product, and categories to the template
    return render(request, 'add_inv.html', {'form': form, 'product': product, 'categories': categories})






import requests
from django.shortcuts import render

def weather_forecast(request):
    # Initialize empty dictionary for weather data and forecast data
    weather_data = {}
    forecast_data = {}
    city = None  # Initialize city to None
    next_day_forecast = []
    next_week_forecast = []

    # Sample Data for Additional Information for Farmers
    additional_info = {
        "soil_moisture_levels": "Monitoring soil moisture is crucial for optimal crop growth...",
        "crop_planning": "Depending on the rainfall prediction, farmers might opt to plant crops...",
        "pest_management": "Rainfall and humidity can influence pest populations...",
        "water_management": "Efficient water management strategies become essential..."
    }

    if request.method == 'POST':
        city = request.POST.get('city')
    elif request.method == 'GET' and 'city' not in request.GET:
        # Default city if none is provided
        city = 'Hyderabad'  # You can change this to any default city

    if city:
        api_key = '1a5f6c9013c1cf931b5512d06bbdd474'
        
        # Current weather API
        current_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        # 5-day forecast API
        forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

        try:
            # Get current weather data
            current_response = requests.get(current_url)
            current_response.raise_for_status()  # Check if the request was successful
            current_data = current_response.json()
            
            weather_data = {
                'city': city,
                'temperature': current_data['main']['temp'],
                'description': current_data['weather'][0]['description'],
                'icon': current_data['weather'][0]['icon'],
            }

            # Get forecast data (next 5 days)
            forecast_response = requests.get(forecast_url)
            forecast_response.raise_for_status()
            forecast_data = forecast_response.json()
            
            # Extract forecast data for the next 24 hours (next day) and next week
            for forecast in forecast_data['list']:
                forecast_time = forecast['dt_txt']
                
                # For next day (midday)
                if "12:00:00" in forecast_time:  
                    next_day_forecast.append({
                        "date": forecast_time.split()[0],
                        "temperature": forecast['main']['temp'],
                        "description": forecast['weather'][0]['description'],
                        "rain": forecast.get('rain', {}).get('3h', 0),
                    })
                
                # For next week (night time, every 3 hours)
                if "00:00:00" in forecast_time:  
                    next_week_forecast.append({
                        "date": forecast_time.split()[0],
                        "temperature": forecast['main']['temp'],
                        "description": forecast['weather'][0]['description'],
                        "rain": forecast.get('rain', {}).get('3h', 0),
                    })
            
        except requests.RequestException:
            weather_data = {'error': 'Error fetching weather data'}

    # Passing actual data to the template
    context = {
        "city": city,
        "weather_data": weather_data,
        "next_day_forecast": next_day_forecast,
        "next_week_forecast": next_week_forecast,
        "additional_info": additional_info,
    }
    
    return render(request, 'weather_forecast.html', context)



from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from .models import Product

def generate_pdf(request):
    # Get all products from the database
    products = Product.objects.all()

    # Create a response object with PDF mime type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="products_report.pdf"'

    # Create a PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Product details as a list of lists
    product_data = [
        ["Product Name", "Price", "Quantity Total", "Date Bought", "Date Expiration", "Category", "Quantity Remaining"]
    ]

    for product in products:
        product_data.append([
            product.name,
            f"${product.price}",
            str(product.quantity_total),
            str(product.date_bought),
            str(product.date_expiration),
            product.category.name,
            str(product.quantity_remaining),
        ])

    # Create a table and add styles
    table = Table(product_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Add the table to the document
    elements.append(table)
    doc.build(elements)

    return response

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import urllib.parse

load_dotenv()
genai.configure(api_key=(os.getenv("GOOGLE_API_KEY")))


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    print(text)
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    index_path = os.path.join(settings.BASE_DIR, "faiss_index")
    vector_store.save_local(index_path)
    return index_path

def get_conversational_chain():
    prompt_template = """
    You are analyzing the data in the inventory given and answering all user questions. The context contains a table with the following
    product names, image, price, quantity_total, date_bought,date_expiration,category,quantity_remaining, Answer on the basis of this.

{context} (Provide the PDF containing the data for analysis)

Question:
{question}

Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local(
        os.path.join(settings.BASE_DIR, "faiss_index"),
        embeddings,
        allow_dangerous_deserialization=True  # Explicitly allow deserialization
    )
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    response_text = response["output_text"]
    if response_text == "":
        response_text = "It seems that the answer is out of context. Here is a general response: ..."
    return response_text

def gemini(request):
    if request.method == 'POST':
        # Handle PDF upload
        pdf_docs = request.FILES.getlist('pdf_files')
        raw_text = get_pdf_text(pdf_docs)
        text_chunks = get_text_chunks(raw_text)
        pdf_path = get_vector_store(text_chunks)  # Save the PDF path

        # Store the PDF path in the user's session
        request.session['pdf_path'] = pdf_path

        # Handle user question
        user_question = request.POST.get('user_question')
        response_text = user_input(user_question)


        # Return response
        return render(request, 'gemini.html', {'response_text': response_text})
    else:
        return render(request, 'gemini.html')

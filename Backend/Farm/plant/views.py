import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import logging
logging.getLogger('absl').setLevel(logging.ERROR)
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.conf import settings
from .recommendations import recommendations
import tensorflow as tf
import numpy as np
from PIL import Image
from django.core.files.storage import FileSystemStorage

# Suppress TensorFlow warnings
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Update model path
model_path = os.path.join(settings.BASE_DIR, 'model/model_InceptionV3.h5')
model = tf.keras.models.load_model(model_path)

class_names = {
    0: 'Corn___Common_Rust', 1: 'Corn___Gray_Leaf_Spot',
    2: 'Corn___Healthy', 3: 'Corn___Leaf_Blight', 
    4: 'Potato___Early_Blight', 5: 'Potato___Healthy', 
    6: 'Potato___Late_Blight', 7: 'Rice___Brown_Spot', 
    8: 'Rice___Healthy', 9: 'Rice___Hispa', 10: 'Rice___Leaf_Blast', 
    11: 'Wheat___Brown_Rust', 12: 'Wheat___Healthy', 13: 'Wheat___Yellow_Rust'
}

def home(request):
    if request.method == 'POST' and request.FILES.get('image'):
        # Save uploaded image
        image_file = request.FILES['image']
        file_name = default_storage.save(f'uploads/{image_file.name}', image_file)
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        
        try:
            # Preprocess image
            img = Image.open(file_path)
            img = img.resize((224, 224))  # Adjust size according to your model's input requirements
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0  # Normalize
            
            # Make prediction
            predictions = model.predict(img_array)
            predicted_class_index = np.argmax(predictions[0])
            predicted_class = class_names[predicted_class_index]
            confidence = float(predictions[0][predicted_class_index])
            
            # Get recommendations
            recommendation = recommendations.get(predicted_class, {})
            
            context = {
                'predicted_class': predicted_class.replace('___', ' '),
                'confidence_format': f"{confidence * 100:.2f}%",
                'image_url': f'/media/{file_name}',
                'disease': recommendation.get('disease', ''),
                'text': recommendation.get('text', ''),
                'solution': recommendation.get('solution', ''),
                'prevention': recommendation.get('prevention', ''),
                'medicine_products': recommendation.get('medicine_products', [])
            }
            
            return render(request, 'plant/plant.html', context)
            
        except Exception as e:
            print(f"Error during prediction: {e}")
            context = {'error': 'Error processing image'}
            return render(request, 'plant/ho.html', context)
            
        finally:
            
            if os.path.exists(file_path):
                os.remove(file_path)
    
    return render(request, 'plant/ho.html')

def predict_disease(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
       
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads', 'plant_images')
        os.makedirs(upload_dir, exist_ok=True)
        
        
        fs = FileSystemStorage(location=upload_dir)
        filename = fs.save(image_file.name, image_file)
        
        # Get the URL for the saved file
        uploaded_file_url = settings.MEDIA_URL + 'uploads/plant_images/' + filename
        
        # Your prediction logic here
        
        return render(request, 'plant/plant.html', {
            'image_url': uploaded_file_url,
            'predicted_class': predicted_class,
            # ... other context data ...
        })
    
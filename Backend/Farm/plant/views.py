from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import PlantImage

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        # For now, the analysis result is a placeholder
        analysis_result = "Your image has been uploaded successfully. AI analysis coming soon!"

        # Save image and analysis result
        PlantImage.objects.create(image=image)

        return render(request, 'plant/plant.html', {
            'uploaded_file_url': uploaded_file_url,
            'analysis_result': analysis_result,
        })
    return render(request, 'plant/plant.html')
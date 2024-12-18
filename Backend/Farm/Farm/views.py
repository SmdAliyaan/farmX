from django.shortcuts import render

def home(request):
    return render(request, 'farmX/index.html')  # Specify the app name if necessary


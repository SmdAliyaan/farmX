from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django import forms
from django.shortcuts import redirect, render

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, "about.html")



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {"form": form})


def ind(request):
    return render(request, "ind.html")   

from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

# Create your views here.

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "users/login.html"
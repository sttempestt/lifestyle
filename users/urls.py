from django.urls import path
from .views import CustomLoginView, registration
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("registration/", registration, name="registration"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]

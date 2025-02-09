from django.urls import path
from .views import CustomLoginView, registration

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
	path("registration/", registration, name="registration")
]



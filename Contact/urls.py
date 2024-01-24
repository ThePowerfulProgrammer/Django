from django.urls import path
from .import views

app_name = "Contact"

urlpatterns = [
    path("contact/",views.contactView,name="contact")
]


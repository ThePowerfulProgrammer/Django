from django.urls import path
from .import views

app_name = "Home"

urlpatterns = [
    path("",views.homeView, name="home"),
    path("contact/", views.contactView, name="contact"),
    # path("success/", views.successView, name="success"),
    path("about/", views.aboutView, name="about"),

]

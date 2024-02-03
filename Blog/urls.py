from django.urls import path
from . import views
app_name = "Blog"

urlpatterns = [
    path("",views.PostIndexView.as_view(),name="index"),
    path("<int:pk>/", views.postDetailView, name="detail"),
    path("<str:category>/", views.PostCategoryView.as_view(), name="category"),
]

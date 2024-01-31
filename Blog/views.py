from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *
from django.views import generic


# Create your views here.


class PostIndexView(generic.ListView):
    template_name = "Blog/index.html"
    context_object_name = "latest_post_list"
    
    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.all().order_by("-created_on")

class PostCategoryView(generic.ListView):
    template_name = 'Post/detail.html'
    context_object_name = 'post_category_list'
    
    def get_queryset(self):
        return self.model.objects.filter(categories__name__contains=self.kwargs['category']).order_by('-created_on')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        return context
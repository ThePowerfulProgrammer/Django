from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.shortcuts import get_object_or_404, render
from .forms import CommentForm
from .models import *
from django.shortcuts import render, redirect
from django.views import generic


# Create your views here.


class PostIndexView(generic.ListView):
    template_name = "Blog/index.html"
    context_object_name = "latest_post_list"
    
    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.all().order_by("-created_on")

class PostCategoryView(generic.ListView):
    template_name = 'Blog/category.html'
    context_object_name = 'post_category_list'
    
    def get_queryset(self):
        return Post.objects.all().filter(categories__name__contains=self.kwargs['category']).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        return context
    
def postDetailView(request,pk):
    post = get_object_or_404(Post,id=pk)
    form = CommentForm()
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(author=form.cleaned_data['author'],
                              body=form.cleaned_data['body'],
                              post=post,
                              )
            comment.save()
            return redirect(request.path_info)
            
    
    comments = Comment.objects.filter(post=post)
    
    context = {
        'post':post,
        'comments':comments,
        'form':CommentForm(),
    }
    
    return render(request,"Blog/detail.html", context)

    
    
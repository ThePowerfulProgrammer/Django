# Blog/admin.py

from django.contrib import admin
from .models import Category, Comment, Post

class CategoryAdmin(admin.ModelAdmin):
    
    pass
    

class PostAdmin(admin.ModelAdmin):

    list_display = ['title','created_on']

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
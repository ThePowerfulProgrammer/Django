from django.db import models

# Create your models here.


# Assign categories to our Posts eg: [Science,Robotics]
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    
# Our actual blog posts    
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts") # We do not have a posts field in Category but we can: Category.posts :) 
    
    def __str__(self):
        return self.title
    

# User interaction
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.author} on '{self.post}'"

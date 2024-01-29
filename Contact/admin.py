from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    
    list_display = ["name","email","subject"]
    
    fieldsets = [
        ("Personal Details",{'fields':['name', 'email']}),
        ("Message", {'fields':['subject', 'body']})
    ]

admin.site.register(Contact, ContactAdmin)
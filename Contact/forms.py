from django import forms
from django.forms import ModelForm
from .models import Contact

# Class to create a contact form
class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(required=False)
    subject = forms.CharField(max_length=40)
    body = forms.CharField(widget=forms.Textarea, required=True)
    
# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name','email','subject','body']
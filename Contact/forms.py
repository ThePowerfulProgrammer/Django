from django import forms
from django.forms import ModelForm
from .models import Contact

# Class to create a contact form
class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control", "id": "test", "placeholder":"Enter name: "}))
    email = forms.EmailField(required=False,widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"name@site.com"}))
    subject = forms.CharField( required=True,max_length=40,widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Why are you writing to me?"}))
    body = forms.CharField(required=True,widget=forms.Textarea(attrs={"class":"form-control", "placeholder": "Make it Count!"}))
    
    
    
    
# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name','email','subject','body']
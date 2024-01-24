from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponseRedirect

# Create your views here.

def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            
            new_contact = Contact(name=name,email=email,subject=subject,body=body)
            new_contact.save()
            
            return HttpResponseRedirect("/Home/")
    return render(request,"Contact/contact.html", {"form":form})
                

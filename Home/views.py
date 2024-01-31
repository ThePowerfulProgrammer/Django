from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

# Create your views here.

# Render home.html to end-user
def homeView(request):
    return render(request,template_name="Home/home.html", context={})

# not using this
def aboutView(request):
    data = {
        "name": "Ashish Ramnath",
        "projectsInDevelopment": ["Reading", "Consuming all forms of horror media", "Playing pool", "Working on arduino Projects"]
    }
    return render(request, template_name="Home/about.html",context=data)

#  render ContactForm to end-user
def contactView(request):
    if request.method == "GET":
        form = ContactForm() # Create empty form
    elif request.method == "POST":
        form = ContactForm(request.POST) # Populate form with data from POST
        if form.is_valid():
            from_email = form.cleaned_data["from_email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            
            try:
                send_mail(subject,message,from_email,['admin@example.com'])
            except BadHeaderError:
                return HttpResponse("<h1>Invalid Header found</h1>")
            return redirect("Home:home")        
    return render(request, "Home/email.html", {"form": form})

# Output success message to user            
def successView(request):
    return HttpResponse("Success! Thank you for your message.")
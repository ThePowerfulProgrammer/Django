from django.shortcuts import render
from django.http import HttpResponse
from .models import Service

# Create your views here.

from django.shortcuts import render

def simpleView(request):
    service = Service.objects.get(pk=1)
    print(service.image.url)
    context = {'service': service}
    return render(request, 'Services/index.html', context=context)

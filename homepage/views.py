from django.shortcuts import render # type: ignore
from django.http import HttpResponse# type: ignore
from django.shortcuts import render  # type: ignore

# Create your views here.
  # type: ignore
def home(request):
    return render(request, 'homepage/home.html')
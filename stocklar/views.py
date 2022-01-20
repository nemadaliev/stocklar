from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def home(request):
    return render(request, 'website/home.html')

def companies(request):
    return render(request, 'website/companies.html')
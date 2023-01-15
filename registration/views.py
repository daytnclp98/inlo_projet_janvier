from django.http import HttpResponse
from django.shortcuts import render

def tarifs(request):
    return render(request, 'tarifs.html')


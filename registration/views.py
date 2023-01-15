from django.http import HttpResponse
from django.shortcuts import render

from registration.models import Inscription


def tarifs(request):
    inscription = Inscription.objects.all()
    return render(request, 'tarifs.html', {'inscription' : [inscription]})


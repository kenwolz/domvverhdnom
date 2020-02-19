from django.http import HttpResponse
from django.shortcuts import render, redirect


def indem(request):
    return render(request, 'service.html')


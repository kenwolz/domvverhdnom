from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')

def contacts(request):
    return render(request, 'mainApp/contacts.html')

def privacy(request):
    return render(request, 'mainApp/privacy.html')

def news(request):
    return render(request, 'mainApp/news.html')
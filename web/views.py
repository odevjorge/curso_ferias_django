from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'pages/home.html')


def segunda_pagina(request):
    return render(request, 'pages/segunda_pagina.html')

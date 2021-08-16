from django.shortcuts import render

from pages.models import Team


def home(request):
    teams = Team.objects.all()
    return render(request, 'pages/index.html', {"teams": teams})


def about(request):
    teams = Team.objects.all()
    return render(request, 'pages/about.html', {"teams": teams})


def location(request):
    return render(request, 'pages/location.html')


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')

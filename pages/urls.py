from django.urls import path
from pages.views import home, about, location, services, contact

urlpatterns = [
    path('', home, name="home"),
    path('about', about, name='about'),
    path('location/', location, name='location'),
    path('services', services, name='services'),
    path('contact/', contact, name='contact')
]

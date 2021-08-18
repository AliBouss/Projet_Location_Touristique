from django.urls import path

from location.views import location

urlpatterns = [
    path('', location, name="location")
]

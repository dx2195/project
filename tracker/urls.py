from django.urls import path
  
from . import views

urlpatterns = [
        path('sightings/', views.sightings, name = 'sightings'),
        path('map/', views.map, name = 'map'),
        path('<unique-squirrel-id>/', views.sighting_details),
]

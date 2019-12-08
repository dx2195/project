from django.urls import path
  
from . import views

urlpatterns = [
        path('sightings/', views.sightings, name = 'sightings'),
        path('sightings/add/', views.create, name = 'create'),
        path('map/', views.map, name = 'map'),
        path('sightings/<unique_squirrel_ID>/', views.update, name = 'update'),
]

from django.urls import path
  
from . import views
urlpatterns = [
        path('sightings/', views.sightings),
        path('<unique-squirrel-id>/', views.sighting_details),
]

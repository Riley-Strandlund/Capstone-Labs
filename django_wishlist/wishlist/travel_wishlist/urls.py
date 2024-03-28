from django.urls import path
from .import views 

urlpatterns = [
    path('', views.place_list, name='place_list'), # represent a request to path empty string, place_list function in the views file handles it
    path('visited', views.places_visited, name='places_visited'),
    path('place/<int:place_pk>/was_visited', views.place_was_visited, name='place_was_visited'), 
    # path('url link path', function, name). The function is the functionality you want and the name is the placeholder used throughout the code so changed urls don't break the code.
    path('about', views.about, name='about')
]
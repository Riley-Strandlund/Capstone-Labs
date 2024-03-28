from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm

# Create your views here.

def place_list(request):

    if request.method == 'POST':
        # create new place
        form = NewPlaceForm(request.POST) # creating a form from data in the request
        place = form.save() # creates a model object from form
        if form.is_valid(): # validates against DB constraints
            place.save() # saves place to db
            return redirect('place_list') # reloads home page

    #places = Place.objects.all() # queries database. Helps fetch 'all' objects
    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form}) # the render requires a template or a dictionary of data. the new forms is for entering new places

def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited':visited})

def place_was_visited(request, place_pk):
    if request.method == 'POST': # only respond to post methods
        #place = Place.objects.get(pk=place_pk) # get database object by primary key. pk is column. place_pk is variable
        place = get_object_or_404(Place, pk=place_pk) # gets and returns object or returns an error
        place.visited = True
        place.save()
    return redirect('place_list') # brings you to the quoted webpage. if the webpage doesn't change then it's an automatic reload.

def about(request):
    author = 'Riley'
    about = 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about':about})

from django.db import models
from django.views.generic import ListView
from .models import Movies

# Create your views here.

class MoviesListView(ListView):
    model = Movies
    template_name = 'movies/movies_list.html'
    context_object_name = 'movies_list'

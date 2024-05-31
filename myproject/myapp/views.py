from django.shortcuts import render
from myapp.models import Movie, Director, Log
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'movie_list'
    queryset = Movie.object.all()

class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'myapp/detail.html'



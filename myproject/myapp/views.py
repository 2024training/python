from django.views import generic
from myapp.models import Movie, Director, Log 
from django.shortcuts import render
from django.urls import reverse



class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'movie_list'
    queryset = Movie.objects.all()

class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'myapp/detail.html'
    context_object_name = 'movie'


class RegisterDirectorView(generic.CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'myapp/register.html'
    def get_success_url(self):
        return reverse('myapp:registermovie') 


class RegisterMovieView(generic.CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'myapp/register.html'
    def get_success_url(self):
        return reverse('myapp:movie_detail', kwargs={'pk': self.object.pk }) 

class WritingLogView(generic.CreateView):
    model = Log
    form_class = LogForm
    template_name = 'myapp/register.html'
    def get_success_url(self):
        return reverse('myapp:movie_detail', kwargs={'pk': self.object.movie.pk }) 

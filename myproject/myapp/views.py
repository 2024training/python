from django.views import generic
from myapp.models import Movie, Director, Log 
from django.shortcuts import render
from django.urls import reverse
from myapp.forms import DirectorForm, MovieForm, LogForm
from django.shortcuts import get_object_or_404, redirect



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


class UpdateLogView(generic.UpdateView):
    model = Log
    form_class = LogForm
    template_name = "myapp/register.html"
    def get_success_url(self):
        return reverse('myapp:movie_detail', kwargs={'pk': self.object.movie.pk })

class DeleteLogView(generic.DeleteView):
    model = Log
    template_name = 'myapp/delete.html'
    def get_success_url(self):
        return reverse('myapp:movie_detail', kwargs={'pk': self.object.movie.pk})

class DeleteMovieView(generic.DeleteView):
    model = Movie
    def get_success_url(self):
        return reverse('myapp:index')
    

def writingthismovielog(request, movie_id):
    obj = get_object_or_404(Movie, id=movie_id)
    form = LogForm({'movie':obj})
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            l = form.save(commit=False)
            l.save()
            return redirect('myapp:movie_detail', pk=l.movie.pk)
    else:
        return render(request, 'myapp/register.html', {'form': form})
      

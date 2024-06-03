from django.urls import path, include
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('register/director', views.RegisterDirectorView.as_view(), name = 'registerdirector'),
    path('register/movie/', views.RegisterMovieView.as_view(), name= 'registermovie'),
    path('writing/log/', views.WritingLogView.as_view(), name = 'writinglog'),
]

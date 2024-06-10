from . import views
from django.urls import path
from todo.views import TodoCreate

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    path('logout/', views.logout_confirm, name='logout_confirm'),
    path('user/', views.user_view, name='user'),
    path('other/', views.other_view, name='other'),
    path('create/', TodoCreate.as_view(), name='todo_create'),
]
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from .views import top
urlpatterns = [
    path('login/',
        LoginView.as_view(
            # redirect_authenticated_user=True,
            template_name='app/login.html'
        ),
        name='login'),
    path('', top, name='top')
]
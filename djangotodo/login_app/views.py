from django.shortcuts import render
from .forms import SignupForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = SignupForm()
        
    param = {
        'form':form
    }
    return render(request, 'login_app/signup.html', param)

def login_view(request):
    pass

def logout_view(request):
    pass

def user_view(request):
    pass

def other_view(request):
    pass

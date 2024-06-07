from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout

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
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            
            if user:
                login(request, user)
                return redirect('http://localhost:8000/todo/todo/')
                # ログイン成功後のリダイレクト処理などを追加することが適切です。
                

    else:
        form = LoginForm()

    param = {
        'form': form,
    }

    return render(request, 'login_app/login.html', param)

def logout_view(request):
    logout(request)
    
    return render(request, 'login_app/logout.html')

def user_view(request):
    pass

def other_view(request):
    pass

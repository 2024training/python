from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # アカウント登録後に自動的にログインする
            return redirect(reverse_lazy('login'))  # ログインページにリダイレクトする
    else:
        form = SignupForm()
        
    param = {
        'form': form
    }
    return render(request, 'login_app/signup.html', param)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            
            if user:
                login(request, user)
                next_page = request.GET.get('next', reverse_lazy('list'))  # 'next' パラメータからリダイレクト先を取得
                return redirect(next_page)  # リダイレクト先を指定してリダイレクト
                
    else:
        form = LoginForm()

    param = {
        'form': form,
    }

    return render(request, 'login_app/login.html', param)

# def logout_view(request):
#     logout(request)
    
#     return render(request, 'login_app/logout.html')

def logout_confirm(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # ログインページにリダイレクト
    return render(request, 'login_app/logout_confirm.html')

def logout_view(request):
    logout(request)
    
    return render(request, 'login_app/logout.html')

def user_view(request):
    pass

def other_view(request):
    pass

from django.views.generic import TemplateView ,ListView ,DetailView ,UpdateView ,DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import DiaryForm
from .models import Diary
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

@login_required
def IndexView(request):
    # ログインしたユーザーに特有のコンテンツを処理します
    return render(request, 'index.html')

def diary_detail(request):
    # ログインしているユーザーのIDを取得
    user_id = request.user.id
    
    # ログインしているユーザーのIDと同じIDを持つ Diary オブジェクトを取得
    diary = Diary.objects.filter(user_id=user_id).first()
    
    # Diary オブジェクトが存在するかどうかを確認
    if diary:
        # Diary オブジェクトが存在する場合は、テンプレートに渡す
        context = {'diary': diary}
        return render(request, 'diary_detail.html', context)
    else:
        # Diary オブジェクトが存在しない場合は、何らかの処理を行うか、エラーページを表示するなどの処理を行う
        return render(request, 'error.html')

class DiaryCreateView(CreateView):
    template_name = 'diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_create_complete')

class DiaryCreateView2(CreateView):
    template_name = 'diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_create_complete')

    def form_valid(self, form):
        # フォームから日記オブジェクトを取得
        diary = form.save(commit=False)
        
        # ログインユーザーのidを取得して、日記のユーザーIDに代入
        diary.user = self.request.user
        
        # 日記を保存
        diary.save()
        
        return super().form_valid(form)

class DiaryCreateCompleteView(TemplateView):
    template_name = 'diary_create_complete.html'

class DiaryListView(ListView):
    template_name = 'diary_list.html'
    model = Diary

class DiaryDetailView(DetailView):
    template_name = 'diary_detail.html'
    model = Diary

class DiaryUpdateView(UpdateView):
    template_name = 'diary_update.html'
    model = Diary
    fields = ('date', 'title', 'text',)
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.updated_at = timezone.now()
        diary.save()
        return super().form_valid(form)

class DiaryDeleteView(DeleteView):
    template_name = 'diary_delete.html'
    model = Diary
    success_url = reverse_lazy('diary:diary_list')

class HomeView(TemplateView):
    template_name = 'home.html'

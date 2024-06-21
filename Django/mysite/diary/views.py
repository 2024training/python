from django.views.generic import TemplateView ,DetailView ,UpdateView ,DeleteView
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

# psuedopsuedocode
# def ListViewtype1(request):
#     # ログインしているユーザーのIDを取得
#     user_id = request.user.id
    
#     # ログインしているユーザーのIDと同じIDを持つ Diary オブジェクトを取得
#     diary = Diary.objects.filter(user_id=user_id)
#     list = []
    
#     # Diary オブジェクトが存在するかどうかを確認
#     if diary:
#         if method="POST":
#             for item in diary:
#                 if request.form.value in item.text:
#                     list.append(item)
#                 if list:
#                     return render(request, 'diary_list.html', list)
#                 else:
#                     return render(request, 'error.html')
#         if method="GET":
#         # Diary オブジェクトが存在する場合は、テンプレートに渡す
#             context = {'diary': diary }
#             return render(request, 'diary_list.html', context)
#     else:
#         # Diary オブジェクトが存在しない場合は、何らかの処理を行うか、エラーページを表示するなどの処理を行う
#         return render(request, 'error.html')
    
def ListView(request):
    # ログインしているユーザーのIDを取得
    user_id = request.user.id
    
    # ログインしているユーザーのIDと同じIDを持つ Diary オブジェクトを取得
    diary_entries = Diary.objects.filter(user_id=user_id)

    if request.method == "POST":
        # POST メソッドの場合、検索テキストを取得し、該当する日記エントリーをフィルタリングする
        search_text = request.POST.get('search_text', '')
        matched_diary_entries = diary_entries.filter(text__icontains=search_text)
        # フィルタリングされた結果をテンプレートに渡してレンダリング
        if matched_diary_entries:
            return render(request, 'diary_list.html', {'diary': matched_diary_entries, 'search_text': search_text})
        else:
            message = "は存在しませんでした。"
            return render(request, 'diary_list.html', {'message': message,'search_text': search_text })
    else:
        # GET メソッドの場合、すべての日記エントリーを表示
        if diary_entries.exists():
            return render(request, 'diary_list.html', {'diary': diary_entries})
        else:
            # 日記エントリーが存在しない場合、エラーページへ
            return render(request, 'error.html')
        # {{ url('index:index', pk=user.pk) }}はhtml内で動的なURLを生成、対して下記はレンダリング時にURLを生成

class DiaryCreateView(CreateView):
    template_name = 'diary_create.html'
    # フォームの定義（インスタンス化）
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_create_complete')

    # オーバーライド
    # フォームの値が有効かどうかをDiaryFormが判断。有効だったかどうかをviews.pyが判断し、以下の関数が実行される。
    def form_valid(self, form):
        # フォームに関連づけられたモデルと一致するかどうかを判断、フォームから日記モデルのインスタンスを作成。
        diary = form.save(commit=False)
        # ログインユーザーのidを取得して、日記のユーザーIDに代入
        diary.user = self.request.user
        # 再度フォームに関連づけられたモデルと一致するかどうかを判断し、モデルのインスタンスの変更をモデルに保存。データーベースへと反映。
        diary.save()
        # return HttpResponseRedirect
        return super().form_valid(form)

class DiaryCreateCompleteView(TemplateView):
    template_name = 'diary_create_complete.html'

class DiaryDetailView(DetailView):
    template_name = 'diary_detail.html'
    model = Diary

class DiaryUpdateView(UpdateView):
    template_name = 'diary_update.html'
    # これってやってることほぼフォームじゃね？
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
    # reverse_lazyしないとビューのロード時にURLの解決が行われることとなる。やってみたらリダイレクトが拒否された。
    success_url = reverse_lazy('diary:diary_list')

class HomeView(TemplateView):
    template_name = 'home.html'

# 情報伝達の種類は？
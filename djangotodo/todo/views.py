from django.shortcuts import render 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class TodoList(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = "tasks"
    
    def get_queryset(self):
        # ログインユーザーに関連するToDoのみを返す
        return Todo.objects.filter(user=self.request.user)
    
class TodoDetail(DetailView):
        model = Todo
        context_object_name = "task"
        
class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'deadline']
    success_url = reverse_lazy('list')  # 作成後にリダイレクトするURL

    def form_valid(self, form):
        form.instance.user = self.request.user  # ログインユーザーを指定
        return super().form_valid(form)

    def form_invalid(self, form):
        # バリデーションエラーがある場合にフォームを再表示する
        return render(self.request, 'todo/todo_form.html', {'form': form})
    
class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")
    
class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")
    
    
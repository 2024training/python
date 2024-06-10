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
    success_url = reverse_lazy('list')
    template_name = 'todo/todo_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        return context
    
class TodoUpdate(UpdateView):
    model = Todo
    fields = ['title', 'description', 'deadline']
    success_url = reverse_lazy('list')
    template_name = 'todo/todo_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        return context
    
class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")
    
    
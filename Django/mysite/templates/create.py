from django.views.generic import TemplateView 
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import DiaryForm
from .models import Diary

class DiaryCreateView(CreateView):
    template_name = 'diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_create_complete')
    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        return super().form_valid(form)

class DiaryCreateCompleteView(TemplateView):
    template_name = 'diary_create_complete.html'

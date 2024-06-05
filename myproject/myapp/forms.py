from django.forms import ModelForm
from myapp.models import Movie, Director, Log
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = ('name',)

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title','watch_date', 'director')
        widgets = {'watch_date': DateInput(),  # カレンダーウィジェットの指定
    }

class LogForm(ModelForm):
    class Meta:
        model = Log
        fields = ('movie','text')


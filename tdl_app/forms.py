from django import forms
from .models import *

class tdlForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    body = forms.Textarea()

    class Meta:
        model = tdl
        # fields = '__all__'
        fields = ['title', 'body']
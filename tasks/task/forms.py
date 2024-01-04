from django import forms
from .models import *

class TaskCreateForm(forms.ModelForm):
    class Meta:
        fields=['name','description']
        model=Task
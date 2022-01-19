from django import forms
from django import *
from . models import *

class stdform(forms.ModelForm):
    class Meta:
        model = stud
        fields = '__all__'
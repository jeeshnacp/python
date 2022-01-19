from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class proform(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'

class sellerform(forms.ModelForm):
    class Meta:
        model=seller
        fields='__all__'

class buyerform(forms.ModelForm):
    class Meta:
        model=buyer
        fields='__all__'

class customcreation(UserCreationForm):
    class Meta:
        model=User
        fields={'username','first_name','last_name','email','password','password1'}
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError      #schreibt eine 14 stellige Zahl als Nutzernamen vor
import re

def validate_username(value):                           #definiert die Funktion dafür!
    if not re.match(r'^\d{14}$', value):
        raise ValidationError('Der Benutzername muss aus einer 14-stelligen Zahl bestehen!')

class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=14, validators=[validate_username])

    class Meta:
        model = User
        fields = ['username']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=14, validators=[validate_username])
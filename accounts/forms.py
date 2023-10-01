from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EmailInput(forms.EmailInput):
    input_type = 'email'


class DateInput(forms.DateInput):
    input_type = 'date'


class RegisterForm(UserCreationForm):
    date_of_birth = forms.DateField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'date_of_birth']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())


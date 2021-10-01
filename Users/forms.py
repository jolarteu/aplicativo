
# Django
from django import forms
from django.contrib.auth.models import User
from Users.models import Profile

class SignupForm(forms.Form):

    username = forms.CharField(label='',min_length=4, max_length=50,
    widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'required': True
                }))
    password= forms.CharField(label='',max_length=15, widget=forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'form-control',
                'required': True
            }
        ))
    password_confirmation = forms.CharField(label='',max_length=15, widget=forms.PasswordInput(attrs={
                'placeholder': 'password confirmation',
                'class': 'form-control',
                'required': True
            }
        ))

    first_name= forms.CharField(label='',min_length=2, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder':'First name',
                'class': 'form-control',
                'required': True
                }
            ))
    last_name= forms.CharField(label='',min_length=2, max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last name',
                'class': 'form-control',
                'required': True
                }
        ))

    email = forms.CharField(label='',min_length=5, max_length=50, widget=forms.EmailInput(
        attrs={
                    "placeholder": "email",
                    "class": "form-control",
                    'required': True
                }
        ))

class ProfileForm(forms.Form):
    picture = forms.ImageField()
    country = forms.CharField(max_length=20, required=False)

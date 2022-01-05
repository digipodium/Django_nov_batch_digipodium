from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your Username',
                'class':'form-control'
            }
        )
    )
    password =  forms.CharField(
        widget= forms.PasswordInput(
            attrs = {
                'placeholder' : 'Your Password',
                'class' : 'form-control'
            }
        )
    )

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your Username',
                'class':'form-control'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Your Email',
                'class' : 'form-control'
            }
        )
    )

    password1 =  forms.CharField(
        widget= forms.PasswordInput(
            attrs = {
                'placeholder' : 'Your Password',
                'class' : 'form-control'
            }
        )
    )

    password2 =  forms.CharField(
        widget= forms.PasswordInput(
            attrs = {
                'placeholder' : 'Cofirm Password',
                'class' : 'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
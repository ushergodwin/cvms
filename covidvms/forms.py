

from django import forms


class Auth_form(forms.Form):
    email = forms.EmailField(max_length=65)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

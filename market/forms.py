from django import forms
from .models import Transaction

class AuthForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['authorised']
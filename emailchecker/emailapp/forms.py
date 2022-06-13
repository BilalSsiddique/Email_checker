from django import forms
from .models import email

class Emailform(forms.ModelForm):
    class Meta:
        model = email
        fields = "__all__"

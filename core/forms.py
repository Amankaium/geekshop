from django import forms
from django.contrib.auth.models import User
from .models import Feedback


class FeedbackCreateForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"


class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

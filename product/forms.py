from django import forms
from .models import Vegetables as Veg


class VegetableCreateForm(forms.ModelForm):
    class Meta:
        model = Veg
        exclude = ('category',)

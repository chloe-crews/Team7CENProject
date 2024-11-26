from django import forms
from .models import Costume

class CostumeForm(forms.ModelForm):
    class Meta:
        model = Costume
        fields = ['title', 'description', 'price_per_day', 'size', 'category', 'image']

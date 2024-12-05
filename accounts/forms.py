from django import forms
from .models import Costume, Message

class CostumeForm(forms.ModelForm):
    class Meta:
        model = Costume
        fields = ['title', 'description', 'price_per_day', 'size', 'category', 'image']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your message here...'}),
        }

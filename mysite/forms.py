from django import forms
from .models import Request
from .models import Category

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'description', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название заявки'}),# текстовая область
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}), # текстовая область
            'category': forms.Select(attrs={'class': 'form-control'}), #выпадающий список
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}), #для загрузки фото
        }
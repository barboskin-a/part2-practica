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

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name'] #из модели вкл в форму
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название категории'}), #поле ввода
        }
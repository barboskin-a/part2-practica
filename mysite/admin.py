from django.contrib import admin
from .models import Category
from .models import Request

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') # отображение строк id и name
    search_fields = ('name',) #поиск по name

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'category', 'status', 'created_at') # отображение строк id, title, user и тд.
    list_filter = ('status', 'category')  #фильтрация по статусу и категории
    search_fields = ('title', 'description')  #поиск по названию и описанию

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Request
from .forms import RequestForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import Category
from .forms import CategoryForm
from django.shortcuts import get_object_or_404

def home(request):
    completed_requests = Request.objects.filter(status='completed').order_by('-created_at')[:4]
    in_progress_count = Request.objects.filter(status='in_progress').count()
    return render(request, 'home.html', {
        'completed_requests': completed_requests,
        'in_progress_count': in_progress_count
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

#принимает заявки
@login_required
def my_requests(request):
    user_requests = Request.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_requests.html', {'requests': user_requests})

#создание заявок
@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.save()
            return redirect('my_requests')
    else:
        form = RequestForm()
    return render(request, 'create_request.html', {'form': form})

#получает данных о всех категориях
@staff_member_required
def manage_categories(request):
    categories = Category.objects.all()
    return render(request, 'manage_categories.html', {'categories': categories})


#добавление категорий
@staff_member_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():  #проверяет форму на валидность (правильность заполнения)
            form.save()  #сохраняет форму
            return redirect('manage_categories')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

#удаление категорий
@staff_member_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk) #получает объект category, исп. перв-ый ключ pk
    if request.method == 'POST': #проверка подтверждения удаления
        category.delete() #удаление
        return redirect('manage_categories') #возвращает на стр. управ категориями
    return render(request, 'delete_category.html', {'category': category}) #отправляет данный

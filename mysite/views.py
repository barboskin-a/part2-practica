from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Request
from .forms import RequestForm

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

@login_required
def my_requests(request):
    user_requests = Request.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_requests.html', {'requests': user_requests})

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

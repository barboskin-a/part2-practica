from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Request

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

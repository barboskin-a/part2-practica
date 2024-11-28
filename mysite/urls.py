from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('my_requests/', views.my_requests, name='my_requests'),
    path('create_request/', views.create_request, name='create_request'),
    path('profile/', views.profile, name='profile'),
    path('requests/change_status/<int:pk>/', views.change_request_status, name='change_request_status'),
    path('requests/', views.manage_requests, name='manage_requests'),
    path('profile/', views.profile, name='profile'),

]
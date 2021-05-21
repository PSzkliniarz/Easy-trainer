from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='workouts-home'),
    path('about/', views.about, name='workouts-about'),
]
from django.urls import path
from .views import TrainingListView, TrainingDetailtView
from . import views

urlpatterns = [
    path('', TrainingListView.as_view(), name='workouts-home'),
    path('training/<int:pk>/', TrainingDetailtView.as_view(), name='training-detail'),
    path('about/', views.about, name='workouts-about'),
]
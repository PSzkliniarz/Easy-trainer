from django.urls import path
from .views import (
    TrainingListView, 
    TrainingDetailtView,
    TrainingCreateView,
    TrainingUpdateView,
    TrainingDeletetView
)
from . import views

urlpatterns = [
    path('', TrainingListView.as_view(), name='workouts-home'),
    path('training/<int:pk>/', TrainingDetailtView.as_view(), name='training-detail'),
    path('training/new/', TrainingCreateView.as_view(), name='training-create'),
    path('training/<int:pk>/update/', TrainingUpdateView.as_view(), name='training-update'),
    path('training/<int:pk>/delete/', TrainingDeletetView.as_view(), name='training-delete'),
    path('about/', views.about, name='workouts-about'),
]
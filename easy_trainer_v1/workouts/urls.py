from django.urls import path
from .views import (
    TrainingListView, 
    TrainingDetailtView,
    TrainingCreateView,
    TrainingUpdateView,
)
from . import views

urlpatterns = [
    path('', TrainingListView.as_view(), name='workouts-home'),
    path('training/<int:pk>/', TrainingDetailtView.as_view(), name='training-detail'),
    path('training/new/', TrainingCreateView.as_view(), name='training-create'),
    path('training/<int:pk>/update/', TrainingUpdateView.as_view(), name='training-update'),
    path('about/', views.about, name='workouts-about'),
]
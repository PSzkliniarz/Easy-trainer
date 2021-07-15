from django.urls import path
from .views import (
    TrainingListView, 
    UserTrainingListView,
    TrainingDetailtView,
    TrainingCreateView,
    TrainingUpdateView,
    TrainingDeletetView,
    CommentCreateView,
    RatingCreateView,
    ImageCreateView,
    VideoCreateView,
    CommentDeletetView
)
from . import views

urlpatterns = [
    path('', TrainingListView.as_view(), name='workouts-home'),
    path('about/', views.about, name='workouts-about'),

    path('user/<str:username>', UserTrainingListView.as_view(), name='user-trainings'),
    
    path('training/<int:pk>/', TrainingDetailtView.as_view(), name='training-detail'),

    path('training/new/', TrainingCreateView.as_view(), name='training-create'),
    path('training/<int:pk>/update/', TrainingUpdateView.as_view(), name='training-update'),
    path('training/<int:pk>/delete/', TrainingDeletetView.as_view(), name='training-delete'),
    path('training/<int:pk>/comment_delete/<int:comment_pk>/', CommentDeletetView.as_view(), name='comment-delete'),

    path('training/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('training/<int:pk>/rating/', RatingCreateView.as_view(), name='add_rating'),
    path('training/<int:pk>/add_image/', ImageCreateView.as_view(), name='add_image'),
    path('training/<int:pk>/add_video/', VideoCreateView.as_view(), name='add_video'),

]
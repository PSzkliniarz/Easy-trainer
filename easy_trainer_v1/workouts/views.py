from PIL import Image
from django.contrib import messages
from django.db.utils import Error
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls.base import reverse, reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Rating, Training, Comment, Image, Video
from .forms import AddCommentForm, AddImageForm, AddVideoForm, AddRatingForm


def home(request):
    context = {
        'trainings': Training.objects.all()
    }
    return render(request, 'workouts/home.html', context)

class TrainingListView(ListView):
    model = Training
    template_name = 'workouts/home.html'
    context_object_name = 'trainings'
    ordering = ['-date_posted']
    paginate_by = 3


class UserTrainingListView(ListView):
    model = Training
    template_name = 'workouts/user_trainings.html'
    context_object_name = 'trainings'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Training.objects.filter(author=user).order_by('-date_posted')


class TrainingDetailtView(DetailView):
    model = Training


class TrainingCreateView(LoginRequiredMixin, CreateView):
    model = Training
    fields = ['title', 'description', 'content', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TrainingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Training
    fields = ['title', 'description', 'content', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        training = self.get_object()
        if self.request.user == training.author:
            return True
        return False


class TrainingDeletetView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Training
    success_url='/'
    
    def test_func(self):
        training = self.get_object()
        if self.request.user == training.author:
            return True
        return False

class CommentDeletetView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    pk_url_kwarg = 'comment_pk' 
    
    def test_func(self):
        deleter = self.get_object()
        if self.request.user == deleter.training.author:
            return True
        return False

    def get_success_url(self):
        success_url = reverse_lazy('training-detail', kwargs={'pk': self.kwargs['pk']})
        return success_url

class ImageDeletetView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Image
    pk_url_kwarg = 'image_pk' 
    
    def test_func(self):
        deleter = self.get_object()
        if self.request.user == deleter.training.author:
            return True
        return False

    def get_success_url(self):
        success_url = reverse_lazy('training-detail', kwargs={'pk': self.kwargs['pk']})
        return success_url

class VideoDeletetView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    pk_url_kwarg = 'video_pk' 
    
    def test_func(self):
        deleter = self.get_object()
        if self.request.user == deleter.training.author:
            return True
        return False

    def get_success_url(self):
        success_url = reverse_lazy('training-detail', kwargs={'pk': self.kwargs['pk']})
        return success_url


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'workouts/add_comment.html'
    form_class = AddCommentForm
    
    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.training_id = self.kwargs['pk']
        super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('training-detail', kwargs={'pk': self.kwargs['pk']})

class RatingCreateView(LoginRequiredMixin, CreateView):
    model = Rating
    template_name = 'workouts/add_rating.html'
    form_class = AddRatingForm
    
    def form_valid(self, form):
        form.instance.rating_user = self.request.user
        form.instance.rating_training_id = self.kwargs['pk']
        return super().form_valid(form)
  
            
    def get_success_url(self):
        return reverse_lazy('training-detail', kwargs={'pk': self.kwargs['pk']})
    
    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())



class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    template_name = 'workouts/add_image.html'
    form_class = AddImageForm
    
    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.training_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('training-detail', kwargs={'pk': self.kwargs['pk']})

    

class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    template_name = 'workouts/add_video.html'
    form_class = AddVideoForm
    
    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.training_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('training-detail', kwargs={'pk': self.kwargs['pk']})

    


def about(request):
    return render(request, 'workouts/about.html', {'title':'About'})
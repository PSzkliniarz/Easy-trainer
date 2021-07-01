from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls.base import reverse, reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Training, Comment
from .forms import AddCommentForm


# Create your views here.
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
    fields = ['title', 'content', 'category', 'rating']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TrainingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Training
    fields = ['title', 'content', 'category', 'rating']

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


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'workouts/add_comment.html'
    form_class = AddCommentForm
    
    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.training_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('training-detail', kwargs={'pk': self.kwargs['pk']})


def about(request):
    return render(request, 'workouts/about.html', {'title':'About'})
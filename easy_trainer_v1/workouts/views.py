from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls.base import reverse
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView
)
from .models import Training


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

def about(request):
    return render(request, 'workouts/about.html', {'title':'About'})
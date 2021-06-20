from django.shortcuts import render
from django.views.generic import ListView, DetailView
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


def about(request):
    return render(request, 'workouts/about.html', {'title':'About'})
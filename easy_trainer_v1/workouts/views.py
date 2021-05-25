from django.shortcuts import render
from .models import Training


# Create your views here.
def home(request):
    context = {
        'trainings': Training.objects.all()
    }
    return render(request, 'workouts/home.html', context)

def about(request):
    return render(request, 'workouts/about.html', {'title':'About'})
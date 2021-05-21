from django.shortcuts import render

trainings = [
    {
        'author': 'trainer1',
        'title': 'Training 1',
        'content': 'First training content',
        'date_posted': 'August 21, 2018'
    },
    {
        'author': 'trainer2',
        'title': 'Training 2',
        'content': 'Secnod training content',
        'date_posted': 'August 24, 2018'
    },
]

# Create your views here.
def home(request):
    context = {
        'trainings': trainings
    }
    return render(request, 'workouts/home.html', context)

def about(request):
    return render(request, 'workouts/about.html', {'title':'About'})
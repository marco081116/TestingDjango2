from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn Pyhon !!!'},
#     {'id': 2, 'name': 'Design with me !!!'},
#     {'id': 3, 'name': 'Frontend DEV !!!'},
# ]

def home(request):
    rooms = Room.objects.all() # override the 'room' value
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    # room = None

    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id= pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
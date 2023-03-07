from django.shortcuts import render, redirect
from django.db.models import Q  # Q look up allows us to and or while searching
from django.contrib import messages # ném message cho user
from django.contrib.auth.models import User # bộ library của django để đăng nhập user
from django.contrib.auth import authenticate, login, logout # bộ library để login
from .models import Room, Topic
from .forms import RoomForm


# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn Pyhon !!!'},
#     {'id': 2, 'name': 'Design with me !!!'},
#     {'id': 3, 'name': 'Frontend DEV !!!'},
# ]

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        try:
            user = User.objects.get(username= username)
        except:
            messages.error(request, 'User does not exist !')

        user = authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not correct !')

    context = {}

    return render(request, 'base/login_register.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else '' # chứa cái tên topics để ném vào

    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
    ) # override the 'room' value

    topics = Topic.objects.all()
    room_count= rooms.count() 

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    # room = None

    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id= pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST) # testing back-end
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # chuyen ve home
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance= room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('home') # chuyen ve home (nhu o create room)

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id = pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home') # chuyen ve home (nhu o create room)
    return render(request, 'base/delete.html', {'obj': room})
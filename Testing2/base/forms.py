from django.forms import ModelForm
from .models import Room, User
# from django.contrib.auth.models import User # không cần nữa, dổi thành user bên models

from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

# đây là model dành cho update user
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']
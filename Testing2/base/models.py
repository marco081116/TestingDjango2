from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create database

class Topic(models.Model):
    name = models.CharField(max_length= 200)

    def __str__(self):
        return self.name

class Room(models.Model): # Từ Room viết hoa chữ R như trong class code trong python 
    host = models.ForeignKey(User, on_delete= models.SET_NULL, null= True)
    topic = models.ForeignKey(Topic, on_delete= models.SET_NULL, null= True)
    name = models.CharField(max_length= 200)
    description = models.TextField(null= True, blank= True)
    # participants = # đang ở trong trang web
    updated = models.DateTimeField(auto_now= True) # auto now -> takes a snapshot on every time we save item(s)
    created = models.DateTimeField(auto_now_add= True) # created -> takes a stamp when we first create item

    class Meta:
        ordering = ['-updated', '-created'] # bỏ thêm dấu - để lên đầu, ko thì ở chót

    def __str__(self):
        return self.name 

class Message(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE) # 1 user can have many mess(s)
    room = models.ForeignKey(Room, on_delete= models.CASCADE) # 1 to many, khi xoa phong thi toan bo message cua room do deu bi xoa
    body = models.TextField()
    updated = models.DateTimeField(auto_now= True) # auto now -> takes a snapshot on every time we save item(s)
    created = models.DateTimeField(auto_now_add= True) # created -> takes a stamp when we first create item

    def __str__(self):
        return self.body[0:50]
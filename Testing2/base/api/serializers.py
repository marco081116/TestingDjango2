# convert model hay object (từ dữ liệu python) thành dữ liệu json 
from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

        
# fields = '__all__' là sẽ trả về tất cả các object bên dưới đây
# class Room(models.Model):  
#     host = models.ForeignKey(User, on_delete= models.SET_NULL, null= True)
#     topic = models.ForeignKey(Topic, on_delete= models.SET_NULL, null= True)
#     name = models.CharField(max_length= 200)
#     description = models.TextField(null= True, blank= True)
#     participants = models.ManyToManyField(User, related_name= 'participants', blank= True) 
#     updated = models.DateTimeField(auto_now= True) 
#     created = models.DateTimeField(auto_now_add= True) 
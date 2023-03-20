# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer


@api_view(['GET']) # Đây là các HTTP methods (như là get, put, post)
def getRoutes(request): # cái view này sẽ cho chúng ta thấy tất cả các cái routes trong API của chúng ta
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return Response(routes)
    # return JsonResponse(routes, safe = False)
    # safe là để sử dụng được nhiều hơn là python dic trong cái return này 
    # chuyển các routes này về json data

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many = True) # many là số lượng cần serializer, mà đây là 1 room nên chúng ta cần many = True
    return Response(serializer.data)
    # Ở đây sẽ có vấn đề là Response sẽ không trả về được là do 'rooms' là 1 kiểu dữ liệu python mà Response thì trả về kiểu 'JSON'
    # Lúc này ta sẽ cần đến 'serializers.py'

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id = pk)
    serializer = RoomSerializer(room, many = False) # many là số lượng cần serializer, mà đây là 1 room nên chúng ta cần many = True
    return Response(serializer.data)
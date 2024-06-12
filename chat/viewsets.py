from rest_framework import viewsets
from chat.models import ChatRoom
from chat.serializers import ChartRoomSerializer
class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChartRoomSerializer
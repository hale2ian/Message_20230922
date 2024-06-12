from rest_framework import serializers
from chat.models import ChatRoom


class ChartRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'name']

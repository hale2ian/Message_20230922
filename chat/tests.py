# tests/test_views.py
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from .models import ChatRoom
from .serializers import ChartRoomSerializer

class ChatRoomViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.chat_room = ChatRoom.objects.create(name='Test Room')
        self.url = reverse('chatroom-list')  # Adjust this to match your URL configuration

    def test_get_chat_rooms(self):
        response = self.client.get(self.url)
        chat_rooms = ChatRoom.objects.all()
        serializer = ChartRoomSerializer(chat_rooms, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_chat_room(self):
        data = {'name': 'New Room'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChatRoom.objects.count(), 2)
        self.assertEqual(ChatRoom.objects.get(id=response.data['id']).name, 'New Room')

    def test_retrieve_chat_room(self):
        url = reverse('chatroom-detail', kwargs={'pk': self.chat_room.pk})
        response = self.client.get(url)
        serializer = ChartRoomSerializer(self.chat_room)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_chat_room(self):
        url = reverse('chatroom-detail', kwargs={'pk': self.chat_room.pk})
        data = {'name': 'Updated Room'}
        response = self.client.put(url, data, format='json')
        self.chat_room.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.chat_room.name, 'Updated Room')

    def test_delete_chat_room(self):
        url = reverse('chatroom-detail', kwargs={'pk': self.chat_room.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ChatRoom.objects.count(), 0)
# Create your tests here.

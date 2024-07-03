from django.urls import path
from rest_framework.routers import DefaultRouter

from chat.views import sumNumbersView
from chat.viewsets import ChatRoomViewSet


router = DefaultRouter()
router.register('chatroom', ChatRoomViewSet, basename='chatroom')
urlpatterns = router.urls
urlpatterns += [
    path('sum_numbers/', sumNumbersView, name='sum_numbers'),
]
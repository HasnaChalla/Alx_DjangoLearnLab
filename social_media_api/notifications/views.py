from django.shortcuts import render
from .models import Notification
from rest_framework import generics, permissions
from .serializers import NotificationSerializer
# Create your views here.


class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')

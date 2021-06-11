from django.shortcuts import render
from .serializers import TaskSerializers
from .models import Task
from rest_framework import generics, permissions

# Create your views here.


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

    permission_classes = [permissions.IsAuthenticated]

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
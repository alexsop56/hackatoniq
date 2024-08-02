from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from worker_shifts.models import Worker, WorkerShift
from .serializers import WorkerSerializer, ShiftSerializer



class WorkerListCreate(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class ShiftListCreate(generics.ListCreateAPIView):
    queryset = WorkerShift.objects.all()
    serializer_class = ShiftSerializer

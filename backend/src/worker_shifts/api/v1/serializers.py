from rest_framework import serializers
from worker_shifts.models import Worker, WorkerTask, Project
from datetime import date, time

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'name', 'inn', 'phone', 'rating']



class WorkerTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerTask
        fields = ['id', 'project', 'workers', 'workersCount', 'workersRequiredCount', 'views', 'workTypeTitle',
                  'price', 'startDate', 'startTime']
        extra_kwargs = {
            'workersCount': {'default': 0},
            'workersRequiredCount': {'default': 0},
            'views': {'default': 0},
            'price': {'default': 0},
            'startDate': {'default': date.today},
            'startTime': {'default': time(10, 0)},
        }

class ProjectSerializer(serializers.ModelSerializer):
    tasks = WorkerTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'address', 'startDate', 'startTime', 'price', 'totalPrice', 'isFinished',
                  'workTypeTitle', 'workersRequiredCount', 'workersCount', 'views', 'tasks']
        extra_kwargs = {
            'startDate': {'default': date.today},
            'startTime': {'default': time(10, 0)},
            'price': {'default': 0},
            'totalPrice': {'default': 0},
            'isFinished': {'default': False},
            'workTypeTitle': {'default': 'Покраска стен'},
            'workersRequiredCount': {'default': 0},
            'workersCount': {'default': 0},
            'views': {'default': 0},
        }
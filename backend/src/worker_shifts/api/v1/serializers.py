from rest_framework import serializers
from worker_shifts.models import Worker, WorkerTask, Project
from datetime import date, time

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'name', 'inn', 'phone', 'rating']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'address', 'start_date', 'start_time', 'price', 'total_price', 'is_finished',
                  'work_type_title', 'workers_required_count', 'workers_count', 'views']
        extra_kwargs = {
            'start_date': {'default': date.today},
            'start_time': {'default': time(10, 0)},
            'price': {'default': 0},
            'total_price': {'default': 0},
            'is_finished': {'default': False},
            'work_type_title': {'default': 'Покраска стен'},
            'workers_required_count': {'default': 0},
            'workers_count': {'default': 0},
            'views': {'default': 0},
        }


class WorkerTaskSerializer(serializers.ModelSerializer):
    workers = serializers.PrimaryKeyRelatedField(queryset=Worker.objects.all(), many=True)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = WorkerTask
        fields = ['id', 'project', 'workers', 'workers_count', 'workers_required_count', 'views', 'work_type_title',
                  'price', 'start_date', 'start_time']
        extra_kwargs = {
            'workers_count': {'default': 0},
            'workers_required_count': {'default': 0},
            'views': {'default': 0},
            'price': {'default': 0},
            'start_date': {'default': date.today},
            'start_time': {'default': time(10, 0)},
        }

    def create(self, validated_data):
        workers = validated_data.pop('workers')
        worker_task = WorkerTask.objects.create(**validated_data)
        worker_task.workers.set(workers)  # Set the many-to-many field with the provided workers IDs
        return worker_task

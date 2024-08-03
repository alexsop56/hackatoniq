from rest_framework import serializers
from worker_shifts.models import Worker, WorkerTask, Project


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'name', 'inn', 'phone', 'rating']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'workersRequiredCount', 'attentionCount', 'todoCount','address']
        extra_kwargs = {
            'workersRequiredCount': {'default': 0},
            'attentionCount': {'default': 0},
            'todoCount': {'default': 0}
        }


class WorkerTaskSerializer(serializers.ModelSerializer):
    workers = serializers.PrimaryKeyRelatedField(queryset=Worker.objects.all(), many=True)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = WorkerTask
        fields = ['id', 'project', 'workers', 'workersCount', 'workersRequiredCount','views','workTypeTitle']
        extra_kwargs = {
            'workersCount': {'default': 0},
            'workersRequiredCount': {'default': 0},
            'views': {'default': 0}
        }

    def create(self, validated_data):
        workers = validated_data.pop('workers')
        worker_task = WorkerTask.objects.create(**validated_data)
        worker_task.workers.set(workers)  # Set the many-to-many field with the provided workers IDs
        return worker_task
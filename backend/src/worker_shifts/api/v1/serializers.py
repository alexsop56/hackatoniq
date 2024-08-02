from rest_framework import serializers
from worker_shifts.models import Worker, WorkerShift

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerShift
        fields = '__all__'
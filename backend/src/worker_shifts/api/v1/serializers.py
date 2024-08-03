from rest_framework import serializers
from worker_shifts.models import Worker, WorkerShift

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'name']
class ShiftSerializer(serializers.ModelSerializer):
    workers = serializers.PrimaryKeyRelatedField(queryset=Worker.objects.all(), many=True)

    class Meta:
        model = WorkerShift
        fields = ['id', 'workers', 'start_time', 'end_time']

    def create(self, validated_data):
        workers = validated_data.pop('workers')
        shift = WorkerShift.objects.create(**validated_data)
        shift.workers.set(workers)  # Set the many-to-many field with the provided workers IDs
        return shift
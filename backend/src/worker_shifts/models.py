import uuid

from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100)
    inn = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkerShift(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.worker.name} ({self.start_time} - {self.end_time})"

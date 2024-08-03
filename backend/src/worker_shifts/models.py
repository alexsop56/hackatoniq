import uuid

from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100)
    inn = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkerShift(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    workers = models.ManyToManyField(Worker, related_name='shifts')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


    def __str__(self):
        worker_names = ', '.join(worker.name for worker in self.workers.all())
        return f"Shift ({worker_names}) ({self.start_time} - {self.end_time})"
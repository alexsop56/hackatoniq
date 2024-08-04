import uuid
import random
from django.db import models
from datetime import date, time
class Worker(models.Model):
    name = models.CharField(max_length=100)
    inn = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    rating = models.FloatField()

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'worker'


class Project(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    startDate = models.DateField(null = True, blank =True)
    startTime = models.TimeField(null = True, blank =True)  # Default time is 08:00 AM
    price = models.FloatField(default=0)
    totalPrice = models.FloatField(default=0)  # Random total price
    isFinished = models.BooleanField(default=0)  # Random finished status
    workTypeTitle = models.CharField(max_length=100, default="Покраска стен")
    workersRequiredCount = models.IntegerField(default=0)
    workersCount = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'project'

class WorkerTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    workers = models.ManyToManyField(Worker, related_name='tasks')
    workersCount = models.IntegerField(default=0)
    workersRequiredCount = models.IntegerField(default=0)
    workTypeTitle = models.CharField(max_length=100,default = 'ремонтные работы')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    startDate = models.DateField(default=date.today)
    startTime = models.TimeField(default=time(10, 0))
    views = models.IntegerField(default=0)
    def __str__(self):
        worker_names = ', '.join(worker.name for worker in self.workers.all())
        return f"Task ({worker_names}) ({self.start_date} {self.start_time})"

    class Meta:
        db_table = 'worker_task'
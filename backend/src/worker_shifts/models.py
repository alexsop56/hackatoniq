import uuid

from django.db import models

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
    workersRequiredCount = models.IntegerField()
    attentionCount = models.IntegerField()
    todoCount = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'project'

class WorkerTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    workers = models.ManyToManyField(Worker, related_name='shifts')
    workersCount = models.IntegerField()
    workersRequiredCount = models.IntegerField()
    views = models.IntegerField()
    workTypeTitle = models.CharField(max_length=100)
    # startTime = models.DateTimeField()
    # endTime = models.DateTimeField()


    def __str__(self):
        worker_names = ', '.join(worker.name for worker in self.workers.all())
        return f"Shift ({worker_names}) ({self.start_time} - {self.end_time})"


    class Meta:
        db_table = 'worker_task'

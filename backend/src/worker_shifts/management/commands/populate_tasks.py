from django.core.management.base import BaseCommand
from worker_shifts.models import Worker, Project, WorkerTask
from datetime import date, time
import uuid

class Command(BaseCommand):
    help = 'Populate the database with initial task data'

    def handle(self, *args, **kwargs):
        # Define the data to be inserted using camelCase keys
        tasks = [
            {
                "id": uuid.uuid4(),
                "projectId": 2,
                "workers": [
                    1,  # Worker IDs
                    2,
                    3,
                ],
                "workersCount": 8,
                "workersRequiredCount": 10,
                "workTypeTitle": 'Земляные работы по разработке котлована',
                "price": 100,
                "startDate": date(2024, 1, 1),
                "startTime": time(8, 0),
                "views": 13,
                "isFinished": True
            },
            {
                "id": uuid.uuid4(),
                "projectId": 2,
                "workers": [
                    1,
                    2,
                    3,
                    4,
                ],
                "workersCount": 5,
                "workersRequiredCount": 14,
                "workTypeTitle": 'Каменная кладка 2-го — 7-го эт.',
                "price": 100,
                "startDate": date(2024, 1, 1),
                "startTime": time(8, 0),
                "views": 13,
                "isFinished": False
            },
            {
                "id": uuid.uuid4(),
                "projectId": 3,
                "workers": [
                    1,
                    2,
                ],
                "workersCount": 7,
                "workersRequiredCount": 7,
                "workTypeTitle": 'Конструкции ж/б 1го',
                "price": 100,
                "startDate": date(2024, 1, 1),
                "startTime": time(8, 0),
                "views": 13,
                "isFinished": False
            }
        ]

        for task_data in tasks:
            # Retrieve the project and workers
            project = Project.objects.get(id=task_data['projectId'])
            workers = Worker.objects.filter(id__in=task_data['workers'])

            # Create or update the WorkerTask
            task, created = WorkerTask.objects.update_or_create(
                id=task_data['id'],
                defaults={
                    'project': project,
                    'workersCount': task_data['workersCount'],
                    'workersRequiredCount': task_data['workersRequiredCount'],
                    'workTypeTitle': task_data['workTypeTitle'],
                    'price': task_data['price'],
                    'startDate': task_data['startDate'],
                    'startTime': task_data['startTime'],
                    'views': task_data['views'],
                }
            )

            # Set workers for the task
            task.workers.set(workers)
            task.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with task data'))

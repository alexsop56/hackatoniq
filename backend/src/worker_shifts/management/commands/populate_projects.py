from django.core.management.base import BaseCommand
from worker_shifts.models import Project, WorkerTask
from datetime import date, time

class Command(BaseCommand):
    help = 'Populate the database with initial project data'

    def handle(self, *args, **kwargs):
        # Define the data to be inserted using camelCase keys
        projects = [
            {
                "id": 1,
                "title": 'ЖК Солнечный',
                "address": 'Кирова ул., 84',
                "startDate": None,
                "startTime": None,
                "price": 100000,
                "totalPrice": 0,
                "isFinished": False,
                "workTypeTitle": "Покраска стен",
                "workersRequiredCount": 13,
                "workersCount": 0,
                "views": 0
            },
            {
                "id": 2,
                "title": 'ЖК Перспективный',
                "address": 'Восточно-Кругликовская ул., 40',
                "startDate": None,
                "startTime": None,
                "price": 320000,
                "totalPrice": 19000,
                "isFinished": False,
                "workTypeTitle": "Покраска стен",
                "workersRequiredCount": 40,
                "workersCount": 37,
                "views": 16
            },
            {
                "id": 3,
                "title": 'ЖК Достояние',
                "address": 'ул. Конгрессная, 31',
                "startDate": None,
                "startTime": None,
                "price": 34000,
                "totalPrice": 9000,
                "isFinished": False,
                "workTypeTitle": "Покраска стен",
                "workersRequiredCount": 18,
                "workersCount": 14,
                "views": 3
            }
        ]

        # Insert the data
        for proj in projects:
            project, created = Project.objects.update_or_create(
                id=proj['id'],
                defaults={
                    'title': proj['title'],
                    'address': proj['address'],
                    'startDate': proj['startDate'],
                    'startTime': proj['startTime'],
                    'price': proj['price'],
                    'totalPrice': proj['totalPrice'],
                    'isFinished': proj['isFinished'],
                    'workTypeTitle': proj['workTypeTitle'],
                    'workersRequiredCount': proj['workersRequiredCount'],
                    'workersCount': proj['workersCount'],
                    'views': proj['views'],
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with project data'))

from django.urls import path
from .views import WorkerListCreate, ShiftListCreate

urlpatterns = [
    path('workers/', WorkerListCreate.as_view(), name='worker-list-create'),
    path('shifts/', ShiftListCreate.as_view(), name='shift-list-create'),
]
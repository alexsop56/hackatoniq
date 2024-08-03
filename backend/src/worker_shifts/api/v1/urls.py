from django.urls import path
from .views import (
    WorkerListCreate, WorkerDetail,
    WorkerTaskListCreate, WorkerTaskDetail,
    ProjectListCreate, ProjectDetail
)

urlpatterns = [
    # Worker URLs
    path('workers/', WorkerListCreate.as_view(), name='workers-list-create'),
    path('workers/<int:pk>/', WorkerDetail.as_view(), name='worker-detail'),

    # WorkerTask URLs
    path('tasks/', WorkerTaskListCreate.as_view(), name='tasks-list-create'),
    path('tasks/<int:pk>/', WorkerTaskDetail.as_view(), name='task-detail'),

    # Project URLs
    path('projects/', ProjectListCreate.as_view(), name='projects-list-create'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
]

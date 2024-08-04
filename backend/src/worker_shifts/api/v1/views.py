from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny

from worker_shifts.models import Worker, WorkerTask, Project
from .serializers import WorkerSerializer, WorkerTaskSerializer, ProjectSerializer

# Worker CRUD Views
class WorkerListCreate(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="получение списка исполнителей",
        responses={200: WorkerSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @csrf_exempt
    @swagger_auto_schema(
        operation_id="создание исполнителя",
        responses={201: WorkerSerializer},
        request_body=WorkerSerializer
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class WorkerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'patch', 'delete']

    @swagger_auto_schema(
        operation_id="получение исполнителя по id",
        responses={200: WorkerSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @csrf_exempt
    @swagger_auto_schema(
        operation_id="обновление исполнителя",
        responses={200: WorkerSerializer},
        request_body=WorkerSerializer
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @csrf_exempt
    @swagger_auto_schema(
        operation_id="удаление исполнителя",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# WorkerTask CRUD Views
class WorkerTaskListCreate(generics.ListCreateAPIView):
    queryset = WorkerTask.objects.all()
    serializer_class = WorkerTaskSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="получение списка заданий",
        responses={200: WorkerTaskSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @csrf_exempt
    @swagger_auto_schema(
        operation_id="создание задания",
        responses={201: WorkerTaskSerializer},
        request_body=WorkerTaskSerializer
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class WorkerTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkerTask.objects.all()
    serializer_class = WorkerTaskSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'patch', 'delete']

    @swagger_auto_schema(
        operation_id="получение задания по id",
        responses={200: WorkerTaskSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @csrf_exempt
    @swagger_auto_schema(
        operation_id="обновление задания",
        responses={200: WorkerTaskSerializer},
        request_body=WorkerTaskSerializer
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="удаление задания",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# Project CRUD Views
class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    @csrf_exempt
    @swagger_auto_schema(
        operation_id="получение списка проектов",
        responses={200: ProjectSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @csrf_exempt
    @swagger_auto_schema(
        operation_id="создание проекта",
        responses={201: ProjectSerializer},
        request_body=ProjectSerializer
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'patch', 'delete']

    @swagger_auto_schema(
        operation_id="получение проекта по id",
        responses={200: ProjectSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @csrf_exempt
    @swagger_auto_schema(
        operation_id="обновление проекта",
        responses={200: ProjectSerializer},
        request_body=ProjectSerializer
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @csrf_exempt
    @swagger_auto_schema(
        operation_id="удаление проекта",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny

from worker_shifts.models import Worker, WorkerShift
from .serializers import WorkerSerializer, ShiftSerializer


class WorkerListCreate(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [AllowAny]  # Assuming you want to restrict this to authenticated users

    @swagger_auto_schema(operation_id="получение списка исполнителей",

                         responses={200: WorkerSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_id="создание исполнителя",
        responses={200: WorkerSerializer(many=True), 201: WorkerSerializer}, request_body=WorkerSerializer)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ShiftListCreate(generics.ListCreateAPIView):
    queryset = WorkerShift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [AllowAny]  # Assuming you want to restrict this to authenticated users


    @swagger_auto_schema(
        operation_id="получение списка заданий",

        responses={
            200: ShiftSerializer(many=True)
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


    @swagger_auto_schema(operation_id="создание задания",
        responses={200: ShiftSerializer(many=True), 201: ShiftSerializer}, request_body=ShiftSerializer)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

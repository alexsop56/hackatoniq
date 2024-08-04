from worker_shifts.models import Worker, Project
from django.contrib import admin

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):

    search_fields = ('name',)

# Define admin class for WorkerShift model


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    search_fields = ('worker__name',)

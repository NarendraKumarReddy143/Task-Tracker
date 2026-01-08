from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'use_case_name',
        'uce_name',
        'tower',
        'task_type',
        'time_to_complete',
        'created_at',
    )

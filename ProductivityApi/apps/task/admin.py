from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    fields = ['user_id', 'title', 'description']
    list_display = ['user_id', 'title', 'description', 'created_at', 'updated_at']

admin.site.register(Task, TaskAdmin)
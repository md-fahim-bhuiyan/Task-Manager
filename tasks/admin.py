from django.contrib import admin
from .models import Task, Photo

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'priority', 'is_complete')
    list_filter = ('priority', 'is_complete')
    search_fields = ('title',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass



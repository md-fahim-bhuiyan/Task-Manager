from django.db import models
class Photo(models.Model):
    image = models.ImageField(upload_to='task_photos/')


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photos = models.ImageField(upload_to='task_photos/', null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    is_complete = models.BooleanField(default=False)


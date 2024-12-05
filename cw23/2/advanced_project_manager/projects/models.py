from django.db import models
from django.utils import timezone

class ActiveProjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(end_date__gte=timezone.now())
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    objects = models.Manager()
    active_projects = ActiveProjectManager()
    
    def __str__(self):
        return self.name
    
class TaskManager(models.Manager):
    def completed(self):
        return self.filter(completed=True)
    def incomplete(self):
        return self.filter(completed=False)
    
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    due_date = models.DateField()
    objects = TaskManager()
    def __str__(self):
        return self.title
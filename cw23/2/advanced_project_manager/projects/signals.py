from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task, Project

@receiver(post_save, sender=Task)
def update_project_status(sender, instance, **kwargs):
    project = instance.project
    if not project.tasks.filter(completed=False).exists():
        project.status = 'Completed'
        project.save()
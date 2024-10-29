from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Project, Task
from datetime import date

class ProjectModelTest(TestCase):
    def test_active_projects(self):
        Project.objects.create(name="Test Project", start_date=date.today(), end_date=date.today())
        active_projects = Project.active_projects.all()
        self.assertEqual(len(active_projects), 1)
        
class TaskSignalTest(TestCase):
    def test_project_completion_signal(self):
        project = Project.objects.create(name="Test Project", start_date=date.today(), end_date=date.today())
        Task.objects.create(project=project, title="Test Task 1", due_date=date.today(), completed=True)
        Task.objects.create(project=project, title="Test Task 2", due_date=date.today(), completed=True)
        project.refresh_from_db()
        self.assertEqual(project.status, "Completed")
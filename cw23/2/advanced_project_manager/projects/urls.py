from django.urls import path
from .views import ProjectListView,TaskCreateView, ProjectCreateView,TaskCreateView , ProjectUpdateView, TaskListView, TaskCompletionToggleView

urlpatterns = [
path('', ProjectListView.as_view(), name='project_list'),
path('create/', ProjectCreateView.as_view(), name='project_create'),
path('task_create/', TaskCreateView.as_view(), name='TaskCreateView'),
path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
path('tasks/', TaskListView.as_view(), name='task_list'),
path('task/<int:pk>/toggle/', TaskCompletionToggleView.as_view(), name='task_toggle'),
]

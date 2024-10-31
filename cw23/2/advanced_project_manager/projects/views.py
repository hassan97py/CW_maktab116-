# from django.shortcuts import render

# # Create your views here.
# from django.views.generic import ListView
# from django.utils import timezone
# from .models import Project

# class ProjectListView(ListView):
#     model = Project
#     template_name = 'projects/project_list.html'
#     context_object_name = 'projects'
#     def get_queryset(self):
#     # Sort projects by start date
#         sort_by = self.request.GET.get('sort', 'start_date')
#         return Project.objects.order_by(sort_by)
# #------------------------------------------------------------
# from django.views.generic.edit import CreateView, UpdateView
# from django.urls import reverse_lazy
# from .models import Project

# class ProjectCreateView(CreateView):
#     model = Project
#     fields = ['name', 'description', 'start_date', 'end_date']
#     template_name = 'projects/project_form.html'
#     success_url = reverse_lazy('project_list')
    
# class ProjectUpdateView(UpdateView):
#     model = Project
#     fields = ['name', 'description', 'start_date', 'end_date']
#     template_name = 'projects/project_form.html'
#     success_url = reverse_lazy('project_list')
    
# from django.shortcuts import get_object_or_404, redirect
# from django.views.generic import ListView
# from django.views import View
# from .models import Task, Project

# class TaskListView(ListView):
#     model = Task
#     template_name = 'projects/task_list.html'
#     context_object_name = 'tasks'
#     def get_queryset(self):
#         project_id = self.kwargs.get('project_id')
#         project = get_object_or_404(Project, id=project_id)
#         sort_by = self.request.GET.get('sort', 'due_date')
#         return project.tasks.order_by(sort_by)
    
# class TaskCompletionToggleView(View):
#     def post(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         task.completed = not task.completed
#         task.save()
#         return redirect('task_list', project_id=task.project.id)
    
# from django.views.decorators.cache import cache_page
# from django.utils.decorators import method_decorator

# class CachedProjectListView(ProjectListView):
#     @method_decorator(cache_page(30)) # Cache for 30 seconds
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
    
    
# class TaskListView(ListView):
#     model = Task
#     template_name = 'projects/task_list.html'
#     context_object_name = 'tasks'
#     def get_queryset(self):
#         project_id = self.kwargs.get('project_id')
#         project = get_object_or_404(Project, id=project_id)
#         sort_by = self.request.session.get('task_sort', 'due_date') # Use session to store sorting
#         return project.tasks.order_by(sort_by)
#     def post(self, request, *args, **kwargs):
#         self.request.session['task_sort'] = request.POST.get('sort')
#         return redirect('task_list', project_id=self.kwargs.get('project_id'))


# from .forms import ProjectForm

# class ProjectCreateView(CreateView):
#     form_class = ProjectForm
#     template_name = 'projects/project_form.html'
#     success_url = reverse_lazy('project_list')

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Project, Task
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


# Mixin for Sorting Projects and Tasks
class SortMixin:
    sort_param = 'start_date'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort',None)
        if sort == 'start_date':
            queryset = queryset.order_by(sort)
        return queryset
    



# 1. Project and Task List Views with Sorting
@method_decorator(cache_page(30), name='dispatch')
class ProjectListView(SortMixin, ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'
    sort_param = 'start_date'  # Default sorting for projects


from django.views.generic import ListView
from .models import Task

class TaskListView(SortMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    sort_param = 'due_date'  # Default sorting for tasks

    # def get_queryset(self):
    #     project_id = self.kwargs.get('project_id')  # Get project_id from URL
    #     return Task.objects.filter(project_id=project_id).order_by(self.sort_param)
    
    def get_queryset(self):
        sort_by = self.request.GET.get('sort', self.sort_param)
        return Task.objects.order_by(sort_by)

class TaskCreateView(CreateView):
    model = Task
    fields = ['project', 'title', 'description', 'completed','due_date']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        if end_date and start_date and end_date < start_date:
            form.add_error('end_date', 'End date cannot be before the start date.')
            return self.form_invalid(form)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('task_list', args=[self.object.project.id])


# class TaskListView(TaskSortMixin, ListView):
#     model = Task
#     template_name = 'task_list.html'
#     context_object_name = 'tasks'
#     sort_param = 'due_date'  # Default sorting for tasks


# 2. Project and Task Create and Update Views with Validation
class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'project_form.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        if end_date and start_date and end_date < start_date:
            form.add_error('end_date', 'End date cannot be before the start date.')
            return self.form_invalid(form)
        return super().form_valid(form)


class ProjectUpdateView(ProjectCreateView, UpdateView):
    success_url = reverse_lazy('project_list')


# class TaskCreateView(CreateView):
#     model = Task
#     fields = ['project', 'title', 'description', 'completed', 'due_date']
#     template_name = 'task_form.html'
#     success_url = reverse_lazy('task_list')


class TaskUpdateView(TaskCreateView, UpdateView):
    success_url = reverse_lazy('task_list')


# 3. Task Completion Toggle View
class TaskCompletionToggleView(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        task.completed = not task.completed
        task.save()
        return redirect('task_list')



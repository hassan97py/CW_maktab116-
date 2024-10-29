from django.shortcuts import render 
from django.views import View 
from .models import Task 
 
# class TaskListView(View): 
#     def get(self, request): 
#         tasks = Task.objects.all() 
#         return render(request, 'tasks/task_list.html', {'tasks': tasks})

# from django.views.generic import ListView 

# class TaskListView(ListView): 
#     model = Task 
#     template_name = 'tasks/task_list.html' 
#     context_object_name = 'tasks'
#-------------------------------------------------------------------------------------
from django.shortcuts import redirect 
from .forms import TaskForm 
 
# class TaskCreateView(View): 
#     def get(self, request): 
#         form = TaskForm() 
#         return render(request, 'tasks/task_form.html', {'form': form}) 
 
#     def post(self, request): 
#         form = TaskForm(request.POST) 
#         if form.is_valid(): 
#             form.save() 
#             return redirect('task_list') 
#         return render(request, 'tasks/task_form.html', {'form': form})
#-----------------------------------------------------------------------------------
from django.shortcuts import get_object_or_404 
 
# class TaskUpdateView(View): 
#     def get(self, request, pk): 
#         task = get_object_or_404(Task, pk=pk) 
#         form = TaskForm(instance=task) 
#         return render(request, 'tasks/task_form.html', {'form': form}) 
 
#     def post(self, request, pk): 
#         task = get_object_or_404(Task, pk=pk) 
#         form = TaskForm(request.POST, instance=task) 
#         if form.is_valid(): 
#             form.save() 
#             return redirect('task_list') 
#         return render(request, 'tasks/task_form.html', {'form': form})
#-------------------------------------------------------------------------------------
# class TaskDeleteView(View): 
#     def get(self, request, pk): 
#         task = get_object_or_404(Task, pk=pk) 
#         return render(request, 'tasks/task_confirm_delete.html', {'task': task}) 
 
#     def post(self, request, pk): 
#         task = get_object_or_404(Task, pk=pk) 
#         task.delete() 
#         return redirect('task_list')
    
#------------------------------------------------------------------------------------
from django.views.generic import ListView 

class TaskListView(ListView): 
    model = Task 
    template_name = 'tasks/task_list.html' 
    context_object_name = 'tasks'
    
#---------------------------------------------------------------------------------
from django.urls import reverse_lazy 
from django.views.generic.edit import CreateView 
 
class TaskCreateView(CreateView): 
    model = Task 
    form_class = TaskForm 
    template_name = 'tasks/task_form.html' 
    success_url = reverse_lazy('task_list')

#---------------------------------------------------------------------------------

from django.views.generic.edit import UpdateView 
 
class TaskUpdateView(UpdateView): 
    model = Task 
    form_class = TaskForm 
    template_name = 'tasks/task_form.html' 
    success_url = reverse_lazy('task_list')
    
#---------------------------------------------------------------------------------

from django.views.generic.edit import DeleteView 
 
class TaskDeleteView(DeleteView): 
    model = Task 
    template_name = 'tasks/task_confirm_delete.html' 
    success_url = reverse_lazy('task_list')
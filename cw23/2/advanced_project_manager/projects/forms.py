from django import forms
from .models import Project, Task
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']
        def clean(self):
            cleaned_data = super().clean()
            start_date = cleaned_data.get('start_date')
            end_date = cleaned_data.get('end_date')
            if end_date < start_date:
                raise forms.ValidationError("End date cannot be before start date.")
            return cleaned_data
        
# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['project', 'title', 'description', 'completed','due_date']
       
        # def clean(self):
        #     cleaned_data = super().clean()
        #     due_date = cleaned_data.get('due_date')
        #     if due_date and due_date < self.instance.project.start_date:
        #         raise forms.ValidationError("Due date cannot be before the project's start date.")
        #     return cleaned_data
#-------------------------------------------------------------------------------------------------

# class ProjectCreateView(CreateView):
#     form_class = ProjectForm
#     template_name = 'projects/project_form.html'
#     success_url = reverse_lazy('project_list')

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'completed', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

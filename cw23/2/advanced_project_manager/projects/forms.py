from django import forms
from .models import Project
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
        
        
#-------------------------------------------------------------------------------------------------

# class ProjectCreateView(CreateView):
#     form_class = ProjectForm
#     template_name = 'projects/project_form.html'
#     success_url = reverse_lazy('project_list')
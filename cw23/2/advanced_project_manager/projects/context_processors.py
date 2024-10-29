from .models import Project
def ongoing_projects(request):
    return {'ongoing_projects': Project.active_projects.all()}
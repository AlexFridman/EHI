from django.views import generic

from .models import Faculty


class FacultyIndexView(generic.ListView):
    template_name = 'faculty/index.html'
    context_object_name = 'faculty_list'

    def get_queryset(self):
        return Faculty.objects.all()


class FacultyDetailView(generic.DetailView):
    model = Faculty
    template_name = 'faculty/detail.html'
    context_object_name = 'faculty'

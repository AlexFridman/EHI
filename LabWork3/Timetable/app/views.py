from django.views import generic

from .models import Faculty, Teacher


class FacultyIndexView(generic.ListView):
    template_name = 'app/faculty/index.html'
    context_object_name = 'faculty_list'

    def get_queryset(self):
        return Faculty.objects.all()


class FacultyDetailView(generic.DetailView):
    model = Faculty
    template_name = 'app/faculty/detail.html'
    context_object_name = 'faculty'


class TeacherIndexView(generic.ListView):
    template_name = 'app/teacher/index.html'
    context_object_name = 'teacher_list'

    def get_queryset(self):
        return Teacher.objects.all()


class TeacherDetailView(generic.DetailView):
    model = Teacher
    template_name = 'app/teacher/detail.html'
    context_object_name = 'teacher'

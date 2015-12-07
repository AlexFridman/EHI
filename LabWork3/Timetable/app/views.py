from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

from .models import Faculty, Teacher


class FacultyIndexView(generic.ListView):
    template_name = 'app/faculty/index.html'
    context_object_name = 'faculty_list'

    def get_queryset(self):
        return Faculty.objects.all()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(FacultyIndexView, self).dispatch(request, *args, **kwargs)


class FacultyDetailView(generic.DetailView):
    model = Faculty
    template_name = 'app/faculty/detail.html'
    context_object_name = 'faculty'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(FacultyDetailView, self).dispatch(request, *args, **kwargs)


class TeacherIndexView(generic.ListView):
    template_name = 'app/teacher/index.html'
    context_object_name = 'teacher_list'

    def get_queryset(self):
        return Teacher.objects.all()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TeacherIndexView, self).dispatch(request, *args, **kwargs)


class TeacherDetailView(generic.DetailView):
    model = Teacher
    template_name = 'app/teacher/detail.html'
    context_object_name = 'teacher'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TeacherDetailView, self).dispatch(request, *args, **kwargs)

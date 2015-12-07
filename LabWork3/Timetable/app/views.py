from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views import generic

from .forms import TimetableSearchForm
from .models import Faculty, Teacher, Class, Group


def index(request):
    return render_to_response('app/index.html', context_instance=RequestContext(request))


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


class TimetableView(generic.ListView):
    template_name = 'app/timetable/classes.html'
    context_object_name = 'class_list'

    def get_queryset(self):
        if 'group' not in self.kwargs['group']:
            pass
        try:
            group_id = Group.objects.filter(number=self.kwargs['group']).first().id
        except AttributeError:
            pass

        return Class.objects.filter(group=group_id).all()


class TimetableSearchView(generic.FormView):
    template_name = 'app/timetable/index.html'
    form_class = TimetableSearchForm

    def form_valid(self, form):
        if 'group' not in form.data:
            pass
        return HttpResponseRedirect('/timetable/{}'.format(form.data['group']))

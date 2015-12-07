from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from app.models import Faculty, Group, Class, Place, Teacher, Profile


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['number', 'faculty']
    list_filter = ['faculty']
    search_fields = ['faculty']


class ClassAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'subject_name', 'group', 'teacher', 'place']
    list_filter = ['start_time', 'subject_name', 'group', 'teacher', 'place']
    search_fields = ['subject_name', 'group']


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['housing', 'room']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    list_filter = ['position']
    search_fields = ['name']


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (ProfileInLine,)


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Teacher, TeacherAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

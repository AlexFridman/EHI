from django.contrib import admin

from app.models import Faculty, Group, Class, Place, Teacher


class FacultyAdmin(admin.ModelAdmin):
    pass


class GroupAdmin(admin.ModelAdmin):
    pass


class ClassAdmin(admin.ModelAdmin):
    pass


class PlaceAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Teacher, TeacherAdmin)

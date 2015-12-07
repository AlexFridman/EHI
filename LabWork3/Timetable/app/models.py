from django.db import models


class Place(models.Model):
    room = models.TextField(null=True)
    housing = models.IntegerField()


class Faculty(models.Model):
    name = models.TextField()


class Group(models.Model):
    number = models.IntegerField()
    faculty = models.ForeignKey(Faculty)


class Teacher(models.Model):
    name = models.TextField()
    position = models.TextField()


class Class(models.Model):
    name = models.TextField()
    place = models.ForeignKey(Place)
    teacher = models.ForeignKey(Teacher)
    group = models.ForeignKey(Group)

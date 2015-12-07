from django.db import models


class Place(models.Model):
    room = models.TextField(null=True)
    housing = models.IntegerField()

    def __str__(self):
        return '{}-{}'.format(self.room, self.housing)


class Faculty(models.Model):
    class Meta:
        verbose_name_plural = "faculties"

    name = models.TextField()
    description = models.TextField()
    #pic = models.ImageField(upload_to='static/app/img/faculty', default='static/app/img/faculty/None/no-img.jpg')

    def __str__(self):
        return self.name


class Group(models.Model):
    number = models.IntegerField()
    faculty = models.ForeignKey(Faculty)

    def __str__(self):
        return str(self.number)


class Teacher(models.Model):
    name = models.TextField()
    position = models.TextField()

    def __str__(self):
        return '{}, {}'.format(self.name, self.position)


class Class(models.Model):
    class Meta:
        verbose_name_plural = "classes"

    subject_name = models.TextField()
    place = models.ForeignKey(Place)
    teacher = models.ForeignKey(Teacher)
    group = models.ForeignKey(Group)
    start_time = models.TimeField()

    def __str__(self):
        return '{}|{}|{}|{}|{}'.format(self.start_time, self.subject_name, self.group, self.teacher, self.place)

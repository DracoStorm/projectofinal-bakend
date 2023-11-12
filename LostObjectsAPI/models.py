from django.db import models

# Create your models here.


class Student(models.Model):
    register = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=15, default='student-firstname')
    last_name = models.CharField(max_length=15, default='student-lastname')

    def __str__(self):
        return self.name


class Place(models.Model):
    faculty = models.CharField(max_length=50)

    def __str__(self):
        return self.faculty


class LostObject(models.Model):
    object_name = models.CharField(max_length=50, default='object-name')
    place = models.ForeignKey(Place, on_delete=models.DO_NOTHING, default=0)
    img = models.CharField(max_length=50)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.object_name

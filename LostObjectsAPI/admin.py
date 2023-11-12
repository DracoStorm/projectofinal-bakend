from django.contrib import admin
from LostObjectsAPI.models import LostObject, Place, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Place)
admin.site.register(LostObject)

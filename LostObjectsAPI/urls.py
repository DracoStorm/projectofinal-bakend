"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from LostObjectsAPI.views import lost_object, lostobject_details, student, student_details, valid_place, lostobject_by_place, lostobject_by_important, lostobject_by_not_important, lostobject_by_name
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('lost_object/', lost_object),
    path('lost_object/<int:id>', lostobject_details),
    path('lost_object/places/', valid_place),
    path('lost_object/by_place/<int:id>', lostobject_by_place),
    path('lost_object/by_important', lostobject_by_important),
    path('lost_object/by_not_important', lostobject_by_not_important),
    path('lost_object/by_name/<str:obj_name>', lostobject_by_name),
    path('student/', student),
    path('student/<int:register>', student_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)

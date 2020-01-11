from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('hello/',view_hello_world_test),
    path('list/',view_student_lists),
    path('studentform/',view_student_form),
    path('studentform/save',view_studentdata_save),
    ]






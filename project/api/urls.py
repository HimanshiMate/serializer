from django.urls import path
from .views import *

urlpatterns = [
    # path('stu_info/<int:pk>',student_detail,name='name'),
    path('stu_list/',student_list,name='students_list'),
    # path('stu_api/',student_api,name='students_api'),

]
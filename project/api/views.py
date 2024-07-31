from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

def student_list(request):
    # stu=Student.objects.create(stu_name='himanshi',stu_city='bhopal',stu_contact=5695768540)
    # print(stu.stu_name,stu.stu_city,stu.stu_contact)
    # stu=Student.objects.create(stu_name='vedansh',stu_city='bhopal',stu_contact=769502385)
    # print(stu.stu_name,stu.stu_city,stu.stu_contact)
    # stu=Student.objects.create(stu_name='azhan',stu_city='bhopal',stu_contact=556947640)
    # print(stu.stu_name,stu.stu_city,stu.stu_contact)
    # stu=Student.objects.get(id=6)
    # stu.delete()

    # stu,created=Student.objects.get_or_create(stu_name='himanshi',stu_city='balaghat',stu_contact=46869900)
    # print(stu.id,stu.stu_name,stu.stu_city)
    # print(created)
    # stu=Student.objects.all()
    # print(stu)
    # print("stu.values()=",stu.values())
    # print("stu.values_list()=",stu.values_list())
    #print("stu.values_list(col1,col2)=",stu.values_list('stu_name','stu_city'))
    # serializer = StudentSerializer(stu,many=True) 
    # print(serializer)
    # print(serializer.data)
    # json_data= JSONRenderer().render(serializer.data)
    # print("json_data=",json_data)
    
    # return HttpResponse(json_data,content_type='application/json')  
    # return JsonResponse(serializer.data,safe=False)

    st_data=Student.objects.get(id=11)
    serializer=StudentSerializer(st_data)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)
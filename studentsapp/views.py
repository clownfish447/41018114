from django.shortcuts import render
from studentsapp.models import student

def listall(request):  
    students = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "listall.html", locals())
	
def a41018114(request):  
    students = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "a41018114.html", locals())		

from django.http import HttpResponse
from django.shortcuts import render
from APP2.models import Student
import random


# Create your views here.
def lala(request):
    return render(request, 'lala.html')


# 增加数据
def add_student(request):
    student = Student()
    student.s_name = 'Lily%d' % random.randrange(100)
    student.save()
    return HttpResponse('Add %s success' % student.s_name)


# 查询数据
def get_student(request):
    students = Student.objects.all()
    for student in students:
        print(student.s_name)
    context = {
        'ha': 'haha',
        'xi': 'xixi',
        'students': students
    }
    return render(request, 'student_list.html', context=context)


# 更新与删除数据基于查询
def update_student(request):
    student = Student.objects.get(pk=2)
    student.s_name = 'Jack'
    student.save()
    return HttpResponse('update student success')


# 删除数据
def delete_student(request):
    student = Student.objects.get(pk=3)
    student.delete()
    student.save()
    return HttpResponse('delete student success')

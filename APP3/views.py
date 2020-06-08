import random
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from APP3.models import Grade, Student


# Create your views here.
def index3(request):
    index3 = loader.get_template('index3.html')
    context = {
        'student_name': 'jack'
    }
    # 渲染成html
    result = index3.render(context=context)
    print(result)
    return HttpResponse(result)

# 增加数据--班级
def add_grade(request):
    grade = Grade()
    grade.g_name = 'python%d' % random.randrange(100)
    grade.save()
    return HttpResponse('Add %s success' % grade.g_name)
# 增加数据--学生
def add_student(request):
    Student.objects.create(s_name='Amy8', s_grade_id='2')
    # student = Student()
    # student.s_name = 'Amy%d' % random.randrange(100)
    # student.s_grade_id = '%d' % random.randrange(100)
    # student.save()
    return HttpResponse('Add student success')
# 找出指定学生的班级名称
def get_grade(request):
    student = Student.objects.get(pk=10)
    grade = student.s_grade
    return HttpResponse('Grade %s' % grade.g_name)

# 获取指定班级的所有学生
def get_student(request):
    grade = Grade.objects.get(pk=4)
    students = grade.student_set.all()
    context = {'students': students}
    return render(request,'student.html',context=context)
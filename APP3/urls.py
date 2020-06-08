from django.urls import path
from APP3 import views

urlpatterns = [
    path('index3/', views.index3),
    path('addgrade/', views.add_grade),
    path('getgrade/', views.get_grade),
    path('addstudent/', views.add_student),
    path('getstudent/', views.get_student),

]
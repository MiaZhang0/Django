from django.urls import path
from APP2 import views

urlpatterns = [
    path('lala/', views.lala),
    path('addstudent/', views.add_student),
    path('getstudent/', views.get_student),
    path('updatestudent/', views.update_student),
    path('delstudent/', views.delete_student),
]
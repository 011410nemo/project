"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path , include
from accounts.views import *
from book.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #صفحات تسجيل الدخول
    path('' , index , name = 'home'),
    path('student_login/' , student_login , name='student_login'),
    path('teacher_login/' , teacher_login , name='teacher_login'),
    path('login_s/' ,login_s , name='login_s'),
    path('login_t/' ,login_t , name='login_t'),
    path('logout/' ,log_out , name='log_out'),
    
    #صفحات الطلاب 
    path('student_layout',index_student,name='student_layout'),
    path('view_lesson/<int:id>',view_lesson , name='view_lesson'),
    path('student_exmple/<int:page>',student_exmple , name='student_exmple'),
    path('student_aims/',student_aims , name='student_aims'),
    path('student_exam/',student_exam , name='student_exam'),
    path('pre_exam/',pre_exam , name='pre_exam'),
    path('exam/<int:id>', exams , name='exam'),
    path('pre_exam_question/<int:id>', pre_exam_question , name='pre_exam_question'),
    path('result/',result,name='result'),
    path('pre_result/',pre_result,name='pre_result'),
    path('contact_us/',contact,name='contact'),
    path('download_books/<int:id>/download',download_books,name='download_books'),
   # path('view_aim/<int:id>',view_aim1 , name='view_aim1'),
    #صفحات المعلمين 
    path('teacher_lesson/',teacher_lesson , name='teacher_lesson'),
    path('teacher_paragraph/',teacher_paragraph , name='teacher_paragraph'),
    path('teacher_exm/',teacher_exm , name='teacher_exm'),
    path('teacher_exer/',teacher_exer , name='teacher_exer'),
    path('teacher_aim/',teacher_aim , name='teacher_aim'),
    path('teacher_exam/',teacher_exams , name='teacher_exams'),
    #اضافة المساراات الخاصة بالقواعد
    path('add_content/' ,add_content , name ='add_content'),
    path('paragraph/' , paragraph ,name='paragraph'),
    path('add_aim/' , add_aim , name ='add_aim'),
    path('add_exmple/',add_exmples ,name='add_exmple'),
    path('add_exersize/' , add_exers , name='add_exer'),
    path('add_quizs/' , add_quizs , name='add_quiz')
]
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

from django.shortcuts import render
from .models import *
from book.models import *
from book.views import *
from django.http import HttpResponse ,HttpResponseRedirect , HttpResponseNotFound
from django.contrib.auth import authenticate ,login , logout
# Create your views here.
def index(request):
    return render(request , 'index.html' , {})
def student_login(request):
    return render(request , 'student_login.html' , {})
def teacher_login(request):
    return render(request , 'teacher_login.html',{})
#تسجيل دخول الطالب
def login_s(request):
   link ='/view_lesson/' +str(1)
   if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']
        log = authenticate(username = username , password = password)
        if log is not None:
            if log.is_student == True:
                login(request , log)
                return HttpResponseRedirect(link)
            #else:
             #   return HttpResponse('not student sign in again')
        return HttpResponseRedirect('/')

#تسجيل دخول المعلم
def login_t(request):
   if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']
        log = authenticate(username = username , password = password)
        if log is not None:
            if log.is_teacher == True:
                login(request , log)
                return HttpResponseRedirect('/teacher_lesson')
            #else:
             #   return HttpResponse('not student sign in again')
        return HttpResponseRedirect('/')
#تسجيل الخروج
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

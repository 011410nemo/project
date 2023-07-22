from django.shortcuts import render
from .models import *
from django.http import HttpResponse ,HttpResponseRedirect , HttpResponseNotFound
from django.contrib.auth import authenticate ,login , logout
from django.core.paginator import Paginator
from .sent_tokenize import sent_token
from .lda import key_word
from .highlight import highlight
from django.core.cache import cache
from django.http import FileResponse
import random
# Create your views here.
#صفحة عرض الدروس
def index_student(request):
     lesson =add_lesson.objects.all()
     return render(request , 'student_layout.html',{'lessons':lesson })
def download_books(request,id):
     book = download_book.objects.get(id =id)
     file_path = book.book_file.path
     response = FileResponse(open(file_path, 'rb'), as_attachment=True)
     return response
    # return render(request , 'view_lesson.html' , {'books':book})
def view_lesson(request,id):
     lesson =add_lesson.objects.all()
     lesson_name = add_lesson.objects.get(id = id)
     return render(request , 'view_lesson.html',{'lessons':lesson , 'name':lesson_name  })
def exams(request,id):
     lesson =add_lesson.objects.all()
     lesson_name =add_lesson.objects.get(id = id) 
     quizs = add_quiz.objects.all()   
     return render(request , 'exam2.html',{'name':lesson_name,'lessons':lesson , 'quiz':quizs})
def pre_exam_question(request,id):
     lesson =add_lesson.objects.all()
     lesson_name =add_lesson.objects.get(id = id) 
     quizs = add_quiz.objects.all()   
     sample_num = 20
     random_object = random.sample(list(quizs), sample_num)
     return render(request , 'pre_exam_question.html',{'name':lesson_name,'lessons':lesson , 'quiz':quizs , 'randoms':random_object})
def result(request):
     lesson =add_lesson.objects.all()
     if request.method == 'POST':
          questions = add_quiz.objects.all()
          score=0
          wrong=0
          correct=0
          total=0
          for q in questions:
               total+=1
               if q.correct_ans == request.POST.get(q.question):
                    score +=10
                    correct +=1
               else:
                    wrong +=1
          percent = score/(total*10) * 100
          context = {
               'score':score,
               'correct':correct,
               'wrong':wrong,
               'percent':percent,
               'total':total,
               'lessons':lesson
          }
          return render(request , "resualt.html",context)
def pre_result(request):
     lesson =add_lesson.objects.all()
     if request.method == 'POST':
          questions = add_quiz.objects.all()
          score=0
          wrong=0
          correct=0
          total=0
          for q in questions:
               total+=1
               if q.correct_ans == request.POST.get(q.question):
                    score +=10
                    correct +=1
               else:
                    wrong +=1
          percent = score/(total*10) * 100
          context = {
               'score':score,
               'correct':correct,
               'wrong':wrong,
               'percent':percent,
               'total':total,
               'lessons':lesson
          }
          return render(request , "pre_exam_resualt.html",context)

#صفحة الأمثلة
def student_exmple(request ,page):
     lesson =add_lesson.objects.all()
     aim1 = lesson_aim.objects.filter(lapnum = page , latype = 1)
     aim2 = lesson_aim.objects.filter(lapnum = page , latype = 2)
     exmple1 =add_exmple.objects.filter(expnum = page ,exaimtype = 1)
     exmple2 =add_exmple.objects.filter(expnum = page ,exaimtype = 2)
     exer1 =add_exer.objects.filter(expnum = page ,exaimtype = 1)
     exer2 =add_exer.objects.filter(expnum = page ,exaimtype = 2)
     #------------------------
     #خاص بجزء تقسيم النص إلى جمل
     p = add_paragraph.objects.get(id = page)
     #هذا الجزء خاص لتسريع عمل الخوارزمية وسرعة التحميل فى الموقع 
     keywords = cache.get('keywords')
     keywords = key_word(p.paragraph)
     cache.set('keywords', keywords, timeout=3600)
     #keywords = key_word(p.paragraph)
     highlights=highlight(p.paragraph)
     sent = sent_token(highlights)
     #خاص بالباجينتور
     paragraph =add_paragraph.objects.get_queryset().order_by('id')
     paginator = Paginator(paragraph ,1)
     page_number = request.GET.get('page',page)
     paragraph = paginator.get_page(page_number)
     
     return render(request , 'example.html',{'paragraphs':paragraph , 'lessons':lesson ,'aim1':aim1 ,
                                                  'aim2':aim2 , 'exmple1':exmple1,'exmple2':exmple2  ,
                                                  'exer1':exer1 , 'exer2':exer2 , 'sents':sent,
                                                  'keyword':keywords,'high':highlights })
#صفحة عرض أهداف
def student_aims(request):
     lesson =add_lesson.objects.all()
     aim1 = lesson_aim.objects.all()
     
     return render(request , 'aims.html',{'lessons':lesson ,'aim1':aim1})
#صفحة الاختبار التحصيلى (البداية ) 
def student_exam(request):
     lesson =add_lesson.objects.all()
     return render(request , 'exam1.html',{'lessons':lesson})
def pre_exam(request):
     lesson =add_lesson.objects.all()
     return render(request , 'pre_exam.html',{'lessons':lesson})
#صفحات المدرس - إضافة درس - فقرات - أهداف - أمثلة - تمارين
def teacher_lesson(request):
     return render(request , 'add_lesson.html',{})
def teacher_paragraph(request):
     lessons = add_lesson.objects.all()
     return render(request , 'add_paragraph.html',{'lesson':lessons})
def teacher_aim(request):
     lessons = add_lesson.objects.all()
     paragraphs =add_paragraph.objects.all()
     aim = aims.objects.all()
     return render(request , 'add_aims.html',{'lesson':lessons , 'paragraph':paragraphs , 'aims':aim})
def teacher_exm(request):
     lesson_aims = lesson_aim.objects.all()
     paragraphs =add_paragraph.objects.all()
     aim = aims.objects.all()
     return render(request , 'add_exmple.html',{'aim':lesson_aims ,'paragraph':paragraphs,'aims':aim})
def teacher_exer(request):
     lesson_aims = lesson_aim.objects.all()
     paragraphs =add_paragraph.objects.all()
     aim = aims.objects.all()
     return render(request , 'add_exersize.html',{'aim':lesson_aims , 'paragraph':paragraphs,'aims':aim})
def teacher_exams(request):
     lessons = add_lesson.objects.all()
     return render(request , 'add_exam.html',{'lesson':lessons})
def contact(request):
     lesson =add_lesson.objects.all()
     return render(request , 'contact.html',{'lessons':lesson})
#****************************************************************
#models
#****************************************************************
#add content
def add_content(request):
    content_name = request.POST['content_name']
    lesson_name = request.POST['lesson_name']
    lesson_num = request.POST['lesson_num']
    lesson_file = request.POST['lesson_file']
    new = add_lesson(Cname = content_name , lname =lesson_name,lnumber =lesson_num , lfile = lesson_file )
    new.save()
  #  return HttpResponse("DATA SAVED")
    return HttpResponseRedirect("/teacher_lesson")
#--------------------------------------------------------
#add paragraph 
def paragraph(request):
    lesson_id = request.POST['graph']
    lesson = add_lesson.objects.get(id =lesson_id )
    paragraph_number = request.POST['p_num']
    p_paragraph = request.POST['p_paragraph'] 
    new = add_paragraph(plname =lesson , pnumber =paragraph_number,paragraph =p_paragraph)
    new.save()
    return HttpResponseRedirect("/teacher_paragraph")
#----------------------------------------------------------------------------
#add aim
def add_aim(request):
     lesson_id =request.POST['graph']
     lessons = add_lesson.objects.get(id =lesson_id )
     paragraph_id = request.POST['graph_num']
     paragraph_num = add_paragraph.objects.get(id = paragraph_id)
     aim_text = request.POST['lesson_aim']
     aim_id =request.POST['aim_type']
     aim_type = aims.objects.get(id =aim_id )
     new = lesson_aim(lalname = lessons , lapnum = paragraph_num , laAim = aim_text , latype = aim_type)
     new.save()
     return HttpResponseRedirect("/teacher_aim")
#--------------------------------------------------------
#add exmple
def add_exmples(request):
     aim_id=request.POST['aim_text']
     aim_text = lesson_aim.objects.get(id = aim_id)
     aim_ids =request.POST['aim_type']
     aim_type = aims.objects.get(id =aim_ids )
     paragraph_id = request.POST['graph_num']
     paragraph_num = add_paragraph.objects.get(id = paragraph_id)
     exname = request.POST['exmple_name']
     exanswer = request.POST['exmple_answer']
     new = add_exmple(expnum =paragraph_num , exaim = aim_text ,exaimtype=aim_type, exexmple = exname , exanswer = exanswer )
     new.save()
     return HttpResponseRedirect("/teacher_exm")


#---------------------------------------------------------
#add exersize
def add_exers(request):
     aim_id = request.POST['aim_text']
     aitext =lesson_aim.objects.get(id = aim_id)
     aim_ids =request.POST['aim_type']
     aim_type = aims.objects.get(id =aim_ids )
     paragraph_id = request.POST['graph_num']
     paragraph_num = add_paragraph.objects.get(id = paragraph_id)
     exername = request.POST['exer_name']
     exans1 = request.POST['lesson_answer1']
     exans2 = request.POST['lesson_answer2']
     exans3= request.POST['lesson_answer3']
     exans4 = request.POST['lesson_answer4']
     excorrect = request.POST['correct_answer']
     new = add_exer(expnum =paragraph_num ,
                    exeraim = aitext,exersize =exername,exer1 =exans1,
                    exaimtype=aim_type,exer2=exans2,
                    exer3=exans3,exer4=exans4,exer_correct=excorrect)
     new.save()
     return HttpResponseRedirect("/teacher_exer")

#-----------------------------------------------------------------
#add_quiz
def add_quizs(request):
     lesson_id =request.POST['graph']
     lessons = add_lesson.objects.get(id =lesson_id )
     question = request.POST['question']
     ans1 = request.POST['lesson_answer1']
     ans2 = request.POST['lesson_answer2']
     ans3= request.POST['lesson_answer3']
     ans4 = request.POST['lesson_answer4']
     correct = request.POST['correct_answer']
     degrees = request.POST['answer_degree']
     new = add_quiz(quiz_lesson_lname =lessons ,
                    question = question,ans1 =ans1,
                    ans2=ans2,ans3=ans3,
                    ans4=ans4,correct_ans=correct,degree=degrees)
     new.save()
     return HttpResponseRedirect("/teacher_exam")
     

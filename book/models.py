from django.db import models
# Create your models here.
class add_lesson(models.Model):
    Cname = models.CharField(max_length=100 , verbose_name='content name')
    lname =models.CharField(max_length=100 , verbose_name='lesson name')
    lnumber =models.CharField(max_length=100 , verbose_name='lesson number')
    lfile=models.FileField(upload_to='lesson_file/', verbose_name='lesson file')

    def __str__(self) -> str:
        return self.lname

class download_book(models.Model):
    lesson_book = models.ForeignKey(add_lesson ,on_delete=models.CASCADE , verbose_name='lesson name')
    book_file = models.FileField(upload_to='book_file/', verbose_name='book file')
    
class add_paragraph(models.Model):
    plname = models.ForeignKey(add_lesson ,on_delete=models.CASCADE , verbose_name='lesson name')
    pnumber = models.CharField(max_length=100 , verbose_name='paragraph number')
    paragraph = models.TextField(verbose_name='paragraph')

    def __str__(self) -> str:
        return self.pnumber



class lesson_aim(models.Model):
    lalname = models.ForeignKey(add_lesson ,on_delete=models.CASCADE , verbose_name='lesson name')
    lapnum =models.ForeignKey(add_paragraph ,on_delete=models.CASCADE , verbose_name='paragph number')
    laAim = models.CharField(max_length=200 , verbose_name='lesson aim')
    latype = models.ForeignKey('aims' ,on_delete=models.CASCADE , verbose_name='aim type' , blank=True , null=True)

    def __str__(self) -> str:
        return self.laAim

class aims(models.Model):
    aim = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.aim

class add_exmple(models.Model):
    expnum =models.ForeignKey(add_paragraph ,on_delete=models.CASCADE , verbose_name='parageaph number' ,blank=True , null=True)
    exaim = models.ForeignKey(lesson_aim ,on_delete=models.CASCADE , verbose_name='lesson aim')
    exaimtype =  models.ForeignKey('aims' ,on_delete=models.CASCADE , verbose_name='aim type' , blank=True , null=True)
    exexmple =models.TextField(verbose_name='exmple')
    exanswer = models.CharField(max_length=200 ,verbose_name='answer')
    def __str__(self) -> str:
        return self.exexmple

class add_exer(models.Model):
    expnum =models.ForeignKey(add_paragraph ,on_delete=models.CASCADE , verbose_name='parageaph number',blank=True , null=True)
    exeraim = models.ForeignKey(lesson_aim ,on_delete=models.CASCADE , verbose_name='lesson aim')
    exaimtype =  models.ForeignKey('aims' ,on_delete=models.CASCADE , verbose_name='aim type' , blank=True , null=True)
    exersize =models.TextField(verbose_name='exersize')
    exer1 = models.CharField(max_length=200 ,verbose_name='answer 1')
    exer2 = models.CharField(max_length=200 ,verbose_name='answer 2')
    exer3 = models.CharField(max_length=200 ,verbose_name='answer 3')
    exer4 = models.CharField(max_length=200 ,verbose_name='answer 4')
    exer_correct = models.CharField(max_length=200 ,verbose_name='correct answer')
    def __str__(self) -> str:
        return self.exersize
    
class add_quiz(models.Model):
    quiz_lesson_lname = models.ForeignKey(add_lesson ,on_delete=models.CASCADE , verbose_name='lesson name')
    question =models.TextField(verbose_name='question')
    ans1 = models.CharField(max_length=200 ,verbose_name='answer 1')
    ans2 = models.CharField(max_length=200 ,verbose_name='answer 2')
    ans3 = models.CharField(max_length=200 ,verbose_name='answer 3')
    ans4 = models.CharField(max_length=200 ,verbose_name='answer 4')
    correct_ans = models.CharField(max_length=200 ,verbose_name='correct answer')
    degree = models.CharField(max_length=200 ,verbose_name='degree')
    
    def __str__(self) -> str:
        return self.question

    
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db.models.signals import post_save

# Create your models here.
class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

   # class Meta(AbstractUser.Meta):
    #    swappable = 'AUTH_USER_MODEL'

class Student(models.Model):
    user = models.OneToOneField(CustomUser,verbose_name='user', on_delete=models.CASCADE, primary_key=True )
    grade = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Student, self).save(*args, **kwargs)

#class Teacher(models.Model):
   # user = models.OneToOneField(User, on_delete=models.CASCADE ,primary_key=True)
    #grade = models.CharField(max_length=100)
    #slug = models.SlugField(blank=True, null=True)

    #def __str__(self):
     #   return self.user.username

    #def save(self, *args, **kwargs):
     #   if not self.slug:
      #      self.slug = slugify(self.user.username)
       # super(Teacher, self).save(*args, **kwargs)
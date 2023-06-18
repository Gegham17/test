from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class StudentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, blank=True)
    stream = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Student Info'



class Stu_Question(models.Model):
    professor = None
    student = models.ForeignKey(User, limit_choices_to={'groups__name': "Student"}, on_delete=models.CASCADE, null=True)
    choice = models.CharField(max_length=3, default="E")

   
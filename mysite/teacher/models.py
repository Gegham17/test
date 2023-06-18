from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class TeacherInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, blank=True)
    stream = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Teacher Info'


class Appointment(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True,on_delete=models.DO_NOTHING)
	date=models.CharField(max_length=50)
	time_start=models.CharField(max_length=50)
	time_end=models.CharField(max_length=50)
	room_number=models.CharField(max_length=50)
	appointment_with=models.CharField(max_length=50,blank=True)
	update_time=models.DateField(auto_now=True, auto_now_add=False)
	frist_time=models.DateField(auto_now=False, auto_now_add=True)
    

	def __str__(self):
		return self.date
	def __str__(self): 
		return self.time_start
	def __str__(self): 
		return self.time_end
	def __str__(self): 
		return self.room_number
	def __str__(self): 
		return self.appointment_with


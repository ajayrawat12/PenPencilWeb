from django.db import models
from .views import *
from django.contrib.auth.models import User
from django.utils import timezone

GENDER_CHOICES = (('Male','Male'), ('Female','Female'), ('Others','Others'))


class Tutor(models.Model):
    T_user = models.OneToOneField(User, verbose_name='related to')
    first_name = models.CharField(max_length=20,null=False,blank=False)
    last_name = models.CharField(max_length=20,null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    joining_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'


class TutorInfo(models.Model):
    T_link = models.OneToOneField(Tutor, verbose_name='of Tutor user')
    prof_pic = models.ImageField(upload_to='profile_pic', null=True,blank=True)
    full_name = models.TextField(max_length=30,blank=False,null=False)
    exp = models.PositiveSmallIntegerField(blank=False,null=False)
    age = models.PositiveSmallIntegerField(blank=False,null=False)
    courses = models.TextField(max_length=500,blank=False,null=False)

    def __str__(self):
        return self.full_name



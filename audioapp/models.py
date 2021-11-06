from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class program(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    Duration = models.DateTimeField(blank=True)
    interview_status =models.BooleanField(default=False)
    def __str__(self):
        return "%s " % (self.name)
class subprogram(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(program, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default='0')
    subprogram_status = models.BooleanField(default=False)
    p_status = models.BooleanField(default=False)
    def __str__(self):
        return "%s %s" % (self.program,self.name)
class audio(models.Model):
    id = models.AutoField(primary_key=True)
    subprogram = models.ForeignKey(subprogram, on_delete=models.CASCADE)
    audioname = models.CharField(max_length=200)
    artistname =  models.CharField(max_length=200 , null=True)
    image = models.FileField(upload_to ='images/',null=True)
    audiofile = models.FileField(upload_to ='audio/',null=True)
    audio = models.BooleanField(default=False)
    def __str__(self):
        return "%s %s" % (self.subprogram,self.audioname)
class coupon(models.Model):
      id = models.AutoField(primary_key=True)
      code = models.CharField(max_length=200)
      price = models.CharField(max_length=200)
      timeDuration = models.DateTimeField(blank=True)
      def __str__(self):
        return "%s" % (self.code)
class OrderDetail(models.Model):
      id = models.AutoField(primary_key=True)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      price = models.CharField(max_length=200)
      ProgramID = models.IntegerField(blank=True)
      def __str__(self):
        return "%s" % (self.user)

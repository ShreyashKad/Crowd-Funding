from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    department=models.CharField(max_length=40)
    contact=models.CharField(max_length=40)
    gender=models.CharField(max_length=40)
    github=models.CharField(max_length=100)
    linkedin=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    pic_path=models.FileField(null=True,blank=True)


    def __str__(self):
        return self.name

class Project(models.Model):
    p_name=models.CharField(max_length=40)
    p_description=models.CharField(max_length=40)
    p_github=models.CharField(max_length=100)
    p_recommendation_pic_path=models.FileField(null=True,blank=True)
    p_domain=models.CharField(max_length=100)
    p_efund=models.CharField(max_length=100)
    p_afund=models.CharField(max_length=100,default='0')
    p_startdate=models.CharField(max_length=100)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.p_name

class DetailFunding(models.Model):
    detail = models.TextField(default="Not Mentioned")
    student = models.OneToOneField(Student, on_delete = models.CASCADE, default=None)

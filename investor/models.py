from django.db import models
from django.utils.timezone import now
from student.models import Project

# Create your models here.
class Investor(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    contact = models.FloatField()
    gender = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    company = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    pic_path = models.FileField(null=True,blank=True)

    def _str_(self):
        return self.email

class Funding(models.Model):
    date_of_funding = models.DateField(default=now, editable=False )
    amount = models.CharField(max_length=40)
    project=models.ForeignKey(Project,on_delete=models.CASCADE,default=None)
    investor=models.ForeignKey(Investor,on_delete=models.CASCADE,default=None)

from django.db import models
from musiacians.models import musician_model
from django.utils import timezone
# Create your models here.
CHOICES = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]
class album_model(models.Model):
    album_name = models.CharField(max_length = 100)
    release_date = models.DateField(default = timezone.now)
    musician = models.ForeignKey(musician_model,on_delete = models.CASCADE)
    rating = models.CharField(max_length=1 ,choices=CHOICES,default='1')
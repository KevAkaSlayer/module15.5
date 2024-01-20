from django.db import models

# Create your models here.

class musician_model(models.Model):
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length = 12)
    InstrumentType = models.CharField(max_length = 20)


    def __str__(self):
        return self.FirstName
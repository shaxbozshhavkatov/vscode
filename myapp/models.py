from django.db import models

# Create your models here.


class PhoneModel(models.Model):
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    
    
    
class InfoModell(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    name1 = models.ForeignKey(PhoneModel,on_delete = models.CASCADE)
    
    def __str__(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        return self.color
from django.db import models

class Car(models.Model):

    brand_name = models.CharField(max_length=50, blank=True)
    car_model = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, default='-')
    release_year = models.CharField('Since year', max_length=50, blank=True)
    last_year = models.CharField('Until year',max_length=50, blank=True, )
    
    def __str__(self):
        return self.name



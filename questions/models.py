from django.db import models
from django.utils import timezone

SORT_CHOICES = ( 
    ("activity", "activity"),
    ("creation", "creation"), 
    )

ORDER_CHOICES = ( 
    ("desc", "desc"), 
    ("asc", "asc"), 
    )
class Data(models.Model):
        page = models.IntegerField(default = None, null = True,blank=True)
        pagesize= models.IntegerField(default = None, null = True,blank=True)
        fromdate= models.DateField(default = None, null = True,blank=True)
        todate= models.DateField(default = None, null = True,blank=True)
        order= models.CharField(max_length= 30,choices=ORDER_CHOICES,default = None, null = True,blank=True)
        min= models.DateField(default = None, null = True,blank=True)
        max= models.DateField(default = None, null = True,blank=True)
        sort= models.CharField(max_length= 30,choices=SORT_CHOICES, default = None, null = True,blank=True)
        q= models.CharField(max_length=1000,default = None, null = True,blank=True)
        site= "stackoverflow"

        def __str__(self):
            return self.site

from django.db import models

class Location(models.Model):
    ip=models.CharField(max_length=25)
    ip_type=models.CharField(max_length=100,blank=True,null=True)
    continent_code=models.CharField(max_length=100,blank=True,null=True)
    continent_name=models.CharField(max_length=100,blank=True,null=True)
    country_code=models.CharField(max_length=100,blank=True,null=True)
    country_name=models.CharField(max_length=100,blank=True,null=True)
    region_code=models.CharField(max_length=20,blank=True,null=True)
    region_name=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
    zip_code=models.CharField(max_length=30,blank=True,null=True)
    latitude=models.CharField(max_length=100,blank=True,null=True)
    longitude=models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.city
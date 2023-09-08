from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    title= models.CharField(max_length=100)
    img =models.TextField(blank=True)
    info=models.TextField()

    class Meta:
        verbose_name_plural="Animals Species"

   

class Animals(models.Model):
    title= models.CharField(max_length=100)
    img =models.TextField()
    category=models.CharField(max_length=100)
    info=models.TextField(blank=True)
    video1=models.TextField(blank=True)
    video2=models.TextField(blank=True)
    slug =models.SlugField(default='',null=True,blank=True)

    def absolute_url(self):
        return reverse("animal_detail",args=[self.slug])
    
    class Meta:
        verbose_name_plural="Animals Entries"

from django.db import models

from django.utils import timezone
from django.urls import reverse





# Create your models here.


class Property(models.Model):
    title=models.CharField(max_length=250)
    published_date=models.DateTimeField(blank=True,null=True)
    created_date=models.DateTimeField(default=timezone.now)
    location=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    picture=models.ImageField(upload_to='prop_pix/', height_field=None, width_field=None,max_length=500)
    price=models.CharField(max_length=50)
    description=models.TextField()
    rooms=models.IntegerField()
    agent=models.ForeignKey('Agent',related_name='Aname', on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return self.title

    # def saveimage(self):
    #     pass

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def get_absolute_url(self): # to return the webpage to list of posts after commenting
        return reverse("property_detail",kwargs={'pk':self.pk})
    

class Agent(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    contact=models.CharField(max_length=15)
    email=models.EmailField()
    pix=models.ImageField(upload_to='agent_pix/', height_field=None, width_field=None,max_length=500)
    

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    # def get_absolute_url(self): # to return the webpage to list of posts after commenting
    #     return reverse("agent_detail",kwargs={'pk':self.pk})
    
    def get_absolute_url(self): # to return the webpage to list of posts after commenting
        return reverse("agent_detail",kwargs={'pk':self.pk})
    


class Leads(models.Model):
    firstname=models.CharField(max_length=50,null=False, blank=False)
    lastname=models.CharField(max_length=50,null=False, blank=False)
    email=models.EmailField(null=False, blank=False)
    message=models.TextField(null=False, blank=False)
    property=models.ForeignKey('Property', related_name='leadsppt', on_delete=models.CASCADE) 

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    def get_absolute_url(self): # to return the webpage to list of posts after commenting
        return reverse("property_detail",kwargs={'pk':self.pk})
    


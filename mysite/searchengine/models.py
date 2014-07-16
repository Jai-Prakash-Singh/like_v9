# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

from django.db import models

class sites_table(models.Model):
    dimainname = models.CharField(max_length=50)
    dimainlink = models.URLField()
    #image = models.ImageField(upload_to = "assets/images/")
    #image = models.ImageField(upload_to = "static/image_uploaded_dir")
    image = models.ImageField(upload_to = "image_uploaded_dir")
    imagelink = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=60)
    added_date = models.DateField()

    def __unicode__(self):
        return self.dimainname

    class Meta:
        ordering = ['dimainname']

import datetime

class ip_country(models.Model):
    ipfield = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    keyword = models.CharField(max_length=100, null=True)
    #added_date = models.DateTimeField(auto_now_add=True, blank=True)
    added_date = models.DateTimeField(default= datetime.datetime.now, blank=True)
    #added_date = models.DateTimeField('date created', default = time.strftime("%c"))



class Document(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "image_uploaded_dir")
    imagelink = models.URLField(blank=True, null=True)
    
    #docfile = models.FileField(upload_to='documents/%Y%m%d')
    urllink =  models.URLField()
    status = models.CharField(max_length=60)
    added_date = models.DateField()

    def __unicode__(self):
        return str(self.title)

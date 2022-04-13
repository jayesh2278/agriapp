from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)
    category = models.ForeignKey(category,on_delete=models.CASCADE,related_name="postcategory")
    image1 = models.ImageField(upload_to = '')
    image2 = models.ImageField(upload_to='',blank = True)
    image3 = models.ImageField(upload_to='',blank = True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) -> str:
        return self.title

class adress (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    taluko = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    pincode = models.IntegerField()

    def __str__(self) -> str:
        return str(self.user)


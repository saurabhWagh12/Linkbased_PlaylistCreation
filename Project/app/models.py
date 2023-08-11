from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserOfPlayList(models.Model):
    username = models.CharField(max_length=200)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=False,blank=False)
    
    def __str__(self):
        return self.username


class MyPlaylist(models.Model):
    user = models.ForeignKey(UserOfPlayList,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=300)
    favourite = models.BooleanField(default=False)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Video(models.Model):
    belongTo = models.ForeignKey(MyPlaylist,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name

    

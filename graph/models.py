from django.db.models import Model
from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=40,unique=True,null=True)
    user_name = models.CharField(max_length=40,null=True)
    user_email = models.EmailField()
    user_city = models.CharField(max_length=40)
    videos_watched = models.ManyToManyField('VideoData', through='WatchedVideo')
    class Meta:
        ordering = ['user_id']
        verbose_name = 'User MetaData'
        verbose_name_plural = 'Users MetaData'
    def __unicode__(self):
        return self.user_id

class VideoData(models.Model):
    video_id = models.CharField(max_length=40,unique=True, null=True)
    video_name = models.CharField(max_length=40) 
    class Meta:
        verbose_name = 'User_Video MetaData'
        verbose_name_plural = 'Users_Video MetaData'
    def __unicode__(self):
        return self.video_name     

class WatchedVideo(models.Model):
    user = models.ForeignKey(User, to_field = 'user_id')
    videoData = models.ForeignKey(VideoData, to_field = 'video_id')
    time  = models.PositiveIntegerField(null = True)
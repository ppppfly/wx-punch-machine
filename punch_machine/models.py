from django.db import models


class WechatUser(models.Model):
    avatarUrl = models.TextField()
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    gender = models.IntegerField()
    language = models.CharField(max_length=20)
    nickName = models.CharField(max_length=100)
    province = models.CharField(max_length=20)

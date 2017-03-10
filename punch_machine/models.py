from django.db import models


class WechatUser(models.Model):
    openid = models.CharField(max_length=50, primary_key=True)
    avatarUrl = models.TextField()
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    gender = models.IntegerField()
    language = models.CharField(max_length=20)
    nickName = models.CharField(max_length=100)
    province = models.CharField(max_length=20)

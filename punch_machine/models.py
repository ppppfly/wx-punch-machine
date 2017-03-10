from django.db import models


class WechatUser(models.Model):
    openid = models.CharField(max_length=50, primary_key=True)
    avatarUrl = models.TextField()
    city = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=20, null=True, blank=True)
    nickName = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=20, null=True, blank=True)

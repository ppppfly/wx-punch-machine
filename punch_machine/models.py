from django.db import models


class TimeMannerModel(models.Model):
    class Meta:
        abstract = True
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class WechatUser(TimeMannerModel):
    openid = models.CharField(max_length=50, primary_key=True)
    avatarUrl = models.TextField()
    city = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=20, null=True, blank=True)
    nickName = models.CharField(max_length=100)
    province = models.CharField(max_length=20, null=True, blank=True)


class Group(TimeMannerModel):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(WechatUser, related_name='groups')


class Permission(TimeMannerModel):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)


class Role(TimeMannerModel):
    name = models.CharField(max_length=10)
    group = models.ForeignKey(Group)
    permissions = models.ManyToManyField(Permission, related_name='roles')


class Membership(TimeMannerModel):
    group = models.ForeignKey(Group)
    WechatUser = models.ForeignKey(WechatUser)
    role = models.ForeignKey(Role)

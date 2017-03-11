from rest_framework import serializers
from punch_machine import models


class WechatUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.WechatUser
        fields = ('openid', 'avatarUrl', 'city', 'country',
                  'gender', 'language', 'nickName', 'province')

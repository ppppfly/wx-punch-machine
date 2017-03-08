from rest_framework import serializers
from punch_machine import models


class WechatUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.WechatUser
        fields = ('id', 'avatarUrl', 'city', 'country', 'gender', 'language',
                  'nickName', 'province')

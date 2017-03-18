# coding=utf-8
from rest_framework import serializers
from punch_machine import models


class WechatUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.WechatUser
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Group
        fields = '__all__'
        depth = 2


class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = ('name', 'openid')

    openid = serializers.ReadOnlyField()

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


class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = ('name', 'openid')

    openid = serializers.CharField()

    def create(self, validated_data):

        # todo: 绑定当前openid和group,并创建组长角色

        super(GroupCreateSerializer, self).create(validated_data)

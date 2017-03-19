# coding=utf-8
from rest_framework import serializers
from punch_machine import models


class WechatUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.WechatUser
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Role
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Membership
        fields = ('group', 'role', 'user')

    group = serializers.CharField(source='group.name')
    role = RoleSerializer()
    user = WechatUserSerializer()


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


class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = ('id', 'name', 'leader_name', 'leader_uri')

    leader_name = serializers.SerializerMethodField()
    leader_uri = serializers.SerializerMethodField()

    def get_leader_name(self, obj):
        if hasattr(obj, 'members'):
            print obj.members.all()
            return obj.members.filter(role__level=100).first().user.nickName

    def get_leader_uri(self, obj):
        if hasattr(obj, 'members'):
            return obj.members.filter(role__level=100).first().user.avatarUrl


class GroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = ('id', 'name', 'members')

    members = MemberSerializer(many=True)

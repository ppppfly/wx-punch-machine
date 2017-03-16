# coding=utf-8
from django.http import HttpResponse
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from punch_machine import models
from punch_machine import serializers


class WechatUserViewSet(viewsets.GenericViewSet,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin):
    queryset = models.WechatUser.objects.all()
    serializer_class = serializers.WechatUserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer

    def get_serializer_class(self):

        if self.request.method in ['POST']:
            self.serializer_class = serializers.GroupCreateSerializer

        else:
            self.serializer_class = serializers.GroupSerializer

        return self.serializer_class

    def perform_create(self, serializer):

        openid = self.request.data.get('openid')
        group_name = self.request.data.get('name')

        if openid:
            resp = super(GroupViewSet, self).perform_create(serializer)
            wx_user = get_object_or_404(models.WechatUser, openid=openid)
            group = get_object_or_404(models.Group, name=group_name)
            role, created = models.Role.objects.get_or_create(name='组长', group=group)
            models.Membership.objects.create(group=group, user=wx_user, role=role)
        else:
            resp = HttpResponse()

        return resp


@api_view(['GET'])
def check_group_name(request):
    group_name = request.GET.get('group_name')
    query_set = models.Group.objects.filter(name=group_name)
    if query_set.exists():
        return Response({
            'errMsg': u'该小组名已经存在'
        }, status=status.HTTP_404_NOT_FOUND)
    return Response()

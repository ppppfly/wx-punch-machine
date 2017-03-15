# coding=utf-8
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
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


@api_view(['GET'])
def check_group_name(request):
    print request.GET
    group_name = request.GET.get('group_name')
    query_set = models.Group.objects.filter(name=group_name)
    if query_set.exists():
        return Response({
            'errMsg': u'该小组名已经存在'
        }, status=status.HTTP_404_NOT_FOUND)
    return Response()

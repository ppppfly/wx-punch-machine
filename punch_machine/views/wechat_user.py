from rest_framework import viewsets
from punch_machine import models
from punch_machine import serializers


class WechatUserViewSet(viewsets.ModelViewSet):
    queryset = models.WechatUser.objects.all()
    serializer_class = serializers.WechatUserSerializer

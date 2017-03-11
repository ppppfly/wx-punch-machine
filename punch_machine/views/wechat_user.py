from rest_framework import viewsets, mixins
from punch_machine import models
from punch_machine import serializers


class WechatUserViewSet(viewsets.GenericViewSet,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin):
    queryset = models.WechatUser.objects.all()
    serializer_class = serializers.WechatUserSerializer

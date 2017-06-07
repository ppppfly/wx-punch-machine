# coding=utf-8
from django.db import models


class Person(models.Model):

    # 1、基础信息（必填）
    name = models.CharField(max_length=10)
    birthday = models.DateField()
    gender = models.IntegerField(choices=((1, u'男'), (2, u'女')))
    city = models.CharField(max_length=5)
    occupation = models.CharField(max_length=20)
    avatar = models.ImageField()

    # 2、学历（选填）
    school = models.CharField(max_length=20, null=True, blank=True)
    major = models.CharField(max_length=20, null=True, blank=True)
    degree = models.IntegerField(
        choices=((1, u'初中'), (2, u'高中'), (3, u'本科'), (4, u'硕士'), (5, u'博士')),
        null=True, blank=True
    )

    # 3、爱好（必填）
    speciality = models.TextField()
    interest = models.TextField()

    # 4、标签（选填）
    tag_1 = models.CharField(max_length=20, null=True, blank=True)
    tag_2 = models.CharField(max_length=20, null=True, blank=True)
    tag_3 = models.CharField(max_length=20, null=True, blank=True)

    # 5、如何遇见漫步人生
    referrer = models.CharField(verbose_name=u'推荐人', max_length=10)
    channel = models.CharField(verbose_name=u'渠道', max_length=20)
    chance = models.CharField(verbose_name=u'机会', max_length=20)

    # 6、阅历
    experience = models.TextField(verbose_name=u'成长阅历')

    # 7、其他
    other = models.TextField(verbose_name=u'其他')


class Portfolio(models.Model):

    person = models.OneToOneField(Person)
    graduation_thesis = models.TextField(u'毕业论文')

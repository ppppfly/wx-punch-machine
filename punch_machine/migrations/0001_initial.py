# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WechatUser',
            fields=[
                ('openid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('avatarUrl', models.TextField()),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.IntegerField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=20, null=True)),
                ('nickName', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]

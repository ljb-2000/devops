#!/usr/bin/env python
# -*- coding: utf-*-
from django.db import models
from account.models import User, Key


class Group(models.Model):
    name = models.CharField('组名', null=False, blank=False, max_length=50)
    desc = models.CharField('描述', null=True, blank=True, max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '主机组'
        verbose_name_plural = verbose_name


class IDC(models.Model):
    name = models.CharField('名称', null=False, blank=False, max_length=50)
    contact = models.CharField('联系人', null=True, blank=True, max_length=50)
    tel = models.CharField('联系电话', null=True, blank=True, max_length=13)
    email = models.EmailField('联系邮箱', null=True, blank=True, max_length=255)
    desc = models.CharField('描述', null=True, blank=True, max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '机房'
        verbose_name_plural = verbose_name


class Host(models.Model):
    LOGIN_TYPE = (
        ('password', '密码'),
        ('key', '密钥')
    )
    hostname = models.CharField('主机名', null=False, blank=False, max_length=100, unique=True)
    ipaddr = models.IPAddressField('IP地址', null=False, blank=False, max_length=15)
    username = models.CharField('账号', null=False, blank=False, max_length=20, default='root')
    login_type = models.CharField('认证方式', null=False, blank=False, max_length=10, default='key', choices=LOGIN_TYPE)
    password = models.CharField('密码', null=True, blank=True, max_length=50)
    private_key = models.ForeignKey(Key, verbose_name='密钥', blank=True, null=True)
    port = models.CharField('端口', null=False, blank=False, max_length=10, default='22')
    idc = models.ForeignKey(IDC, verbose_name='机房')
    groups = models.ManyToManyField(Group, verbose_name='组', related_name='hosts')
    users = models.ManyToManyField(User, verbose_name='管理人')

    def __unicode__(self):
        return self.hostname

    class Meta:
        verbose_name = '主机'
        verbose_name_plural = verbose_name

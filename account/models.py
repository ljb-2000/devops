#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from hashlib import md5
import os.path
import time


class UserManager(BaseUserManager):
    def _create_user(self, username, password, realname, email, sex, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('必须提供账号')
        email = self.normalize_email(email)
        user = self.model(username=username, realname=realname, sex=sex, email=email, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.joined_at = now
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password, realname, email, sex, **extra_fields):
        return self._create_user(username, password, realname, email, sex, False, False)

    def create_superuser(self, username, password, realname, email, sex, **extra_fields):
        return self._create_user(username, password, realname, email, sex, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    SEX = (
        ('male', '男'),
        ('female', '女')
    )
    username = models.CharField('用户名', blank=False, null=False, max_length=50, unique=True)
    realname = models.CharField('姓名', blank=True, null=True, max_length=50)
    email = models.EmailField('电子邮箱', blank=False, null=False, max_length=255)
    joined_at = models.DateTimeField('加入时间', default=timezone.now)
    sex = models.CharField('性别', blank=False, null=False, max_length='10', default='male', choices=SEX)
    is_staff = models.BooleanField('是否可登陆后台', default=False)
    is_active = models.BooleanField('是否可用', default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['realname', 'email', 'sex']

    objects = UserManager()

    def get_headimg(self):
        return 'http://www.gravatar.com/avatar/%s' % md5(self.email if self.email else 'daixijun1990@gmail.com').hexdigest()

    def get_full_name(self):
        return self.realname

    def get_short_name(self):
        return self.realname

    def __unicode__(self):
        return self.realname if self.realname else self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


def get_key_path(instance, filename):
    t = time.localtime()
    return "%(user)s/keys/%(year)d/%(mon)d/%(day)d/%(filename)s" % {'user': str(instance.user.username), 'year': t.tm_year, 'mon': t.tm_mon, 'day': t.tm_mday, 'filename': filename}


class Key(models.Model):
    name = models.CharField('名称', blank=False, null=False, max_length=50)
    user = models.ForeignKey(User, verbose_name='用户')
    key = models.FileField('密钥', upload_to=get_key_path)
    desc = models.CharField('描述', blank=True, null=True, max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '密钥'
        verbose_name_plural = verbose_name

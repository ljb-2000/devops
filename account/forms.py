#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from .models import User
from xadmin.widgets import AdminRadioSelect

class UserCreateForm(forms.ModelForm):
    error_messages = {
        'duplicate_username': '用户已经被注册',
        'password_mismatch': '两次输入的密码不一致',
    }
    username = forms.RegexField(label='用户名', max_length=50, regex=r'^[\w.@+-]+$', 
            help_text='必填,最多50个字符,只能包含 字母,数字和 @/./+/-/_  特殊符号',
            error_message = {
                'invalid': '用户名必须是 字母,数字和 @/./+/-/_ 的组合'
            })
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput)
    realname = forms.CharField(label='姓名', max_length=50, required=False)
    sex = forms.ChoiceField(label='性别', choices=User.SEX, widget=AdminRadioSelect(attrs={'inline': 'inline'}), initial='male')
    email = forms.CharField(label='电子邮箱', max_length=50, # widget=forms.EmailInput,
            help_text='电子邮箱格式： user@example.com'
            )

    class Meta:
        model = User
        fields = ('username', 'realname', 'sex', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        # fields = '__all__'

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'], code='duplicate_username')

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(self.error_messages['password_mismatch'], code='password_mismatch')
        return password2

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xadmin
from .models import User, Key
from .forms import UserCreateForm
from devops.settings import APPS_LABEL_TITLE
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.forms import UserChangeForm
from xadmin.layout import Fieldset, Main, Side#, Row#, FormHelper
from xadmin.plugins.auth import PermissionModelMultipleChoiceField
xadmin.site.unregister(User)
# xadmin.site.unregister(Group)
# xadmin.site.unregister(Permission)
from xadmin.views import BaseAdminView, CommAdminView

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(BaseAdminView, BaseSetting)


class GlobalSetting(object):
    # global_search_models = [Host, IDC]
    # global_models_icon = {
    #        Host: 'fa fa-laptop', IDC: 'fa fa-cloud'
    #        }
    menu_style = 'accordion'#'accordion'
    site_title = '运维'
    site_footer = 'verystar.cn 2014'
    apps_label_title = APPS_LABEL_TITLE

    def get_site_menu(self):
        return (
            {'title': '用户管理', 'icon': 'fa fa-user', 'perm': self.get_model_perm(User, 'change'), 'menus': (
                {'title': '用户', 'icon': 'fa fa-user', 'url': self.get_model_url(User, 'changelist')},
                {'title': '组', 'icon': 'fa fa-group', 'url': self.get_model_url(Group, 'changelist')},
                {'title': '权限', 'icon': 'fa fa-lock', 'url': self.get_model_url(Permission, 'changelist')},
                {'title': '密钥', 'icon': 'fa fa-key', 'url': self.get_model_url(Key, 'changelist')},
            )},
        )
xadmin.site.register(CommAdminView, GlobalSetting)


class UserAdmin(object):
    list_display = ('username', 'realname', 'email', 'sex', 'joined_at', 'is_active', 'is_staff', 'is_superuser')
    relfield_style = 'fk-ajax'
    readonly_fields = ('joined_at', 'last_login')
    style_fields = {'user_permissions': 'm2m_transfer', 'groups': 'checkbox-inline', 'sex': 'radio-inline'}
    change_user_password_template = None
    model_icon = 'fa fa-user'
    reversion_enable = True

    def get_model_form(self, **kwargs):
        if self.org_obj is None:
            self.form = UserCreateForm
        else:
            self.form = UserChangeForm
        return super(UserAdmin, self).get_model_form(**kwargs)

    def get_field_attrs(self, db_field, **kwargs):
        attrs = super(UserAdmin, self).get_field_attrs(db_field, **kwargs)
        if db_field.name == 'user_permissions':
            attrs['form_class'] = PermissionModelMultipleChoiceField
        return attrs

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('用户信息',
                             'username',
                             'password',
                             'email', 'sex', 'realname',
                             #css_class='unsort no_title'
                             ),
                    Fieldset('权限和组',
                             'groups', 'user_permissions',
                             ),
                ),
                Side(
                    Fieldset('用户状态',
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                    Fieldset('时间',
                            'joined_at', 'last_login'
                            )
                )
            )
        else:
            self.form_layout = (
                Main(
                    Fieldset('用户信息',
                             'username', 'password1', 'password2',
                             'email', 'sex', 'realname',
                             #css_class='unsort no_title'
                             ),
                    Fieldset('权限和组',
                             'groups', 'user_permissions',
                             ),
                ),
                Side(
                    Fieldset('用户状态',
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                    Fieldset('时间',
                            'joined_at', 'last_login'
                            )
                )
            )
        return super(UserAdmin, self).get_form_layout()
xadmin.site.register(User, UserAdmin)


# class GroupAdmin(object):
#     list_display = ('name', 'group_permissions')
# xadmin.site.register(Group, GroupAdmin)

# class PermissionAdmin(object):
#     list_display = ('name', 'codename')
# xadmin.site.register(Permission, PermissionAdmin)


class KeyAdmin(object):
    list_display = ('name', 'key', 'desc')
    exclude = ('user', )

    def save_models(self):
        self.new_obj.user = self.request.user
        self.new_obj.save()
xadmin.site.register(Key, KeyAdmin)

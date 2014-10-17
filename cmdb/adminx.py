#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xadmin
from cmdb.models import Host, Group, IDC


class HostAdmin(object):
    list_display = ('hostname', 'ipaddr', 'login_type', 'username', 'groups', 'users', 'idc')
    reversion_enable = True
    model_icon = 'fa fa-laptop'
    style_fields = {'users': 'checkbox-inline', 'groups': 'checkbox-inline'}
    list_per_page = 20
    search_fields = ('groups', 'hostname', 'users')

    def get_media(self):
        media = super(HostAdmin, self).get_media()
        # media = media + self.form_obj.media
        media.add_js([self.static('custom/js/xadmin.cmdb.host.js')])
        return media

    def get_list_queryset(self):
        qs = super(HostAdmin, self).get_list_queryset()
        if self.request.user.is_superuser:
            return qs
        return qs.filter(users=self.request.user)
xadmin.site.register(Host, HostAdmin)


class GroupAdmin(object):
    list_display = ('name', 'desc')
    reversion_enable = True
    model_icon = 'fa  fa-bars'
xadmin.site.register(Group, GroupAdmin)


class IDCAdmin(object):
    list_display = ('name', 'contact', 'tel', 'email', 'desc')
    reversion_enable = True
    model_icon = 'fa fa-cloud'
xadmin.site.register(IDC, IDCAdmin)

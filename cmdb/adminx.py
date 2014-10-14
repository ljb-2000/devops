#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xadmin
from cmdb.models import Host, Group, IDC


class HostAdmin(object):
    list_display = ('hostname', 'ipaddr', 'login_type', 'login_type', 'username')
    reversion_enable = True
    model_icon = 'fa fa-laptop'
    style_fields = {'users': 'checkbox-inline'}

    def get_media(self):
        media = super(HostAdmin, self).get_media()
        # media = media + self.form_obj.media
        media.add_js([self.static('custom/js/xadmin.cmdb.host.js')])
        return media
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

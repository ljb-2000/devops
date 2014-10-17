#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from cmdb.models import Host, Group


class HostSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.RelatedField(many=True)
    groups = serializers.RelatedField(many=True)
    private_key = serializers.SerializerMethodField('get_key_url')
    idc = serializers.RelatedField()

    def get_key_url(self, obj):
        return obj.private_key.key.path if obj.login_type=='key' else None

    class Meta:
        model = Host
        lookup_field = 'hostname'
        fields = ('id', 'hostname', 'ipaddr', 'username', 'login_type', 'password', 'private_key', 'port', 'users', 'groups', 'idc', 'url')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    hosts = serializers.RelatedField(many=True)

    class Meta:
        model = Group
        lookup_field = 'name'
        fields = ['id', 'name', 'url', 'hosts']

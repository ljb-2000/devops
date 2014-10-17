#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework import permissions
from rest_framework import status
from django.http import Http404
from cmdb.models import Host, Group
from cmdb.serializers import HostSerializer, GroupSerializer


# class HostListView(generics.ListCreateAPIView):
    # queryset = Host.objects.all()
    # serializer_class = HostSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # # paginate_by = 3


# class HostDetailView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Host.objects.all()
    # serializer_class = HostSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# class GroupListView(generics.ListCreateAPIView):
    # queryset = Group.objects.all()
    # serializer_class = GroupSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Group.objects.all()
    # serializer_class = GroupSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class HostViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    queryset = Host.objects.all()
    lookup_field = 'hostname'
    lookup_value_regex = '[^/]+'
    serializer_class = HostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class GroupViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put', 'delete']
    queryset = Group.objects.all()
    lookup_field = 'name'
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class HostListView(APIView):
    # """ List all Hosts, or create a new Host"""
    # def get(self, request, format=None):
        # hosts = Host.objects.all()
        # serializer = HostSerializer(hosts, many=True)
        # return Response(serializer.data)

    # def post(self, request, format=None):
        # serializer = HostSerializer(data=request.DATA)
        # if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class HostDetailView(APIView):
    # """ Retrieve, update or delete a Host instance"""
    # def get_object(self, pk):
        # try:
            # return Host.objects.get(pk=pk)
        # except Host.DoesNotExist:
            # raise Http404

    # def get(self, request, pk, format=None):
        # host = self.get_object(pk)
        # serializer = HostSerializer(host)
        # return Response(serializer.data)

    # def put(self, request, pk, format=None):
        # host = self.get_object(pk)
        # serializer = HostSerializer(host, data=request.DATA)
        # if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
        # host = self.get_object(pk)
        # host.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def host_list(request):
    # if request.method == 'GET':
        # hosts = Host.objects.all()
        # serializer = HostSerializer(hosts, many=True)
        # return Response(serializer.data)

    # elif request.method == 'POST':
        # serializer = HostSerializer(data=request.DATA)
        # if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def host_detail(request, pk):
    # try:
        # host = Host.objects.get(pk=pk)
    # except Host.DoesNotExist:
        # return Response(status=status.HTTP_404_NOT_FOUND)

    # if request.method == 'GET':
        # serializer = HostSerializer(host)
        # return Response(serializer.data)

    # elif request.method == 'PUT':
        # serializer = HostSerializer(host, data=request.DATA)
        # if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
        # host.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)

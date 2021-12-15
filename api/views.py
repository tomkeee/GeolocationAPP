import re
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .utils import *
from .serializers import LocationSerializer,UserSerializerWithToken
from .models import Location

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ArticleAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            data=Location.objects.all()
        except:
            error_message={"error":"internal problem has occured during retrieving the data"}
            return Response(error_message, status=status.HTTP_404_NOT_FOUND)

        serializer=LocationSerializer(data,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        try:
            data=Location.objects.get(id=pk)
        except Location.DoesNotExist:
            error_message = {'error': 'data with such id does not exist'}
            return Response(error_message, status=status.HTTP_404_NOT_FOUND)

        serializer=LocationSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            location_data=Location.objects.get(id=pk)
        except Location.DoesNotExist:
            error_message = {'error': 'data with such id does not exist'}
            return Response(error_message, status=status.HTTP_404_NOT_FOUND)

        serializer=LocationSerializer(location_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            location_data=Location.objects.get(id=pk)
        except Location.DoesNotExist:
            error_message = {'error': 'data with such id does not exist'}
            return Response(error_message, status=status.HTTP_404_NOT_FOUND)

        location_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

import time
class RegisterUser(APIView):
    def post(self, request):
        serializer=UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class AddClientIPAddress(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            ip=get_client_ip(request)
            location_object=save_client_data(ip)
            serializer=LocationSerializer(location_object,many=False)
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response({"error":"There was a problem finding you geolocation data"},status=status.HTTP_400_BAD_REQUEST)


class AddByUrl(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,pk):
        try:
            location_object=save_client_data(pk)
            serializer=LocationSerializer(location_object,many=False)
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        except:
            return Response({"error":"There was a problem finding you geolocation data"},status=status.HTTP_400_BAD_REQUEST)
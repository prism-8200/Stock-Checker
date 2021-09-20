from django.http import response
from django.shortcuts import render
import json
import redis
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from RestAPI.DownloadZip import download_Parse
import time


redisInstance =redis.Redis(host='127.0.0.1',port=6375,decode_responses=True)



@api_view(['GET'])
def fetchAllMethod(request, *args, **kwargs):
    if request.method == 'GET':
        bef_time = time.ctime(time.time())
        items = []
        count = 0
        print("inside view")
        # download_Parse()
        # print(redisInstance.keys("*"))
        # print(type(redisInstance.keys("*")))
        for key in redisInstance.keys("*"):
            items.append(redisInstance.hgetall(key))
            # print(redisInstance.hgetall(key))
            count += 1
        # response = {
        #     'count': count,
        #     'msg': f"Found {count} items.",
        #     'items': items
        # }
        response=items
        aft_time=time.ctime(time.time())
        print(bef_time," :  ",aft_time)  
        return Response(response, status=200,content_type='application/json')

@api_view(['GET'])
def searchMethod(request, *args, **kwargs):
   if request.method == 'GET':
        if kwargs['searchString'] :
            bef_time = time.ctime(time.time())
            key =(str(kwargs['searchString'])).upper()
            key+='*'
            items = []
            count = 0
            print(key)
            value = redisInstance.hgetall(key)
            if len(redisInstance.keys(key))>0:
                for key in redisInstance.keys(key):
                     items.append(redisInstance.hgetall(key))
            # print(redisInstance.hgetall(key))
                     count += 1
                # response = {
                #     'count': count,
                #     'msg': f"Found {count} items.",
                #     'items': items}
                response=items
                aft_time=time.ctime(time.time())
                print(bef_time," :  ",aft_time)  
                return Response(response, status=200,content_type='application/json')
            else:
                response = {
                    'key': kwargs['searchString'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)






# Create your views here.

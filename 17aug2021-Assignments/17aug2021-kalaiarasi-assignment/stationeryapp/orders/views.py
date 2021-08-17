from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from orders.serializers import OrderSerializer
from orders.models import Order
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.

@csrf_exempt
def order_details(request, id):
    try:
        orders=Order.objects.get(id=id)
    except Order.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    
    if(request.method=="GET"):
        order_serializer=OrderSerializer(orders)
        return JsonResponse(order_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        orders.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        order_serialize=OrderSerializer(orders,data=mydict)
        if (order_serialize.is_valid()):
            order_serialize.save()
            return JsonResponse(order_serialize.data,status=status.HTTP_200_OK)
        
@csrf_exempt
def order_list(request):
    if(request.method=="GET"):
        orders=Order.objects.all()
        order_serializer=OrderSerializer(orders,many=True)
        return JsonResponse(order_serializer.data,safe=False)
        
@csrf_exempt
def adddetail(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        order_serialize=OrderSerializer(data=mydict)
        if (order_serialize.is_valid()):
            order_serialize.save()
            return JsonResponse(order_serialize.data,status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
      
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)



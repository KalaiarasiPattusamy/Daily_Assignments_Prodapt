from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from stocks.serializers import StockSerializer
from stocks.models import Stock
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.

@csrf_exempt
def stock_details(request, id):
    try:
        stocks=Stock.objects.get(id=id)
    except Stock.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    
    if(request.method=="GET"):
        stock_serializer=StockSerializer(stocks)
        return JsonResponse(stock_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        stocks.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        stock_serialize=StockSerializer(stocks,data=mydict)
        if (stock_serialize.is_valid()):
            stock_serialize.save()
            return JsonResponse(stock_serialize.data,status=status.HTTP_200_OK)
        
@csrf_exempt
def stock_list(request):
    if(request.method=="GET"):
        stocks=Stock.objects.all()
        stock_serializer=StockSerializer(stocks,many=True)
        return JsonResponse(stock_serializer.data,safe=False)
        
@csrf_exempt
def additem(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        stock_serialize=StockSerializer(data=mydict)
        if (stock_serialize.is_valid()):
            stock_serialize.save()
            return JsonResponse(stock_serialize.data,status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
      
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)



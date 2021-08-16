from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from sellerapp.sellerserial import SellerSerializer
from sellerapp.models import Seller
# Create your views here.

@csrf_exempt
def seller_list(request):
    if(request.method=="GET"):
        sel=Seller.objects.all()
        seller_serializer=SellerSerializer(sel,many=True)
        return JsonResponse(seller_serializer.data,safe=False)
        
@csrf_exempt
def addseller(request):
    if(request.method=="POST"):
        getName=request.POST.get("sellername")
        getid=request.POST.get("sellerid")
        getaddress=request.POST.get("address")
        getmobnum=request.POST.get("mobnum")
        
        dict={"sellername":getName,"sellerid":getid,"address":getaddress,"mobnum":getmobnum}
        seller_serialize=SellerSerializer(data=dict)
        if (seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data)
        
        else:
            return HttpResponse("Error in serialization")
      
    else:
        return HttpResponse("no get method allowed")


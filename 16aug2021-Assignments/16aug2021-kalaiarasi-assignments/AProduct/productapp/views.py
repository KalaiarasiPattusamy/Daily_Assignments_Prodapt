from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from productapp.serializers import ProductSerializer
from productapp.models import Product
# Create your views here.

@csrf_exempt
def product_list(request):
    if(request.method=="GET"):
        products=Product.objects.all()
        product_serializer=ProductSerializer(products,many=True)
        return JsonResponse(product_serializer.data,safe=False)
        
@csrf_exempt
def addproduct(request):
    if(request.method=="POST"):
        getName=request.POST.get("name")
        getcode=request.POST.get("code")
        getdescription=request.POST.get("description")
        getprice=request.POST.get("price")
        
        dict={"name":getName,"code":getcode,"description":getdescription,"price":getprice}
        product_serialize=ProductSerializer(data=dict)
        if (product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data)
        
        else:
            return HttpResponse("Error in serialization")
      
    else:
        return HttpResponse("no get method allowed")


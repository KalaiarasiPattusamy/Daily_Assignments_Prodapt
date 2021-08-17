from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from notes.serializers import NoteSerializer
from notes.models import Note
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.

@csrf_exempt
def note_details(request, title):
    try:
        notes=Note.objects.get(title=title)
    except Note.DoesNotExist:
        return HttpResponse("Invalid title",status=status.HTTP_404_NOT_FOUND)
    
    if(request.method=="GET"):
        note_serializer=NoteSerializer(notes)
        return JsonResponse(note_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        notes.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        note_serialize=NoteSerializer(notes,data=mydict)
        if (note_serialize.is_valid()):
            note_serialize.save()
            return JsonResponse(note_serialize.data,status=status.HTTP_200_OK)
        




@csrf_exempt
def note_list(request):
    if(request.method=="GET"):
        notes=Note.objects.all()
        note_serializer=NoteSerializer(notes,many=True)
        return JsonResponse(note_serializer.data,safe=False)
        
@csrf_exempt
def addnote(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        note_serialize=NoteSerializer(data=mydict)
        if (note_serialize.is_valid()):
            note_serialize.save()
            return JsonResponse(note_serialize.data,status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
      
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)


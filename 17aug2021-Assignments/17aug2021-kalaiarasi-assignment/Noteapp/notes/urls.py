from django.urls import path,include
from . import views


urlpatterns = [
    path('add/',views.addnote,name='addnote'),
    path('viewall/',views.note_list,name='note_list'),
    path('viewnote/<title>',views.note_details,name='note_details'),
]

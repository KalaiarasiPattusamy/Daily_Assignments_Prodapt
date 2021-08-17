from django.urls import path,include
from . import views


urlpatterns = [
    path('add/',views.additem,name='additem'),
    path('viewall/',views.stock_list,name='stock_list'),
    path('viewstock/<id>',views.stock_details,name='stock_details'),
]

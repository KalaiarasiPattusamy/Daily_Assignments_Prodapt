from django.urls import path,include
from . import views


urlpatterns = [
    path('add/',views.adddetail,name='adddetail'),
    path('viewall/',views.order_list,name='order_list'),
    path('vieworder/<id>',views.order_details,name='order_details'),
]

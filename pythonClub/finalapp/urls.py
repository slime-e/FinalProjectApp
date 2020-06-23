from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index2'),
    path('getbreeds/', views.getbreeds, name='breeds'),
    path('getdogs/', views.getdogs, name='dogs'),
    path('dogdetails/<int:id>', views.dogdetails, name='dogdetails'),
    path('newDog/', views.newDog, name='newdog'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
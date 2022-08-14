from django.contrib import admin
from django.urls import path,include
from mehendihome import views

urlpatterns = [
   path('',views.home,name='home.html'),
   path('uploadmehendi',views.uploadmehendi,name='uploadmehendi.html'),
   path('uploadrangoli',views.uploadrangoli,name='uploadrangoli.html'),
   path('mehendigallary',views.mehendigallary,name='mehendigallary.html'),
   path('rangoligallary',views.rangoligallary,name='rangoligallary.html'),
   path('searchmehendi',views.searchmehendi,name='searchmehendi.html'),
   path('searchrangoli',views.searchrangoli,name='searchrangoli.html'),
   path('dadmin',views.dadmin,name='dadmin.html'),
   path('admindashboard',views.admindashboard,name='admindashboard.html'),
   path('logoutuser',views.logoutuser,name='logoutuser'),
   path('deletemehendi',views.deletemehendi,name='deletemehendi.html'),
   path('deleterangoli',views.deleterangoli,name='deleterangoli.html'),
   path('makeappoinment',views.makeappoinment,name='makeappoinment.html'),
   path('viewappoinment',views.viewappoinment,name='viewappoinment.html'),
   

]

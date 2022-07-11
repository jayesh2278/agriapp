from django import views
from django.urls import path

from app.models import adress

from .views import signup, activate,login1 

urlpatterns = [  
    #path('', home, name = 'home'),  
    path('signup/', signup, name = 'firstindex'),  
    path('activate/<slug:uidb64>/<slug:token>/',activate, name='activate'),
    path('',login1,name = 'login1'),
]

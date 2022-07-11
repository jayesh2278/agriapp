from django.urls import path

from django.urls import include, path

from . import views

urlpatterns = [
    path('index',views.addNoteView,name= 'index'),
    path('categaryview',views.categoryview,name = 'all_category'),
    path('catdetail/<int:id>',views.catdetail,name = 'catdetail'),
    path('adressform',views.adrform,name='adrform'),
    path('userallpost/<int:id>',views.userallpost,name = 'userallpost'),
        
]
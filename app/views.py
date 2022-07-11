from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .forms import  PostForm,adressform
from .models import category,Post

@login_required
def addNoteView(request):
    if request.method =="POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            temp=form.save(commit=False)
            temp.user = request.user
            temp.save()
            
            datas = category.objects.all()
            return render(request,'categoryview.html',{'datas':datas})
           
        else:
        
            msg = 'Errors: %s' % form.errors.as_text()
            return HttpResponse(msg, status=400)
        
          
    else:
        form = PostForm()
        return render(request,'index.html',{'form':form})
    

@login_required
def categoryview(request):
    datas = category.objects.all()
    return render(request,'categoryview.html',{'datas':datas})                

@login_required
def catdetail(request,id):
    print(type(id))
    if id==int(5):
        posts = Post.objects.all()
        return render(request,'catdetail.html',{'posts':posts})
    else:
        category1 = category.objects.get(pk=id)
        posts= Post.objects.filter(category_id = category1.id)
        return render(request,'catdetail.html',{'posts':posts}) 
    
@login_required
def adrform(request):
    if request.method=="POST":
        form = adressform(request.POST)
        if form.is_valid():
            tar = form.save(commit=False)
            tar.user = request.user
            tar.save()
    else:
        form = adressform()
        return render(request,'adressform.html',{'form':form})

def userallpost(request,id):
   posts = Post.objects.filter(user = id)
   return render(request,'alluserpost.html',{'posts':posts})

   



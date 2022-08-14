from datetime import datetime
from email.mime import image
from multiprocessing import context
from operator import methodcaller
import os
import re
from xml.etree.ElementTree import tostring
from xmlrpc.client import DateTime
from django.shortcuts import render
from datetime import date, datetime
from django.contrib import messages
from django.contrib import messages

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout


from uuid import uuid4
from mehendihome.models import appoinment, mehendi,rangoli
# Create your views here.


def home(request):
    img1= mehendi.objects.order_by('-id')[0]
    img2= mehendi.objects.order_by('-id')[1]
    img3= mehendi.objects.order_by('-id')[2]
    img4= mehendi.objects.order_by('-id')[3]
    img5= mehendi.objects.order_by('-id')[4]
    imgg1= rangoli.objects.order_by('-id')[0]
    imgg2= rangoli.objects.order_by('-id')[1]
    imgg3= rangoli.objects.order_by('-id')[2]
    imgg4= rangoli.objects.order_by('-id')[3]
    imgg5= rangoli.objects.order_by('-id')[4]
    context = {
        'mg1' : img1.image,
        'mg2' : img2.image,
        'mg3' : img3.image,
        'mg4' : img4.image,
        'mg5' : img5.image,
        'rg1' : imgg1.image,
        'rg2' : imgg2.image,
        'rg3' : imgg3.image,
        'rg4' : imgg4.image,
        'rg5' : imgg5.image
    }
    return render(request,'home.html',context=context)

def uploadmehendi(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method == "POST":
        mehendi_style = request.POST.get('mehstyle')
       
        desc = request.POST.get('desc')
        image =request.FILES['image']
        now = datetime.now()
        timeee = datetime.time(now)
        

      
        
        meh = mehendi(mehendi_style= mehendi_style,mehendi_desc = desc,mehendi_time = timeee ,image = image,mehendi_date=now)
        meh.save()
        messages.add_message(request, messages.INFO, 'Upload Sucessfull')
        
        
   

        


    return render(request,'uploadmehendi.html')
def uploadrangoli(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method == "POST":
        mehendi_style = request.POST.get('mehstyle')
       
        desc = request.POST.get('desc')
        image =request.FILES['image']
        now = datetime.now()
        
       
        meh = rangoli(rangoli_style= mehendi_style,rangoli_desc = desc, image = image,rangoli_date=now)
        meh.save()
        print('sucess')

        


    return render(request,'uploadrangoli.html')


def mehendigallary(request):
    mehim = mehendi.objects.order_by('-id').all()

    return render(request,'mehendigallary.html',{'mehinf':mehim})

def rangoligallary(request):
    mehim = rangoli.objects.order_by('-id').all()
    
   


    

    return render(request,'rangoligallary.html',{'rangoinfo':mehim})

def searchmehendi(request):
    
    if request.method == "POST":
        name = request.POST.get('search')
        mehres = mehendi.objects.filter(mehendi_style = name)
        
        return render(request,'searchmehendi.html',{
            'search' :name,
            'result' : mehres
        })
        
    else:
      return redirect('/')

def searchrangoli(request):
    if request.method == "POST":
        name = request.POST.get('search')
        mehres = rangoli.objects.filter(rangoli_style = name)
        print(mehres)
        
        return render(request,'searchrangoli.html',{
            'search' :name,
            'result' : mehres
        })
        
    else:
      return redirect('/')


def dadmin(request):
    if request.method == "POST":
  
            username = request.POST['aduser']
            password = request.POST['adpass']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/admindashboard")
        # Redirect to a success page.
      
            else:
        # Return an 'invalid login' error message.
                return redirect("/dadmin")
        
    return render(request,'dadmin.html')

def admindashboard(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request,'admindashboard.html')


def logoutuser(request):
    logout(request)
    return redirect("/")


def deletemehendi(request):
    if request.user.is_anonymous:
        return redirect("/")
    mehim = mehendi.objects.order_by('-id').all()

    if request.method == "POST":
        mehid = request.POST.get('mehid')
        sd = mehendi.objects.get(id=mehid)
        sd.delete()
        os.remove(sd.image.path)
           

        


    return render(request,'deletemehendi.html',{'mehinf':mehim})
    
def deleterangoli(request):
    if request.user.is_anonymous:
        return redirect("/")
    mehim = rangoli.objects.order_by('-id').all()

    if request.method == "POST":
        mehid = request.POST.get('rangid')
        sd = rangoli.objects.get(id=mehid)
        sd.delete()
        os.remove(sd.image.path)
           
    
   


    

    return render(request,'deleterangoli.html',{'rangoinfo':mehim})


def makeappoinment(request):
    if request.method == "POST":
        now = datetime.now()
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        contacts = request.POST.get('contact')

        if(contacts):
            check10 = str(contacts)
            m = re.match(r'^\d{10}$', check10)
            if m:
                checkmob = appoinment.objects.all()
                for checking in checkmob:
                    if(checking.number == contacts):
                        messages.add_message(request, messages.INFO, "Number Already Exist")	
                        break
                    if(checking.email == email):
                        messages.add_message(request, messages.INFO, "Email Already Exist")	
                        break
                else:
                    info = appoinment(name=name,email=email,address=address,time=now,number=contacts)
                    info.save()
                    messages.add_message(request, messages.INFO, "Appoinment Marked We Will Contact U Soon")
                   
            else:
                messages.add_message(request, messages.INFO, "Number Must Be 10 digits")
       



    return render(request,'makeappoinment.html')



def viewappoinment(request):
    if request.user.is_anonymous:
        return redirect("/")

    sinf = appoinment.objects.all()

    return render(request,'viewappoinment.html',{
        'sinf' :sinf
    })
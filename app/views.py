from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def form(request):
    if request.method=='POST':
        username=request.POST['un'] 
        password=request.POST['pw'] 
        print(username) 
        print(password)
        return HttpResponse('data is inserted')   
    return render (request,'form.html')

def data(request):
    if request.method=='POST':
        topic=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('data is inserted')
    return render(request,'data.html')
def Webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST['name']
        url=request.POST['Url']
        TO=Topic.objects.get(topic_name=topic)
        WO=WebPage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('data is inserted')
    return render(request,'Webpage.html',d)
def AcessRecords(request):
    if request.method=='POST':
        n=request.POST['name']
        date=request.POST['date']
        author=request.POST['author']
        WO=WebPage.objects.get(name=n)
        AO=AcessRecord.objects.get_or_create(name=WO,date=date,author=author)[0]
        AO.save()
        return HttpResponse('data is inserted')
    return render(request,'AcessRecord.html')


def retrieve_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        msts=request.POST.getlist('topic')
        rwos=WebPage.objects.none()
        for i in msts:
            rwos=rwos|WebPage.objects.filter(topic_name=i)
        d1={'rwos':rwos}
        return render(request,'display_webpage.html',d1)
    return render(request,'Webpage.html',d)
def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'checkbox.html',d)
    
    
    
    
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from.models import student
from.forms import Name
def pagehtml(request):
    id=loader.get_template('demo1html.html')
    return HttpResponse(id.render())
def fsave(request):
    if request.method=="POST":
        name=request.POST.get('t1')
        place=request.POST.get('t2')
        phonenumber=request.POST.get('t3')
        qualification=request.POST.get('t4')
        fathersname=request.POST.get('t5')
        mothersname=request.POST.get('t6')
        experience=request.POST.get('t7')
        s=student(name=name,place=place,phonenumber=phonenumber,qualification=qualification,fathersname=fathersname,mothersname=mothersname,experience=experience)
        s.save()
        return HttpResponse('datasave')
    else:
        return HttpResponse('data not saved')
    
def dataread(request):
    data=student.objects.all()
    return render(request,'displaydata.html',{'data':data})
def firstpage(request):
    if request.method=='POST':
        form=Name(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('http://127.0.0.1:8000/dataread')
    else: 
        form=Name()
        return render(request,'name.html',{'form':form})
def form(request):
    id=loader.get_template('name.html')
    return HttpResponse(id.render())
    

















        





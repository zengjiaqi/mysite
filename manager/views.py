#coding=utf8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from manager.models import TestModule

# Create your views here.
def index(request):
    if request.session.has_key('isLogin'):
        if request.session['isLogin']:
            return render(request,'manager/index.html',{})
    return HttpResponseRedirect('/manager/login/')  #跳转到login界面  

def add_module(request,module_name,parent_id,desc):
    modules = TestModule.objects
    tb = TestModule(module_name=module_name,module_desc=desc)
    if parent_id <= 0:
        path = modules.get(id=parent_id).path
    else:
        path = ""
    tb.save()
    last_id = modules.latest("id").id
    tb = modules.get(id=last_id)
    tb.path =  "%s%s/" % (path,last_id)
    tb.save()
    
    return HttpResponse("add_success")

def show_module_tree(request):
    modules = TestModule.objects
    moduleslist = modules.filter(path__regex=r'^[0-9]+/$')
    return render(request,'manager/manager.html',{'moduleslist':moduleslist})

def login(request):
    return render(request,'manager/login.html',{})

    
    




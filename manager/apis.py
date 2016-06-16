#coding=utf8
from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import User

@csrf_exempt
def login_api(request):
    
    response_data={}

    if request.method == "POST":
        username = request.POST["user"]
        password = request.POST['password']
    try:
        user = User.objects.get(username=username)
        if password == user.password:
            response_data['result']=1
            request.session['isLogin']=True
            request.session['user']=username
            response_data['msg']=u'登录成功'
        else:
            response_data['result']=0
            response_data['msg']=u'密码错误'
    except User.DoesNotExist,e:
        response_data['result']=0
        response_data['msg']=u'用户不存在'
    except:
        response_data['result']=-1
        response_data['msg']=u'其他错误'


        

    response = HttpResponse(json.dumps(response_data),content_type="application/json")
    

    return response




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
        else:
            response_data['result']=0
    except:
        response_data['result']=0
        

    return HttpResponse(json.dumps(response_data),content_type="application/json")




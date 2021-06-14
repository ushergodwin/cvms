from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from controller.ctrl import controller
from covidvms.models import Auth
from covidvms.usermodel import UserModel
from django.http import JsonResponse
import json

File = controller.File
Math = controller.Math


# Register your models here.
class Health:

    @classmethod
    def index(cls, request):
        current_user = ""
        username = ""
        if 'current' in request.session.keys():
            current_user = request.session.get('current')
            UserModel.set_current_user(current_user)
            userdata = UserModel.userdata()
            username = userdata['name']

            context = {
                "title": 'CVMS | Health Dashboard',
                "user": Auth.getUser(),
                "user_name": username,
                "user_email": current_user
            }
            return render(request, 'covidvms/health/dashboard.html', context)
        else:
            return redirect('/')

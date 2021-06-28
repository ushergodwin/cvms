from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from controller.ctrl.controller import File, Math, Notify
from covidvms.models import Auth
from covidvms.usermodel import UserModel
from django.http import JsonResponse
import json


import matplotlib.pyplot as plt
plt.switch_backend('agg')

from io import StringIO
import numpy as np

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
                "user_name": username,
                "user_email": current_user,
                "page": "HOME",
                "graph1": Health.return_graph()
            }
            return render(request, 'covidvms/health/dashboard.html', context)
        else:
            return redirect('/')

    @classmethod
    def return_graph(cls):
        fig = plt.figure()
        graph = fig.add_subplot(1,2,1, 
        title="Sample Bar Grap Showing Percentages of Vaccinated Citizens",
        ylabel="Vaccination (in percentage %)",
        xlabel="Population (in million)")
        x = [20,14,16,15,15,10,8,6,4,1]
        y = [10,20,30,40,50,60,70,80,90,100]
        graph.bar(x,y)
        #plt.style.use('fivethirtyeight')
        plt.plot()
        plt.close()
        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        imgdata.seek(0)

        data = imgdata.getvalue()
        return data
    
    @classmethod
    def vaccination_chart(cls, request):
        labels = ["Kampala", "Wakiso", "Jinja", "Entebbe", "Masaka", "Kabale", "Mbarara", "Kasese"]
        data = [20000000,10000000,15000000,5000000,8000000,9000000,12000000,4000000]
        content = {'labels': labels, 'data': data}
        return JsonResponse(content)

    @classmethod
    def add_citizen(cls, request):
        current_user = ""
        username = ""
        if 'current' in request.session.keys():
            current_user = request.session.get('current')
            UserModel.set_current_user(current_user)
            userdata = UserModel.userdata()
            username = userdata['name']

            context = {
                "title": 'CVMS | ADD CITIZEN',
                "user_name": username,
                "user_email": current_user,
                "page": "ADD CITIZEN",
            }
            return render(request, 'covidvms/health/add-citizen.html', context)
        else:
            return redirect('/')

    @classmethod
    def register_citizen(cls, request):
        if request.method == "POST":
            return HttpResponse(Notify.success("Request received"))
        else:
            return HttpResponse(Notify.info("Request not recognized"))

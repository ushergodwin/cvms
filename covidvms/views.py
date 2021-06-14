from django.http import HttpResponse
from django.shortcuts import redirect, render
from controller.ctrl import controller
from covidvms.models import Auth
from django.http import JsonResponse
import json
File = controller.File
Math = controller.Math
Password = controller.Password


# Create your views here.
class Home:
    request = False

    def __int__(self):
        self.request = True

    @classmethod
    def index(cls, request):
        context = {
            "title": 'Covid Vaccination Management System',
            "user": Auth.getUser(),
        }
        return render(request, 'covidvms/index.html', context)

    @classmethod
    def logout(cls, request, logout):
        try:
            if logout is not None:
                session_id = request.session.get('current')
                request.session.pop(session_id)
        except KeyError:
            pass
        return redirect('/')

    @classmethod
    def navbar(cls, request, doc):
        context = {
            "details": {}
        }
        return render(request, 'covidvms/nav.html', context)

    @classmethod
    def test_get(cls, request):
        # if "user" not in request.session:
        #     return redirect('covidvms:index')
        if request.method == "GET":
            gid = request.GET.get('id')
            age = request.GET.get('age')
            return HttpResponse("You sent id: " + gid + " and age: " + age)

    @classmethod
    def login(cls, request):
        redirect_url = "citizen/dashboard"
        if request.method == "POST" and request.POST.get('login'):
            email = request.POST.get('email')
            password = request.POST.get('password')
            Auth.authenticate(email, password)
            if Auth.email_error != "":
                return HttpResponse(json.dumps({"status": Auth.email_error}))
            if Auth.is_authenticated:
                if Auth.account_type == 1:
                    redirect_url = "health/dashboard"
                if Auth.account_type == 2:
                    redirect_url = "admin/dashboard"
                request.session['current'] = email
                return HttpResponse(json.dumps({"status": "Authenticated", "redirect": redirect_url}))
            else:
                return HttpResponse(json.dumps({"status": "Invalid email or password"}))

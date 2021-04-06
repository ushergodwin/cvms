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
    def logout(cls, request, session_id):
        try:
            del request.session[session_id]
        except KeyError:
            pass
        return render(request, 'covidvms/index.html', {})

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
        if request.method == "POST" and request.POST.get('login'):
            email = request.POST.get('email')
            password = request.POST.get('password')
            Auth.authenticate(email, password)
            if Auth.email_error != "":
                return HttpResponse(json.dumps({"status": Auth.email_error}))
            if Auth.is_authenticated:
                return HttpResponse(json.dumps({"status": "Authenticated"}))
            else:
                return HttpResponse(json.dumps({"status": "Invalid email or password"}))

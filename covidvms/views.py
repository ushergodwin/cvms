from django.http import HttpResponse
from django.shortcuts import redirect, render
from controller.ctrl.controller import File, Math, Password, String
from covidvms.models import Auth
from django.http import JsonResponse
import json
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from covidvms.usermodel import UserModel

# Create your views here.
class Home:
    request = False

    def __int__(self):
        self.request = True

    @classmethod
    def index(cls, request):
        context = {
            "title": 'Covid Vaccination Management System'
        }
        return render(request, 'covidvms/index.html', context)

    @classmethod
    def logout(cls, request, logout):
        try:
            if logout is not None:
                del request.session['current']
        except KeyError:
            pass
        return redirect('/')

    @classmethod
    def Admin_user(cls, request):  # -> HttpResponse:
        # def Adminuser(cls,request:'covidvms/admin/admin-dashboard')->HttpResponse:
        if 'current' not in request.session.keys():
            return redirect('/')

        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'Admin | Panel',
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "page": "ALL CITIZEN",
        }
        return render(request, 'covidvms/admin/dashboard.html', context)  # --> HttpResponse

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

            column = "email"

            user_key = ""

            try:
                validate_email(email)
                user_key = email
            except ValidationError as e:
                column = "username"
                user_key = String.to_lower(String.trim(email))

            Auth.authenticate(user_key, password, column)
            if Auth.email_error != "":
                return HttpResponse(json.dumps({"status": Auth.email_error}))
            if Auth.is_authenticated:
                if Auth.is_superuser == 0 and Auth.is_staff == 1:
                    redirect_url = "health/dashboard"
                if Auth.is_superuser == 1 and Auth.is_staff == 1:
                    redirect_url = "admin/dashboard"
                request.session['current'] = email
                return HttpResponse(json.dumps({"status": "Authenticated", "redirect": redirect_url}))
            else:
                return HttpResponse(json.dumps({"status": "Invalid email or password"}))

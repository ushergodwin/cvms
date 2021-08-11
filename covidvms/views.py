import json
from django.contrib.auth.hashers import make_password
from django.contrib import messages

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Sum

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from matplotlib import pyplot as plt
from pycsql.core.manager import String
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from covidvms.citizenmodel import Covid19Vaccination, Ug
from covidvms.models import Auth
from covidvms.forms import Auth_form
from covidvms.usermodel import UserModel
from io import StringIO


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
    def show_bar(cls, request):
        if 'current' not in request.session.keys():
            return redirect('/')

        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'Admin | Panel',
            "user_email": current_user,
            "page": Home.partial_graph(request),
            "labels": ['vaccination_district__name'],
            "data": ['vaccination_district__no_of_dozes'],
            "graph2": Home.return_graph1(),
            "queryset": Covid19Vaccination.objects.values('vaccination_district__name').annotate(
                vaccination_district__no_of_dozes=Sum('no_of_dozes')).order_by('-vaccination_district__no_of_dozes')
            # "page":Home.partial_graph(labels=[vaccination_district__name], data=[vaccination_district__no_of_dozes]) ,
        }

        return render(request, 'covidvms/admin/bar-graph.html', context)

    @classmethod
    def partial_graph(cls, request):
        if 'current' not in request.session.keys():
            return redirect('/')

        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)
        UserModel.set_current_user(request.session.get('current'))

        labels = []
        data = []

        queryset = Covid19Vaccination.objects.values('vaccination_district__name').annotate(
            vaccination_district__no_of_dozes=Sum('no_of_dozes')).order_by('-vaccination_district__no_of_dozes')
        for entry in queryset:
            labels.append(entry['vaccination_district__name'])
            data.append(entry['vaccination_district__no_of_dozes'])

        return JsonResponse({
            'labels': labels,
            'data': data,
        })

    @classmethod
    def navbar(cls, request, doc):
        context = {
            "details": {}
        }
        return render(request, 'covidvms/', context)

    @classmethod
    def test_get(cls, request):
        # if "user" not in request.session:
        #     return redirect('covidvms:index')
        if request.method == "GET":
            gid = request.GET.get('id')
            age = request.GET.get('age')
            return HttpResponse("You sent id: " + gid + " and age: " + age)

    @classmethod
    def staff_user(cls, request):
        if 'current' not in request.session.keys():
            return redirect('/')

        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)
        UserModel.set_current_user(request.session.get('current'))

        form = Auth_form(request.POST)
        if request.method == 'POST':
            form = Auth_form(request.POST or None)
            if form.is_valid():

                username = form.cleaned_data['username']
                email = form.cleaned_data['email']

                password = make_password(form.cleaned_data['password'])

                user = User.objects.create(username=username, email=email, password=password)
                user.is_staff = True
                user.save()

                # message = ('%(name)s is added to staff.') % {'name': username}
                # message.success(request, message)

                return HttpResponseRedirect('staff')
            else:
                form = Auth_form(request.POST)

        return render(request, 'covidvms/admin/staff.html', {'form': form})

    @classmethod
    def login(cls, request):
        redirect_url = "citizen/dashboard"
        if request.method == "POST" and request.POST.get('login'):
            email = request.POST.get('email')
            password = request.POST.get('password')

            column = "email"

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

    @classmethod
    def return_graph1(cls):
        fig = plt.figure()
        graph = fig.add_subplot(1, 2, 1,
                                title="Sample Bar Graph Showing Percentages of Vaccinated Citizens",
                                ylabel="Vaccination (in percentage %)",
                                xlabel="Population (in million)")
        x = [20, 14, 16, 15, 15, 10, 8, 6, 4, 1]
        y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        graph.bar(x, y)
        # plt.style.use('fivethirtyeight')
        plt.plot()
        plt.close()
        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        imgdata.seek(0)

        return imgdata.getvalue()

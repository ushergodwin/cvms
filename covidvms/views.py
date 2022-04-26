import json
from multiprocessing import context
from django.contrib.auth.hashers import make_password
from django.contrib import messages

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Sum

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from pycsql.core.manager import Notify, String
from django.contrib.auth.models import User

from covidvms.citizenmodel import Covid19Vaccination, Covid19Vaccines, Ug, Vaccination_centers, CitizenModel
from covidvms.models import Auth, FeedBack
from covidvms.forms import Auth_form
from covidvms.usermodel import UserModel

from pycsql.db.pycsql import pycsql

# Create your views here.
class Home:
    request = False

    def __int__(self):
        self.request = True


    @classmethod
    def index(cls, request):
        context = {
            "title": 'CVMS'
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
    def Admin_user(cls, request):
        if 'current' not in request.session.keys():
            return redirect('/')

        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'CVMS Admin | Panel',
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "page": "ALL CITIZEN",
            "no_of_districts": len(Ug.objects.all())
        }
        return render(request, 'covidvms/admin/dashboard.html', context)

    
    
    @classmethod
    def show_vaccination_graphs(cls, request, stage):
        
        if 'current' not in request.session.keys():
            return redirect('/')

        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'CVMS Admin | Panel',
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "page": "ALL CITIZEN",
            "no_of_districts": len(Ug.objects.all())
        }
        
        if stage == 'fully':
           return render(request, 'covidvms/admin/fully-vaccinated-graph.html', context)
        
        return render(request, 'covidvms/admin/first-doze-graph.html', context)


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
    def show_feedback(cls, request):
        context = {
            'title': 'CVMS | COVID 19 VACCINATION FEEDBACK',
            'vaccines': Covid19Vaccines.objects.all(),
            'centers': Vaccination_centers.objects.all()
        }
        
        return render(request, 'covidvms/citizen/feedback.html', context)
    
    
    @classmethod
    def save_feedback(cls, request):
        feedback_type = request.POST.get('feedback_type')
        vaccine_name = 'N/A' if not request.POST.get('vaccine_name') else request.POST.get('vaccine_name')
        vaccine_center = 'N/A' if not request.POST.get('vaccine_center') else request.POST.get('vaccine_center')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        feedback = request.POST.get('feedback')
        
        sql = "SELECT nin_number FROM covidvms_citizenmodel WHERE email = %s OR phone_number = %s LIMIT 1"
        nin_number = pycsql.query(sql, query_data=[email, phone_number])
        if len(nin_number) < 1:
            return HttpResponse(Notify.info("You can not provide feedback beacuse your are not registed. Please register in order to provide feedback"))
        
        feedbackObj = FeedBack.objects.create(feedback_type=feedback_type, vaccination_center=vaccine_center, vaccine_name=vaccine_name, email=email, phone_number=phone_number, side_effects=feedback)
        
        feedbackObj.save()
        
        return HttpResponse(Notify.info("Your feedback has been submitted successfully. Thank you for your response.")) 
    
    
    @classmethod
    def show_citizen_registration_form(cls, request):
        
        context = {
            'title': "CVMS | SELF REGISTRATION",
            "districts": CitizenModel.get_districts()
        }
        
        return render(request, 'covidvms/citizen/register.html', context)
    
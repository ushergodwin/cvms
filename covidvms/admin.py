from datetime import datetime

import matplotlib.pyplot as plt
from django.contrib import admin
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect, render

from pycsql.core.manager import Math
from pycsql.core.manager import Notify
from pycsql.core.manager import String
from pycsql.core.manager import Date
from pycsql.core.manager import Password
from pycsql.db.pycsql import pycsql
from covidvms.citizenmodel import CitizenModel, Covid19Vaccines, Ug, Vaccination_centers, Covid19Vaccination
from covidvms.usermodel import UserModel

from django.views.generic import TemplateView
from django.core.mail import send_mail
import smtplib
from decouple import config as env
from covidvms.models import FeedBack


# Register your models here.
class Health(TemplateView):


    @classmethod
    def index(cls, request):
        if 'current' not in request.session.keys():
            return redirect('/')
        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'CVMS | Health Dashboard',
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "page": {"active": "HOME", "nav": "HOME"},
            "no_of_districts": len(Ug.objects.all()),
            "districts": CitizenModel.get_districts()
        }
        return render(request, 'covidvms/health/dashboard.html', context)


    @classmethod
    def partial_vaccination_chart(cls, request):
        limit1 = request.GET.get('min')
        limit2 = request.GET.get('max')
        query = "SELECT dist_id, name FROM covidvms_ug ORDER BY name ASC LIMIT %s, %s"
        query_param = [int(limit1), int(limit2)]
        districts = pycsql.query(query, query_param)
        data = []
        sql = "SELECT COUNT(vaccination_id) FROM covidvms_covid19vaccination WHERE no_of_dozes = %s AND vaccination_district_id = %s"
        for dist_id, name in districts:
            vaccinated = pycsql.query(sql, [1, dist_id])
            vaccinated = max(vaccinated[0][0], 0)
            data.append({'district': String.to_upper(name), 'vaccination': vaccinated})

        return JsonResponse(data, safe=False)
            
    
    
    @classmethod 
    def fully_vaccinated_chart(cls, request):
        limit1 = request.GET.get('min')
        limit2 = request.GET.get('max')
        query = "SELECT dist_id, name FROM covidvms_ug ORDER BY name ASC LIMIT %s, %s"
        query_param = [int(limit1), int(limit2)]
        districts = pycsql.query(query, query_param)
        data = []
        sql = "SELECT COUNT(vaccination_id) FROM covidvms_covid19vaccination WHERE no_of_dozes = %s AND vaccination_district_id = %s"
        for dist_id, name in districts:
            vaccinated = pycsql.query(sql, [2, dist_id])
            vaccinated = max(vaccinated[0][0], 0)
            data.append({'district': String.to_upper(name), 'vaccination': vaccinated})

        return JsonResponse(data, safe=False)
        
        
        
    @classmethod
    def add_citizen(cls, request):
        if 'current' not in request.session.keys():
            return redirect('/')
        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'CVMS | ADD CITIZEN',
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "page": {"active": "ADD", "nav": "CITIZEN"},
            "districts": CitizenModel.get_districts()
        }
        return render(request, 'covidvms/health/add-citizen.html', context)



    @classmethod
    def register_citizen(cls, request):

        if request.method != "POST" or not request.POST.get('add_citizen'):  # here
            return HttpResponse(Notify.info("Request not recognized"))
        
        requested_by = request.POST.get('add_citizen')
        
        surname = String.trim(request.POST.get('surname'))
        given_name = String.trim(request.POST.get('givenname'))
        nationality = String.trim(request.POST.get('nationality'))
        gender = String.trim(request.POST.get('gender'))
        date_of_birth = String.trim(request.POST.get('dob'))
        nin_number = String.trim(request.POST.get('nin'))
        card_no = String.trim(request.POST.get('card_no'))
        expiry_date = String.trim(request.POST.get('expiry_date'))
        village = String.trim(request.POST.get('village'))
        parish = String.trim(request.POST.get('parish'))
        sub_county = String.trim(request.POST.get('sub_county'))
        county = String.trim(request.POST.get('county'))
        district = String.trim(request.POST.get('district'))
        phone_number = String.trim(request.POST.get('tel'))
        email_address = String.trim(request.POST.get('email'))
        
        nin_number = String.trim(request.POST.get('other_id')) if len(nin_number) < 1 else nin_number
        
        citizenInput = [surname,given_name,nationality,gender,date_of_birth,nin_number,
        expiry_date,village,parish,sub_county,county,district,phone_number,email_address
        ]

        if not String.is_not_empty(citizenInput):
            return HttpResponse(Notify.info("Oops, Some fields are empty"))
        prefix_code = "+256"
        citizen_data = {"sur_name": String.to_upper(surname),"given_name": String.to_upper(given_name),
            "nationality": nationality,"gender": gender,"date_of_birth": String.replace("/", "-", date_of_birth),
            "nin_number": nin_number,"card_no": card_no,"expiry_date": String.replace("/", "-", expiry_date),
            "village": String.to_upper(village),"parish": String.to_upper(parish),
            "sub_county": String.to_upper(sub_county),"county": String.to_upper(county),
            "district": String.to_upper(district),"phone_number": prefix_code + phone_number,
            "email": email_address
        }

        # check if user exists
        where_data = {
            "nin_number": nin_number
        }

        if CitizenModel.citizen_exits(where_data):
            return HttpResponse(Notify.failure("Citizen already exits!! Please enter another citizen."))
        
        insert_citizen = CitizenModel.add_citizen(citizen_data)

        if not insert_citizen:
            return HttpResponse(Notify.failure(
                "Oops, there was an error while adding the citizen. please try again later!!"))
        prefix = "0"

        citizen_account_info = {
            "password": Password.hash_password(prefix + phone_number),"is_superuser": 0,
            "username": String.to_lower(surname + given_name),"first_name": surname,
            "last_name": given_name,"email": email_address,"is_staff": 0,"is_active": 1,
            "date_joined": datetime.now()
        }

        citizen_vaccination_data = {
            "vaccination_id": Math.random_number(0, 99999999),
            "citizen_nin_id": nin_number,
            "doze_status": "PARTIAL"
        }

        # prepare citizen to receive the first doze
        prepared = CitizenModel.prepare_citizen_doze(citizen_vaccination_data)

        if not prepared:
            return HttpResponse(Notify.failure(
                "Oops, there was an error while preparing citizen for the first doze. please try again later!!"))

        # create the citizen's account automatically
        CitizenModel.create_citizen_account(citizen_account_info)
        
        message = "Citizen added successfully" if requested_by == 1 else "You have been registered successfully. Please go to the nearest center to receive the first doze of the vaccine of your choice. Thank you."
        
        return HttpResponse(Notify.success(message))



    @classmethod
    def view_citizens(cls, request):
        if 'current' not in request.session.keys():
            return redirect('/')
        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'CVMS | CITIZEN | ADD',
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "page": {"active": "ALL", "nav": "CITIZENS"},
            "citizens": CitizenModel.get_all_citizens()
        }
        return render(request, 'covidvms/health/view-citizens.html', context)

    
    
    @classmethod
    def view_citizen_by_id(cls, request, citizen): 
        if 'current' not in request.session.keys():
            return redirect('/')
        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'CVMS | CITIZEN VIEW ' + citizen,
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "page": {"active": citizen, "nav": "CITIZEN"},
            "citizen": CitizenModel.get_citizen_by_id(citizen)
        }
        return render(request, 'covidvms/health/view-citizen-details.html', context)
    
    
    
    @classmethod
    def view_first_doze(cls, request):
        if 'current' not in request.session.keys():
            return redirect('/')
        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'CVMS | VACCINATION | FIRST DOZE',
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "page": {"active": "FIST DOZE", 'nav': "VACCINATION"},
            "citizens": CitizenModel.get_citizen_for_first_doze()
        }
        return render(request, 'covidvms/health/first-doze.html', context)



    @classmethod
    def register_first_doze(cls, request, citizen):
        if 'current' not in request.session.keys():
            return redirect('/')
        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'CVMS | VACCINATION | FIRST DOZE',
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "page": {"active": "FIST DOZE", "nav": "VACCINATION"},
            "citizen": CitizenModel.citizen_for_first_doze(citizen),
            "vaccines": Covid19Vaccines.objects.all(),
            "current_date": Date.date(),
            "date": Date.dbdate(24, False),
            "next": Date.strtotime(4, "weeks", True),
            "next_dd": Date.strtotime(4, "weeks", True, True),
            "centers": Vaccination_centers.objects.all()
        }
        return render(request, 'covidvms/health/register-first-doze.html', context)



    @classmethod
    def save_first_doze(cls, request):
        if request.method != "POST" and not request.POST.get('register_first_doze'):
            return HttpResponse(
                Notify.failure("An error occurred while processing your request. Please contact the site admin."))
            
        vaccine_id  = request.POST.get('vaccine')
        pycsql.where({'vaccine_id': vaccine_id})
        no_of_shots = int(pycsql.getOneValue('dozes', 'covidvms_covid19vaccines'))
        
        doze_status = "FULLY" if no_of_shots == 1 else "PARTIAL"
        no_of_dozes = 2 if no_of_shots == 1 else 1
         
        citizen_nin_id = request.POST.get('citizen_nin_id')
        
        card_data = {
            "card_epi": "HMIS EPI " + String.to_string(Math.random_number(0, 99999)),
            "card_sn": String.to_string(Math.random_number(0, 99999999)),
            "batch_no": String.to_string(Math.random_number(0, 99999)) + "BD",
            "citizen_nin_id": citizen_nin_id
        }
        
        doze_data = {
            "no_of_dozes": no_of_dozes,
            "taken_at": request.POST.get('taken_date') + " " + String.to_string(datetime.time(datetime.now())),
            "next_doze_on": request.POST.get('next_doze_date') + " " + String.to_string(datetime.time(datetime.now())),
            "vaccine_type_id": request.POST.get('vaccine'),
            "vaccination_center": request.POST.get('center'),
            "vaccination_district_id": request.POST.get('dist_id'),
            "doze_status": doze_status
        }
                
        if not Covid19Vaccination.vaccinate_citizen(doze_data, citizen_nin_id):
            return HttpResponse(
                Notify.failure("Something went wrong while processing the request. Please try again later!"))
            
             
        # notify user for the next doze by email or phone number
        pycsql.where({'vaccine_id': vaccine_id})
        vaccine_name = pycsql.getOneValue('name', 'covidvms_covid19vaccines')
        message = "Hello Citizen, you have today " + String.to_string(datetime.now())
        
        cls.send_vaccination_email(no_of_dozes=no_of_dozes, vaccine_name=vaccine_name, message=message, card_data=card_data, next_doze_date=request.POST.get('next_doze_date'), email=request.POST.get('email'))
        
        return HttpResponse(Notify.success("Citizen registered for the first doze successfully"))



    @classmethod
    def view_second_doze(cls, request):
        if 'current' not in request.session.keys():
            return redirect('/')
        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'CVMS | VACCINATION | SECOND DOZE',
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "page": {"active": "SECOND DOZE", "nav": "VACCINATION"},
            "citizens": CitizenModel.get_citizen_for_second_doze()
        }
        return render(request, 'covidvms/health/second-doze.html', context)
    
    
    
    @classmethod
    def register_second_doze(cls, request, citizen):
        if 'current' not in request.session.keys():
            return redirect('/')
        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'CVMS | VACCINATION | SECOND DOZE',
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "page": {"active": "SECOND DOZE", "nav": "VACCINATION"},
            "citizen": CitizenModel.citizen_for_second_doze(citizen),
            "next": Date.strtotime(8, "weeks", True),
            "next_dd": Date.strtotime(8, "weeks", True, True),
        }
        return render(request, 'covidvms/health/register-second-doze.html', context)



    @classmethod
    def save_second_doze(cls, request):
        if request.method != "POST" and not request.POST.get('register_second_doze'):
            return HttpResponse(
                Notify.failure("An error occurred while processing your request. Please contact the site admin."))

        no_of_dozes = 2
        
        doze_data = {
            "no_of_dozes": no_of_dozes,
            "doze_status": "FULLY"
        }
        
        citizen_nin_id = request.POST.get('citizen_nin_id')
                
        card_data = {
            "card_epi": "HMIS EPI " + String.to_string(Math.random_number(0, 99999)),
            "card_sn": String.to_string(Math.random_number(0, 99999999)),
            "batch_no": String.to_string(Math.random_number(0, 99999)) + "BD",
            "citizen_nin_id": citizen_nin_id
        }


        if not Covid19Vaccination.vaccinate_citizen(doze_data, citizen_nin_id):
            return HttpResponse(
                Notify.failure("Something went wrong while processing the request. Please try again later!"))

        # notify user for the next doze by email or phone number
        vaccine_id = request.POST.get('vaccine_id')
        pycsql.where({'vaccine_id': vaccine_id})
        vaccine_name = pycsql.getOneValue('name', 'covidvms_covid19vaccines')
        message = "Hello Citizen, you have today " + String.to_string(datetime.now())
        
        cls.send_vaccination_email(no_of_dozes=no_of_dozes, vaccine_name=vaccine_name, message=message, card_data=card_data, next_doze_date=request.POST.get('next_doze_date'), email=request.POST.get('email'))
    
        return HttpResponse(Notify.success("Citizen registered for the second doze successfully"))
    
    
    
    @classmethod
    def send_vaccination_email(cls, no_of_dozes, vaccine_name, message, card_data, next_doze_date, email):
        if no_of_dozes == 2:
                    # create a vaccination card for those receiving jj
            Covid19Vaccination.create_vaccination_card(card_data)
            message += " received and completed the " + vaccine_name + " Vaccine. Please continue to observe the SOPs as directed by the Ministry of Health. Thank you."
        else:
            message += " received the first doze of " + vaccine_name + ". Your booster doze will be taken on " + next_doze_date + ". Please note this date for your reference. Thank you."
        

        #send_mail("COVID 19 VACCINATION", message, from_email=None, recipient_list=[email], fail_silently=False)
        
        mail = smtplib.SMTP_SSL(env("EMAIL_HOST"), env("EMAIL_PORT"))
        mail.login(env("EMAIL_HOST_USER"), env("EMAIL_HOST_PASSWORD"))
        mail.sendmail(env("DEFAULT_FROM_EMAIL"), email, message)
        mail.quit()
    
    @classmethod
    def fully_vaccinated(cls, request):
        if 'current' not in request.session.keys():
            return redirect('/')
        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'CVMS | FULLY VACCINATED CITIZENS',
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "page": {"active": "FULLY VACCINATED", "nav": "VACCINATION"},
            "citizens": CitizenModel.fully_vaccinated_citizen()
        }
        return render(request, 'covidvms/health/vaccinated.html', context)
    
    
    
    @classmethod
    def vaccination_clearence_card(cls, request, citizen):
        if 'current' not in request.session.keys():
            return redirect('/')
        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)
        citizen_data = CitizenModel.vaccination_card(citizen)
        context = {
            "title": 'CVMS | CITIZEN VACCINATION CARD',
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "page": {"active": "CARD", "nav": "VACCINATION"},
            "citizen": citizen_data,
            "citizen_len": max(len(citizen_data), 0),
        }

        return render(request, 'covidvms/health/vaccination_card.html', context)
    
    
    
    @classmethod
    def citizen_vaccination_card(cls, request, citizen):
        citizen_data = CitizenModel.vaccination_card(citizen)
        context = {
            "title": 'CVMS | CITIZEN VACCINATION CARD',
            "citizen": citizen_data,
            "citizen_len": max(len(citizen_data), 0),
        }
        return render(request, 'covidvms/health/vaccination_card.html', context)
    
    
    
    @classmethod
    def display_feedback(cls, request):
        if 'current' not in request.session.keys():
            return redirect('/')
        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'CVMS | CITIZEN FEEDBACK',
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "feedbacks": FeedBack.objects.all().order_by('-sent_at')
        }
        return render(request, 'covidvms/admin/feedback.html', context)


    @classmethod
    def display_feedback_for_staff(cls, request):
        if 'current' not in request.session.keys():
            return redirect('/')
        current_user = request.session.get('current')
        UserModel.set_current_user(current_user)

        context = {
            "title": 'CVMS | CITIZEN FEEDBACK',
            "user_name": UserModel.userdata()['fname'],
            "user_email": current_user,
            "feedbacks": FeedBack.objects.filter(feedback_type='Vaccine Side Effects')
        }
        return render(request, 'covidvms/health/feedback.html', context)

admin.site.register(Covid19Vaccines)
admin.site.register(Ug)
admin.site.register(Vaccination_centers)

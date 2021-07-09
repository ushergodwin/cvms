from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from controller.ctrl.controller import File, Math, Notify, String, Date, NIN, Password
from covidvms.models import Auth
from covidvms.usermodel import UserModel
from covidvms.citizenmodel import CitizenModel, Covid19Vaccines
from django.http import JsonResponse
import json
from datetime import datetime


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
            username = userdata['fname']

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
            username = userdata['fname']

            context = {
                "title": 'CVMS | ADD CITIZEN',
                "user_name": username,
                "user_email": current_user,
                "page": "ADD CITIZEN",
                "districts": CitizenModel.get_districts()
            }
            return render(request, 'covidvms/health/add-citizen.html', context)
        else:
            return redirect('/')

    @classmethod
    def register_citizen(cls, request):

        if request.method == "POST" and request.POST.get('add_citizen'):
            prefix_code = "+256"
            prifix = "0"

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

            citizenInput = [
                surname,
                given_name,
                nationality,
                gender,
                date_of_birth,
                nin_number,
                card_no,
                expiry_date,
                village,
                parish,
                sub_county,
                county,
                district,
                phone_number,
                email_address
            ]

            if String.is_not_empty(citizenInput):

                citizen_data = {
                    "sur_name": String.to_upper(surname),
                    "given_name": String.to_upper(given_name),
                    "nationality": nationality,
                    "gender": gender,
                    "date_of_birth": String.replace("/", "-", date_of_birth),
                    "nin_number" : nin_number,
                    "card_no": card_no,
                    "expiry_date": String.replace("/", "-", expiry_date),
                    "village": String.to_upper(village),
                    "parish": String.to_upper(parish),
                    "sub_county": String.to_upper(sub_county),
                    "county": String.to_upper(county),
                    "district": String.to_upper(district),
                    "phone_number": prefix_code + phone_number,
                    "email": email_address
                }

                #check if user exists
                where_data = {
                    "nin_number": nin_number,
                    "card_no": card_no,
                    "email": email_address
                }

                if not CitizenModel.citizen_exits(where_data):
                    insert_citizen = CitizenModel.add_citizen(citizen_data)

                    if insert_citizen:

                        citizen_account_info = {
                            "password": Password.hash_password(prifix + phone_number),
                            "is_superuser": 0,
                            "username": String.to_lower(surname+given_name),
                            "first_name": surname,
                            "last_name": given_name,
                            "email": email_address,
                            "is_staff": 0,
                            "is_active": 1,
                            "date_joined": datetime.now()
                        }

                        citizen_vaccination_data = {
                            "vaccination_id" : Math.random_number(0, 99999999),
                            "citizen_nin_id" : nin_number,
                            "doze_status": "PARTIAL"
                        }

                        #prepare citizen to receive the first doze
                        prepared = CitizenModel.prepare_citizen_doze(citizen_vaccination_data)

                        if prepared:
                            #create the citizen's account automatically
                            CitizenModel.create_citizen_account(citizen_account_info)
                            return HttpResponse(Notify.success("Citizen added successfully"))
                        else:
                            return HttpResponse(Notify.failure("Oops, there was an error while preparing citizen for the first doze. please try again later!!"))
                    else:
                        return HttpResponse(Notify.failure("Oops, there was an error while adding the citizen. please try again later!!"))
                else:
                    return HttpResponse(Notify.failure("Citizen already exits!! Please enter another citizen."))
            else:
                return HttpResponse(Notify.info("Oops, Some fields are empty"))
        else:
            return HttpResponse(Notify.info("Request not recognized"))

    @classmethod
    def view_citizens(cls, request):
        current_user = ""
        username = ""
        if 'current' in request.session.keys():
            current_user = request.session.get('current')
            UserModel.set_current_user(current_user)
            userdata = UserModel.userdata()
            username = userdata['fname']

            context = {
                "title": 'CVMS | ADD CITIZEN',
                "user_name": username,
                "user_email": current_user,
                "page": "ALL CITIZEN",
                "citizens": CitizenModel.get_all_citizens()
            }
            return render(request, 'covidvms/health/view-citizens.html', context)
        else:
            return redirect('/')

    @classmethod
    def view_first_doze(cls, request):
        current_user = ""
        username = ""
        if 'current' in request.session.keys():
            current_user = request.session.get('current')
            UserModel.set_current_user(current_user)
            userdata = UserModel.userdata()
            username = userdata['fname']

            context = {
                "title": 'CVMS | FIRST DOZE',
                "user_name": username,
                "user_email": current_user,
                "page": "FIST DOZE",
                "citizens": CitizenModel.get_citizen_for_first_doze()
            }
            return render(request, 'covidvms/health/first-doze.html', context)
        else:
            return redirect('/')
        
    @classmethod
    def register_first_doze(cls, request, citizen):
        current_user = ""
        username = ""
        if 'current' in request.session.keys():
            current_user = request.session.get('current')
            UserModel.set_current_user(current_user)
            userdata = UserModel.userdata()
            username = userdata['fname']

            context = {
                "title": 'CVMS | FIRST DOZE',
                "user_name": username,
                "user_email": current_user,
                "page": "FIST DOZE",
                "citizen": CitizenModel.citizen_for_first_doze(citizen),
                "vaccines": Covid19Vaccines.objects.all(),
                "current_date": Date.date(),
                "date": Date.dbdate(24, False),
                "next": Date.strtotime(21, "days", True),
                "next_dd": Date.strtotime(21, "days", True, True)
            }
            return render(request, 'covidvms/health/register-first-doze.html', context)
        else:
            return redirect('/')

admin.site.register(Covid19Vaccines)

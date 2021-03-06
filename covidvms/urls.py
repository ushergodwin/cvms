"""covidvms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home, name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import requests
from django.urls import path

from . import views
from covidvms.admin import Health

app_name = "covidvms"
urlpatterns = [
    path('', views.Home.index, name='index'),
    path('login/', views.Home.login, name="login"),
    path('health/dashboard', Health.index, name='index'),
    path('session/<str:logout>', views.Home.logout, name='logout'),
    path('vaccination_chart', Health.partial_vaccination_chart, name='vaccination_chart'),
    path('fully_vaccinated_chart', Health.fully_vaccinated_chart, name='fully_vaccinated_chart'),
    path('health/citizen/add', Health.add_citizen, name='add_citizen'),
    path('register/', Health.register_citizen, name="register_citizen"),
    path('health/citizens/view',Health.view_citizens, name='view_citizens'),
    path('health/citizen/view/<str:citizen>', Health.view_citizen_by_id, name='view_citizen_by_id'),
    path('health/citizen/details/<str:citizen>', Health.view_citizen_by_email, name='view_citizen_by_email'),
    path('health/vaccination/first-doze', Health.view_first_doze, name='view_first_doze'),
    path('health/vaccination/register/<str:citizen>', Health.register_first_doze, name='register_first_doze'),
    path('admin/dashboard', views.Home.Admin_user, name='Admin_user'),
    path('admin/dashboard/citizen/details/<str:citizen>', Health.admin_view_citizen_by_email, name='admin_view_citizen_by_email'),
    path('admin/dashboard/staff', views.Home.staff_user, name='staff_user'),

    path('admin/dashboard/graphs/<str:stage>', views.Home.show_vaccination_graphs, name='show_vaccination_graphs'),
    path('admin/dashboard/vaccination/feedback', Health.display_feedback, name='display_feedback'),
    path("vaccination/register/first-doze", Health.save_first_doze, name="save_first_doze"),
    path("vaccination/register/second-doze", Health.save_second_doze, name="save_second_doze"),
    path('health/vaccination/second-doze', Health.view_second_doze, name='view_second_doze'),
    path('health/vaccination/register/second-doze/<str:citizen>', Health.register_second_doze, name='register_second_doze'),
    path('health/vaccination/completed', Health.fully_vaccinated, name="fully_vaccinated"),
    path('health/vaccination/card/<str:citizen>', Health.vaccination_clearence_card, name='vaccination_clearence_card'),
    path('health/vaccination/feedback/side_effects', Health.display_feedback_for_staff, name='display_feedback_for_staff'),
    path('health/citizen/vaccination/card/<str:citizen>', Health.citizen_vaccination_card, name='citizen_vaccination_card'),
    path('health/citizen/vaccination_card/download/<str:citizen>', Health.download_vaccination_card_pdf, name='download_vaccination_card_pdf'),
    path('health/citizen/vaccination/feedback', views.Home.show_feedback, name='show_feedback'),
    path('health/citizen/vaccination/feedback/save', views.Home.save_feedback, name='save_feedback'),
    path('health/citizen/vaccination/register', views.Home.show_citizen_registration_form, name='show_citizen_registration_form'),
]

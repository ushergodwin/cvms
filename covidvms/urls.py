"""covidvms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from . import views
from . import admin

app_name = "covidvms"
urlpatterns = [
    path('', views.Home.index, name='index'),
    path('login/', views.Home.login, name="login"),
    path('health/dashboard', admin.Health.index, name='health'),
    path('session/<str:logout>', views.Home.logout, name='logout'),
    path('vaccination_chart/', admin.Health.vaccination_chart, name ='vaccination_chart'),
    path('health/add-citizen', admin.Health.add_citizen, name='add-citizen'),
    path('register/', admin.Health.register_citizen, name="register_citizen"),
    path('health/view-citizens', admin.Health.view_citizens, name='view-citizens'),
    path('health/vaccination/first-doze', admin.Health.view_first_doze, name='view-first-doze'),
    path('health/vaccination/register/<str:citizen>', admin.Health.register_first_doze, name='register-first-doze'),
    path('health/dashboard/Admin-us/', views.Home.Admin_user, name='Admin_user'),

]

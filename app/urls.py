from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.Home,name="Home"),
    path("Request_Abmulance/",views.Request_Abmulance,name="Request_Abmulance"),
    path("Ambulance_Confirm/",views.Ambulance_Confirm,name="Ambulance_Confirm"),
    path("appointment/",views.Appointment,name="appointment"),
    path("Appointment_Confirm/",views.Appointment_Confirm,name="Appointment_Confirm"),
    path("SignUp/",views.SignUp,name="SignUp"),
]
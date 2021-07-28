from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Ambulance)
admin.site.register(Reason)
admin.site.register(Disease)
admin.site.register(Appointment)
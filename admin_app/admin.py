from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Speciality)
admin.site.register(Doctor)
admin.site.register(Shift)
admin.site.register(Nurse)
admin.site.register(Room_Service)
admin.site.register(Gender)


from django.contrib import admin
from appointment.models import Appointment

# Register your models here.


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'date_time')


admin.site.register(Appointment, AppointmentAdmin)

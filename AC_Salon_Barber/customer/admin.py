from django.contrib import admin
from customer.models import Customer

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'name', 'phone_number')


admin.site.register(Customer, CustomerAdmin)

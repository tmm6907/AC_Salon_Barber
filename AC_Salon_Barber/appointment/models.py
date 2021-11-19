from django.db import models
from django.db.models.deletion import CASCADE
from customer.models import Customer

# Create your models here.


class Appointment(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=CASCADE)
    date_time = models.DateTimeField()

    def _str_(self):
        return self.customer_id

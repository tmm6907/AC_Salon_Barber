from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_id = models.IntegerField(max_length=8, primary_key=True)
    name = models.CharField(max_length=24)
    phone_number = models.CharField(max_length=11)

    def _str_(self):
        return self.name

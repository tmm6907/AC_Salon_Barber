from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from api.serializers import AppointmentSerializer, CustomerSerializer
from appointment.models import Appointment
from customer.models import Customer


class AppointmentCreateViewset(GenericViewSet, mixins.CreateModelMixin):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentListViewset(GenericViewSet, mixins.ListModelMixin):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class CustomerCreateViewset(GenericViewSet, mixins.CreateModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerListViewset(GenericViewSet, mixins.ListModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

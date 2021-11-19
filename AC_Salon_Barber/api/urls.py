from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import AppointmentCreateViewset, AppointmentListViewset, CustomerCreateViewset, CustomerListViewset


router = DefaultRouter()

router.register(r'customer-create', CustomerCreateViewset)
router.register(r'customer-list', CustomerListViewset)
router.register(r'appointment-create', AppointmentCreateViewset)
router.register(r'appointment-list', AppointmentListViewset)

urlpatterns = [
    path('', include(router.urls))
]

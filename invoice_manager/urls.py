from django.urls import path, include
from rest_framework.routers import DefaultRouter
from invoices.api import InvoiceViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

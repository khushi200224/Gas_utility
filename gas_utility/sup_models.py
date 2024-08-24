# support/models.py
from django.db import models
from customers.models import Customer
from requests.models import ServiceRequest

class SupportTicket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=255, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
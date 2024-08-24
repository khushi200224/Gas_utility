# requests/models.py
from django.db import models
from customers.models import Customer

class ServiceRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=255)
    description = models.TextField()
    attachment = models.FileField(upload_to='requests/attachments/')
    status = models.CharField(max_length=255, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
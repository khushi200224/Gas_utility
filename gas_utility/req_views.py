# requests/views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import ServiceRequest

class ServiceRequestListView(ListView):
    model = ServiceRequest
    template_name = 'requests/service_request_list.html'

class ServiceRequestDetailView(DetailView):
    model = ServiceRequest
    template_name = 'requests/service_request_detail.html'

class ServiceRequestCreateView(CreateView):
    model = ServiceRequest
    fields = ('request_type', 'description', 'attachment')
    template_name = 'requests/service_request_form.html'
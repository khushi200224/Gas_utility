# customers/views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Customer

class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'

class CustomerCreateView(CreateView):
    model = Customer
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'address')
    template_name = 'customers/customer_form.html'
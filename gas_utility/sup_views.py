# support/views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import SupportTicket

class SupportTicketListView(ListView):
    model = SupportTicket
    template_name = 'support/support_ticket_list.html'

class SupportTicketDetailView(DetailView):
    model = SupportTicket
    template_name = 'support/support_ticket_detail.html'

class SupportTicketCreateView(CreateView):
    model = SupportTicket
    fields = ('description',)
    template_name = 'support/support_ticket_form.html'
from django.shortcuts import render
from django.views import generic as views

# class InvoiceListView(views.View):
#     template_name = 'invoices/invoices.html'


def invoices(request):
    return render(request, 'invoices/invoices.html')
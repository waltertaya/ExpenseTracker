from django.shortcuts import render
from .models import Expense


def home(request):
    return render(request, 'expenses/home.html')


def reports(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/reports.html', {'expenses': expenses})


def dashboard(request):
    return render(request, 'expenses/dashboard.html')


def expenses(request):
    return render(request, 'expenses/expenses.html')

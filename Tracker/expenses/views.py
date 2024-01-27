from django.shortcuts import render, redirect
from .models import Expense


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        work_id = request.POST.get('work_id')

        # Store the data in the session
        request.session['username'] = username
        request.session['email'] = email
        request.session['work_id'] = work_id
        return redirect('home', name=username)
    else:
        return render(request, 'expenses/login.html')


def home(request, name=''):
    username = request.session.get('username', 'Guest')
    email = request.session.get('email', '')
    work_id = request.session.get('work_id', '')

    return render(request, 'expenses/home.html', {'username': username,
                                                  'email': email,
                                                  'work_id': work_id})


def reports(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/reports.html', {'expenses': expenses})


def dashboard(request):
    return render(request, 'expenses/dashboard.html')


def expenses(request):
    return render(request, 'expenses/expenses.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def userlogin(request):
    return render(request, 'userlogin.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    """
    The home page of the weatherstation web app
    :param request:
    :return:
    """
    # TODO: read measurement data from shared file share
    return render(request, 'index/index.html')

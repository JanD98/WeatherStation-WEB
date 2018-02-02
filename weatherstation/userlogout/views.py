from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout


def userlogout(request):
    """
    The home page of the weatherstation web app
    :param request:
    :return:
    """
    # TODO: read measurement data from shared file share
    return render(request, 'userlogout/')

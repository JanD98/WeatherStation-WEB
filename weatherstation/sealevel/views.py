from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/login')
def sealevel(request):
    """
    The home page of the weatherstation web app
    :param request:
    :return:
    """
    # TODO: read measurement data from shared file share
    return render(request, 'sealevel/sealevel.html')

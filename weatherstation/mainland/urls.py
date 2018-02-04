"""weatherstation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mainland, name='mainland'),
    # Line chart data
    url(r'^temperature_chart/json/$', views.temperature_chart_json,
        name='temperature_chart_json'),
    url(r'^wind_chart/json/$', views.wind_chart_json,
        name='wind_chart_json'),
    url(r'^rainfall_chart/json/$', views.rainfall_chart_json,
        name='rainfall_chart_json'),

    url(r'^download/', views.download, name='download')
]

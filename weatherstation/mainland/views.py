import csv

from chartjs.views.lines import BaseLineChartView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from chartjs.colors import next_color, COLORS
from random import shuffle

from .datamanagement.datagatherer import DataGatherer


class TemperatureChart(BaseLineChartView):

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "00:00"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Temperature", "Average Temperature Sea", "Average Temperature Land"]

    def get_data(self):
        """Return 3 datasets to plot."""
        return DataGatherer().get_temperature_data()

    def get_colors(self):
        colors = COLORS[3:6]
        return next_color(colors)


class WindChart(BaseLineChartView):

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "00:00"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Wind", "Average Wind Sea", "Average Wind Land"]

    def get_data(self):
        """Return 3 datasets to plot."""
        return DataGatherer().get_wind_data()

    def get_colors(self):
        colors = COLORS[3:6]
        return next_color(colors)


class RainfallChart(BaseLineChartView):

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "00:00"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Rainfall", "Average Rainfall Sea", "Average Rainfall Land"]

    def get_data(self):
        """Return 3 datasets to plot."""
        return DataGatherer().get_rainfall_data()

    def get_colors(self):
        colors = COLORS[3:6]
        return next_color(colors)


temperature_chart_json = TemperatureChart.as_view()
wind_chart_json = WindChart.as_view()
rainfall_chart_json = RainfallChart.as_view()


@login_required()
def mainland(request):
    """
    The home page of the weatherstation web app
    :param request:
    :return:
    """
    # TODO: read measurement data from shared file share
    return render(request, 'mainland.html')


def downloadtemp(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="chart-data.csv"'

    c = TemperatureChart()
    data = DataGatherer.get_temperature_data()

    wr = csv.writer(response, delimiter=';', lineterminator='\n')
    wr.writerow(c.get_providers())
    for temperature_type in list(zip(*data)):
        print(temperature_type)
        wr.writerow(temperature_type)
    return response


def downloadrain(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="chart-data.csv"'

    c = RainfallChart()
    data = DataGatherer.get_rainfall_data()

    wr = csv.writer(response, delimiter=';', lineterminator='\n')
    wr.writerow(c.get_providers())
    for rainfall_type in list(zip(*data)):
        print(rainfall_type)
        wr.writerow(rainfall_type)
    return response


def downloadwind(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="chart-data.csv"'

    c = WindChart()
    data = DataGatherer.get_wind_data()

    wr = csv.writer(response, delimiter=';', lineterminator='\n')
    wr.writerow(c.get_providers())
    for wind_type in list(zip(*data)):
        print(wind_type)
        wr.writerow(wind_type)
    return response
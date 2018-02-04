import csv

from chartjs.views.lines import BaseLineChartView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .datamanagement.datagatherer import DataGatherer


class TemperatureChart(BaseLineChartView):

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "00:00"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Temperature", "Temperature Sea", "Temperature Land"]

    def get_data(self):
        """Return 3 datasets to plot."""
        return DataGatherer().get_temperature_data()


class WindChart(BaseLineChartView):

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "00:00"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Wind", "Wind Sea", "Wind Land"]

    def get_data(self):
        """Return 3 datasets to plot."""
        return DataGatherer().get_wind_data()


class RainfallChart(BaseLineChartView):

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "00:00"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Rainfall", "Rainfall Sea", "Rainfall Land"]

    def get_data(self):
        """Return 3 datasets to plot."""
        return DataGatherer().get_rainfall_data()


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


def download(request):
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

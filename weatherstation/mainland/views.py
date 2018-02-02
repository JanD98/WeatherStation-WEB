from chartjs.views.lines import BaseLineChartView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView

from .datamanagement.datagatherer import DataGatherer


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "00:00"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Temperature"]

    def get_data(self):
        """Return 3 datasets to plot."""
        return DataGatherer().readdata()


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()


@login_required(login_url='/login/')
def mainland(request):
    """
    The home page of the weatherstation web app
    :param request:
    :return:
    """
    # TODO: read measurement data from shared file share
    return render(request, 'mainland.html')

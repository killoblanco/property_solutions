from django.conf.urls import url
from core.scrumboard.api.views import *

urlpatterns = [
    url(r'type-chart-data$', RequestTypeChartData.as_view(), name='type_chart_data'),
    url(r'priority-chart-data$', RequestPriorityChartData.as_view(), name='priority_chart_data'),
    url(r'deadline-chart-data$', RequestDeadlineChartData.as_view(), name='deadline_chart_data'),
]
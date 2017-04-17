import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response

from core.scrumboard.models import Requirements


class RequestTypeChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            'labels': [],
            'data': [],
            'label': 'Type',
            'type': 'doughnut'
        }
        qs = list(Requirements.objects.values_list('type', flat=True))
        s = pd.Series(qs)
        count = dict(s.value_counts())
        for label, d in count.items():
            data['labels'].append(label)
            data['data'].append(d)

        return Response(data)


class RequestPriorityChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            'labels': [1, 2, 3, 4, 5],
            'data': [],
            'label': 'Priority',
            'type': 'bar'
        }
        qs = list(Requirements.objects.values_list('priority', flat=True))
        s = pd.Series(qs)
        count = dict(s.value_counts())
        for label in data['labels']:
            if str(label) in count.keys():
                data['data'].append(count[str(label)])
            else:
                data['data'].append(0)

        return Response(data)

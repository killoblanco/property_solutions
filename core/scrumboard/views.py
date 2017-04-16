from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from core.scrumboard.models import Requirements
from core.scrumboard.forms import RequirementForm


# Create your views here.
class IndexView(View):
    template_name = 'scrumboard/pages/index.html'

    page = {
        'title': 'Scrum Board'
    }

    def get(self, request, *args, **kwargs):
        context = {
            'page': self.page,
        }
        return render(request, self.template_name, context)


class RequestsListView(ListView):
    model = Requirements
    context_object_name = 'requirements'
    template_name = 'scrumboard/pages/list.html'


class CreateRequestView(CreateView):
    template_name = 'scrumboard/pages/form.html'
    form_class = RequirementForm
    success_url = reverse_lazy('core:scrumboard:list')

from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View
from web.forms import ContactForm
from mailg.core import Mailg


# Create your views here.
class OnePageView(View):
    form_class = ContactForm
    template_name = 'web/pages/one_page.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            mailer = Mailg()
            mailer.data['to'] = [form.cleaned_data['email']]
            mailer.data['subject'] = form.cleaned_data['subject']
            msg = "Hi, my name is {}.\n\nI'd like to ask you about {}"
            mailer.data['text'] = msg.format(form.cleaned_data['name'], form.cleaned_data['message'])
            try:
                mailer.send_mail()
                messages.success(request, "Thank you for contact us!")
            except:
                messages.error(request, 'The email can not be send')

            context = {
                'form': self.form_class()
            }
        return render(request, self.template_name, context)

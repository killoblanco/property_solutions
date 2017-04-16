from crispy_forms.layout import Submit
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from core.scrumboard.models import Requirements


class RequirementForm(ModelForm):
    class Meta:
        model = Requirements
        fields = ['type', 'priority', 'detail', 'deadline']

    def __init__(self, *args, **kwargs):
        super(RequirementForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

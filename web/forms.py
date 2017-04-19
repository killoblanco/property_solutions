from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CrispyContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=True
    )
    email = forms.EmailField(
        required=True
    )
    subject = forms.CharField(
        max_length=255,
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Name'
        })
    )
    email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email'
        })
    )
    subject = forms.CharField(
        max_length=255,
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Subject'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Message'
        }),
        required=True,
        label=''
    )

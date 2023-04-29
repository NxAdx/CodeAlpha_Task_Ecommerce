from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('D', 'Debit Card'),
    ('C', 'Credit Card')
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Dwarka Nagar',
        'class': 'textinput form-control'
    }))
    apartments_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Betul',
        'class': 'apartments_address textinput form-control'
    }))
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100 countryselectwidget form-select'
        }))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'textinput form-control'

    }))
    same_billing_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=PAYMENT_CHOICES)

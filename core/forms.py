from django import forms
from django_countries.fields import CountryField

PAYMENT_CHOICES = (
    ('D', 'Debit Card'),
    ('C', 'Credit Card')
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Dwarka Nagar'
    }))
    apartments_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Betul'
    }))
    country = CountryField(blank_label='(select country)').formfield(attrs={
        'class': 'form-control'
    })
    zip_code = forms.CharField()
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=PAYMENT_CHOICES)

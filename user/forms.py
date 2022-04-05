from unittest.util import _MAX_LENGTH
from django import forms
from user.models import BillingAddress


class AddresForm(forms.ModelForm):
    
    class Meta:
        model = BillingAddress
        fields = (
            'first_name',
            'last_name',
            'email',
            'country',
            'address',
            'town',
            'mobile_phone',
            'information',
            'reference',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address'
            }),
            'country': forms.Select(attrs={
                'placeholder': 'Country',
                'class': 'form-control'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Address'
            }),
            'town': forms.Select(attrs={
                'placeholder': 'Town/City',
                'class': 'form-control'
            }),
            'mobile_phone': forms.NumberInput(attrs={
                'placeholder': 'Mobile phone'
            }),
            'information': forms.Textarea(attrs={
                'placeholder': 'Additional information',
                'rows': 2
            }),
            'reference': forms.TextInput()
            

        }



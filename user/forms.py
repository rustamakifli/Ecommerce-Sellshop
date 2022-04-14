from django import forms
from user.models import BillingAddress
from django.contrib.auth import get_user_model


USER = get_user_model()

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

# class RegisterForm(forms.ModelForm):
#     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Confirm Password'
#             }))

#     class Meta:
#         model = USER
#         fields = (
#             'first_name',
#             'email',
#             'phone_number',
#             'username',
#             'password',
#             'confirm_password'
#         )

#         widgets = {
#             'first_name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Name here'
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Email'
#             }),
#             'phone_number':forms.CharField(),
#             'username': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Username'
#             }),
#             'password': forms.PasswordInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Password'
#             })
#         }

#     def clean(self):
#         data = self.cleaned_data
#         if data['password'] != data['confirm_password']:
#             raise forms.ValidationError("Password and confirm_password does not match")
#         return super().clean()



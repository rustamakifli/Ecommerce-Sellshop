from django import forms
from core.models import Contact, Subscribe


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'message',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your Name...'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email...'
            }),
            'message': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Enter your message...'
            })
        }

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email...'
            }),
        }
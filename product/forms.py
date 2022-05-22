from django import forms
from product.models import ProductReview


class ProductReviewsForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = (
            'name',
            'email',
            'review',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your email'
            }),
            'review': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Your review'
            })
        }

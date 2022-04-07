from django import forms
from product.models import ProductReviews


class ProductReviewsForm(forms.ModelForm):
    class Meta:
        model = ProductReviews
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

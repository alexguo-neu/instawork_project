from django import forms

from .models import People
import re


class PeopleModelForm(forms.ModelForm):
    phone = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$',
        widget=forms.NumberInput(attrs={
                'placeholder': 'Please enter your phone number'
        }),
        error_messages={"invalid": "Phone number not valid"}
    )

    class Meta:
        model = People
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'role',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Please enter your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Please enter your last name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Please enter your email'
            }),
            'role': forms.RadioSelect()
        }

    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     pattern = re.compile("^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$")
    #     if not bool(pattern.match(phone)):
    #         print("yyyyyyyy")
    #         raise forms.ValidationError("This is not a valid phone number")
    #     return phone

from django import forms

from .models import People

class PeopleModelForm(forms.ModelForm):
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
            'phone': forms.NumberInput(attrs={
                'placeholder': 'Please enter your phone number'
            }),
            'role': forms.RadioSelect()
        }


    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if title.lower() == 'abc':
    #         raise forms.ValidationError("This is not a valid title")
    #     return title
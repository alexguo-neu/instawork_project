from django import forms

from .models import People


class PeopleModelForm(forms.ModelForm):
    class Meta:
        model = People
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone'
        ]

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if title.lower() == 'abc':
    #         raise forms.ValidationError("This is not a valid title")
    #     return title
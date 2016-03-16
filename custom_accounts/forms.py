from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email',]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

class contact_us_form(forms.Form):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=False,max_length=30)
    message = forms.CharField(required=True, max_length=250)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

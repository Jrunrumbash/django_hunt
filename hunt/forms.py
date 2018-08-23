from django import forms
from django.core.exceptions import ValidationError

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class PlayerForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=200)
    email = forms.EmailField(label="Ericsson email", max_length=200)
    password1 = forms.CharField(label='Choose Password')
    password2 = forms.CharField(label='Confirm Password')

    def clean(self):
        password1 = self.cleaned_data.get('password1', None)
        password2 = self.cleaned_data.get('password2', None)
        print(password1)
        print(password2)

        if password1 and password2 and (password1 == password2):
            pass

        else:
            raise ValidationError(('Passwords do not match!!'))

    def clean_name(self):
        name = self.cleaned_data['name']
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if "ericsson.com" not in email:
            raise ValidationError(('Not an ericsson email'))
        return email
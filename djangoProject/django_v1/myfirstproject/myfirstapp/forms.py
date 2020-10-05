from django import forms
from myfirstapp.models import property_type
from .models import Register
import re

prop_type_choices = [
        ('CONDO', 'Condominium'),
        ('COOP', 'Housing Cooperative'),
        ('SFAM', 'Single-Family'),
        ('MULTI', 'Multi-Family'),
    ]

class Registeration(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    vpassword = forms.CharField(widget=forms.PasswordInput,label="Re-enter the Password")
    prop_type = forms.CharField(label='Select a property type you are interested in:',widget=forms.Select(choices=prop_type_choices))

    class Meta:
        model = Register
        fields = "__all__"

    def clean(self):
        super(Registeration,self).clean()

        password = self.cleaned_data.get('password')
        UpperPass = 0
        LowerPass = 0
        dititPass = 0
        spChar = ''
        UpperPass = sum(1 for i in password if i.isupper())
        LowerPass = sum(1 for i in password if i.isupper())
        dititPass = sum(1 for i in password if i.isdigit())
        spChar = re.sub('[\w]+', '', password)

        if ((UpperPass < 1) or (LowerPass < 1) or (dititPass < 1) or (len(spChar) < 1)):
            self._errors['password'] = self.error_class(["Password needs to have at-least 1 lower case letter, 1 upper case letter, 1 digit, and 1 special character"])

        vpassword = self.cleaned_data.get('vpassword')

        if password != vpassword:
            self._errors['vpassword'] = self.error_class(["Passoword Doesn't Match"])


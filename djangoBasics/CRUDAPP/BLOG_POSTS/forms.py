from django import forms
from .models import Property_Info

class Listings(forms.ModelForm):
    class Meta:
        model = Property_Info
        fields = "__all__"
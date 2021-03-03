from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('contact_name', 'contact_number', 'email', 'category', 'description')


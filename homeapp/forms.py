from django import forms
from homeapp.models import Contact, ImageModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'

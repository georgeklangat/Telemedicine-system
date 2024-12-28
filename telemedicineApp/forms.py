from django import forms

from telemedicineApp.models import Appointment, Product, Contact, ImageModel


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class ImagemodelForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'

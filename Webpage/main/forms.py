from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact, DatePicker, Profile # add this for user profile

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
	class Meta: 
		model = Profile
		fields = ('user',)

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'


class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	file = forms.FileField()

class FileForm(forms.Form):
	id = forms.IntegerField()
	Date = forms.DateTimeField()
	Distance_travelled = forms.FloatField()
	Average_EngineRPM = forms.IntegerField()
	Fuel_used = forms.FloatField()
	Average_Vehiclespeed =  forms.FloatField()
	Driver_Risk = forms.IntegerField()

class DateInput(forms.DateInput):
    input_type = 'date'

class DatePickerForm(forms.ModelForm):

    class Meta:
        model = DatePicker
        fields = [ 'date']
        widgets = {
            'date': DateInput(),
        }

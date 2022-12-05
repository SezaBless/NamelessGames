from django import forms
from .models import ContactProfile ,Blog  #, Testimonial 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Se usaron forms para Creacion de usuarios y para el contacto 

class CreateUserForm(UserCreationForm):
	class meta :
		model = User 
		fields =["username", "email", "pasword1", "pasword2"]

class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Message..',
			'rows': 6,
			}))


	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message',)
		
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	numero_de_telephone_whatsapp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

	def clean_numero_de_telephone(self):
		numero_de_telephone = self.cleaned_data['numero_de_telephone']

		# Vérifier que le numéro de téléphone est valide
		if not phonenumbers.is_valid_number(numero_de_telephone):
			raise forms.ValidationError("Le numéro de téléphone n'est pas valide.")

		return numero_de_telephone


class UserUpdateForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')


class PasswordUpdateForm(PasswordChangeForm):
	class Meta:
		model = User
		fields = ('password', 'newpassword1', 'newpassword2')

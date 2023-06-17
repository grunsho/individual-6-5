from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class FormularioLogin(AuthenticationForm):
    username = forms.CharField(max_length=50, required=True, label='Nombre de Usuario', error_messages={
                                    'required': 'El usuario es obligatorio'})
    password = forms.CharField(max_length=16, required=True, label='Contraseña',
                                widget=forms.PasswordInput, error_messages={
                                    'required': 'La contraseña es obligatoria'})

class RegistroUsuariosForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistroUsuariosForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de Usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar Contraseña'
        self.fields['first_name'].label = 'Nombre'
        self.fields['last_name'].label = 'Apellido'
        self.fields['email'].label = 'Correo electrónico'
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()


    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields
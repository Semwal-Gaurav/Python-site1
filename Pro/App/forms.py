from django import forms
from .models import UserRegisterForm, UserLogin



class UserRegisterForms(forms.ModelForm):

    class Meta:
        model = UserRegisterForm  
        fields = ['username', 'email', 'password', 'confirmpassword']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        confirmpassword = cleaned_data.get('confirmpassword')

        if UserRegisterForm .objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email address already exists.")

        if UserRegisterForm .objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")

        if password != confirmpassword:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
    

class UserLogins(forms.ModelForm):
    class Meta:
        model = UserLogin
        fields = ['username', 'password']

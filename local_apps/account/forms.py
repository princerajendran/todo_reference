from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm


class AddUserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('account_id', 'name', 'email', 'mobile', 'image', 'role')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UpdateUserForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'mobile', 'image', 'role', 'is_active', 'is_staff', 'is_superuser')

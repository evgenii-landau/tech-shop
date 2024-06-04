from django import forms


class LoginUserForm(forms.Form):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={"class": "form__input"}),
        help_text="Пожалуйста введите логин",
    )
    password = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form__input"})
    )

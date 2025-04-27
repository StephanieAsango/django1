from django import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_bulma.layout import Layout,Field

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "myforms"
        self.helper.form_method ="post"
        self.helper.form_class = "mg-5"
        

        self.helper.layout = Layout(
            Field("username", placeholder = "Name"),
            Field("email", placeholder = "Email"),
            Field("password1",placeholder = "Password"),
            "password2"
        )
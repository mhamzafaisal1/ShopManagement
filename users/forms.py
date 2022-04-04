# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from django.contrib.auth.models import User

# class UserCreateForm(UserCreationForm):
#     class Meta:
#         model = User 
#         fields = ("username","password1","password2")
#         help_texts = {
#             'username' : None,
#         }








from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):

    def _init_(self, *args, **kwargs):
        super(UserCreateForm, self)._init_(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
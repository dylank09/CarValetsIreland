from django import forms
from valetapp.models.Users.membershiptype import MembershipType
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    # membership_types = MembershipType.objects.all()
    # colours = [(colour, colour.get_colour()) for colour in membership_types]
    # colours = tuple(colours)
    # colours = forms.ChoiceField(
    #     choices=colours, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

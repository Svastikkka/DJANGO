from django import forms
from users.models import users


class NewFormUser(forms.ModelForm):
    class Meta:
        model = users
        fields = "__all__"

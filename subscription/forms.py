from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class FollowUserButton(forms.Form):
    user_to_follow = forms.CharField(widget=forms.HiddenInput())


class SearchUser(forms.Form):
    search = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Rechercher un utilisateur'
            }
        )
    )
    search_user_id = forms.BooleanField(widget=forms.HiddenInput, initial=True)

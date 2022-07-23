from django.contrib.auth import get_user_model
from django import forms
<<<<<<< HEAD
=======
from . import models
>>>>>>> f3dc60dde3dd6edbe4a2fcebb4307cc0156b0a30

User = get_user_model()


<<<<<<< HEAD
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
=======
class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = models.UserFollows
        fields = ['followed_user', ]

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            user = kwargs.pop('user')
            self.fields['user'] = user
        super().__init__(*args, **kwargs)

>>>>>>> f3dc60dde3dd6edbe4a2fcebb4307cc0156b0a30

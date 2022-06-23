from django.contrib.auth import get_user_model
from django import forms
from . import models

User = get_user_model()


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = models.UserFollows
        fields = ['followed_user', ]

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            user = kwargs.pop('user')
            self.fields['user'] = user
        super().__init__(*args, **kwargs)


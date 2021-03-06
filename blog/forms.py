from django import forms
<<<<<<< HEAD
=======

>>>>>>> f3dc60dde3dd6edbe4a2fcebb4307cc0156b0a30
from . import models


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class TicketFormDelete(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class CritiqueForm(forms.ModelForm):
    edit_critique = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Critique
        fields = ['headline', 'body', 'rating']


class CritiqueFormDelete(forms.Form):
    delete_critique = forms.BooleanField(widget=forms.HiddenInput, initial=True)

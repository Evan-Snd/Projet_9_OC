from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from . import forms, models


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    critiques = models.Critique.objects.all()
    return render(request, 'blog/home.html', context={'tickets': tickets, 'critiques': critiques})


@login_required
def create_ticket(request):
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            if ticket_form.cleaned_data['image']:
                ticket.image = ticket_form.cleaned_data['image']
            ticket.save()
            return redirect('home')
    context = {
        'ticket_form': ticket_form,
}
    return render(request, 'blog/create_ticket_post.html', context=context)


@login_required
def create_critique(request, ticket_id):
    critique_form = forms.CritiqueForm()
    if request.method == 'POST':
        critique_form = forms.CritiqueForm(request.POST)
        if critique_form.is_valid():
            critique = critique_form.save(commit=False)
            critique.user = request.user
            critique.ticket = get_object_or_404(models.Ticket, id=ticket_id)
            critique.ticket.save()
            critique.save()
            return redirect('home')
    context = {
        'critique_form': critique_form,
}
    return render(request, 'blog/create_critique_post.html', context=context)


@login_required
def create_ticket_and_critique(request):
    ticket_form = forms.TicketForm()
    critique_form = forms.CritiqueForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        critique_form = forms.CritiqueForm(request.POST)
        if all([ticket_form.is_valid(), critique_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            if ticket_form.cleaned_data['image']:
                ticket.image = ticket_form.cleaned_data['image']
            ticket.save()
            critique = critique_form.save(commit=False)
            critique.user = request.user
            critique.ticket = get_object_or_404(models.Ticket, id=ticket.id)
            critique.save()
            return redirect('feed')
    context = {
        'ticket_form': ticket_form,
        'critique_form': critique_form
    }
    return render(
        request,
        'blog/create_critique_post.html',
        context
    )


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_ticket_form = forms.TicketForm(instance=ticket)
    delete_ticket_form = forms.TicketFormDelete()
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_ticket_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_ticket_form.is_valid():
                edit_ticket_form.save()
                return redirect('home')
        if 'delete_ticket' in request.POST:
            delete_ticket_form = forms.TicketFormDelete(request.POST)
            if delete_ticket_form.is_valid():
                ticket.delete()
                return redirect('home')
    context = {
        'edit_ticket_form': edit_ticket_form,
        'delete_ticket_form': delete_ticket_form
    }
    return render(
        request,
        'blog/edit_ticket.html',
        context
    )


@login_required
def edit_critique(request, critique_id):
    critique = get_object_or_404(models.Critique, id=critique_id)
    edit_critique_form = forms.CritiqueForm(instance=critique)
    delete_critique_form = forms.CritiqueFormDelete()
    if request.method == 'POST':
        if 'edit_critique' in request.POST:
            edit_critique_form = forms.CritiqueForm(request.POST, instance=critique)
            if edit_critique_form.is_valid():
                edit_critique_form.save()
                return redirect('home')
        if 'delete_critique' in request.POST:
            delete_critique_form = forms.CritiqueFormDelete(request.POST)
            if delete_critique_form.is_valid():
                critique.delete()
                return redirect('home')
    context = {
        'edit_critique_form': edit_critique_form,
        'delete_critique_form': delete_critique_form
    }
    return render(request,'blog/edit_critique.html', context)
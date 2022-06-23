from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from . import forms, models


@login_required
def follow_users(request):
    form = forms.FollowUsersForm()
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    # abonnements = models.UserFollows.objects.followed_user.all()
    # abonnes = models.UserFollows.objects.user.all()
    return render(request, 'subscription/follow_users_form.html',
                  context={'form': form})  # 'abonnements': abonnements, 'abonnés': abonnes})

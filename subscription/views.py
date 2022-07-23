<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from authentication.models import User

from . import forms
=======
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from . import forms, models
>>>>>>> f3dc60dde3dd6edbe4a2fcebb4307cc0156b0a30


@login_required
def follow_users(request):
<<<<<<< HEAD
    search_form = forms.SearchUser()
    searched_user_resp = ""
    requested_user = request.user
    # search
    searched_user_resp_btn = ''

    # get follows and followers
    user_follows = requested_user.follows.all()
    user_followers = requested_user.followed_by.all()

    group_follows_users = {}
    for user in user_follows:
        follow_form = forms.FollowUserButton(initial={'user_to_follow': user.id})
        group_follows_users[user] = follow_form

    if request.method == 'POST':

        # search form
        if request.POST.get('search_user_id'):
            search_form = forms.SearchUser(request.POST)
            if search_form.is_valid():
                query = search_form.cleaned_data['search']
                searched_user = User.objects.filter(username__icontains=query).first()
                if searched_user:
                    searched_user_resp = searched_user
                    searched_user_resp_btn = forms.FollowUserButton(initial={'user_to_follow': searched_user.id})

        # follow / unfollow button
        else:
            follow_form = forms.FollowUserButton(request.POST)
            if follow_form.is_valid():
                user_to_follow = get_object_or_404(User, id=follow_form.cleaned_data['user_to_follow'])
                if request.user.follows.filter(id=user_to_follow.id).exists():
                    request.user.follows.remove(user_to_follow)
                    user_to_follow.followed_by.remove(request.user)
                    return redirect('follow_users')
                else:
                    request.user.follows.add(user_to_follow)
                    user_to_follow.followed_by.add(request.user)
                    return redirect('follow_users')

    context = {
        'search_form': search_form,
        'searched_user_resp': searched_user_resp,
        'searched_user_btn': searched_user_resp_btn,
        'requested_user': requested_user,
        'user_follows': user_follows,
        'group_user_follows': group_follows_users,
        'user_followers': user_followers
    }
    return render(
        request,
        'subscription/follow_users_form.html',
        context
    )
=======
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
>>>>>>> f3dc60dde3dd6edbe4a2fcebb4307cc0156b0a30

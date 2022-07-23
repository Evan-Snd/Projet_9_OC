"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import authentication.views
import blog.views
import subscription.views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth app
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),

    # Blog app
    path('home/', blog.views.home, name='home'),
<<<<<<< HEAD
    path('my-posts/<str:user>/', blog.views.my_post, name='my_posts'),
    path('create-ticket/', blog.views.create_ticket, name='create_ticket'),
    path('edit_ticket/<int:ticket_id>/', blog.views.edit_ticket, name="edit_ticket"),
    path('create-critique/<int:ticket_id>/', blog.views.create_critique, name='create_critique'),
    path('create-critique/', blog.views.create_ticket_and_critique, name='create_ticket_and_critique'),
=======
    path('create-ticket/', blog.views.create_ticket, name='create_ticket'),
    path('edit_ticket/<int:ticket_id>/', blog.views.edit_ticket, name="edit_ticket"),
    path('create-critique/<int:ticket_id>/', blog.views.create_critique, name='create_critique'),
    path('create-critique', blog.views.create_ticket_and_critique, name='create_ticket_and_critique'),
>>>>>>> f3dc60dde3dd6edbe4a2fcebb4307cc0156b0a30
    path('edit_critique/<int:critique_id>/', blog.views.edit_critique, name="edit_critique"),

    # Subscription app
    path('follow-users/', subscription.views.follow_users, name='follow_users'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

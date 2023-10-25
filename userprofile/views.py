from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import SignupForm
from .models import Userprofile
from team.models import Team, Plan


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            # plan = Plan.objects.get(pk=1)
            team = Team.objects.create(
                name='The team name', created_by=user)
            team.members.add(user)
            team.save()

            userprofile = Userprofile.objects.create(
                user=user, active_team=team)

            return redirect('/login/')

    form = SignupForm()
    return render(request, 'userprofile/signup.html', {
        'form': form
    })


def login(request):
    return render(request, 'userprofile/login.html')


@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')

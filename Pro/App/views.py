from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from .forms import SignUpForm ,ProfileForm
from .models import  Profile
from django.contrib.auth import authenticate, login

from django.http import HttpResponse

# home page
def home(request):
    return render(request, 'App/home.html')

# intro page
def intro(request):
    return render(request, 'App/intro.html')

# syntax page
def syntax(request):
    return render(request, 'App/quiz.html')

def datatypes(request):
    return render(request, 'App/datatypes.html')

def controlflow(request):
    return render(request, 'App/contorlflow.html')

def functions(request):
    return render(request, 'App/functions.html')

def modules(request):
    return render(request, 'App/modules.html')

def loop(request):
    return render(request, 'App/loop.html')

def filehandling(request):
    return render(request, 'App/filehandling.html')

# to redirect the page to another page
def change_path(request, new_path):
    return redirect(new_path)

# warning for login_required
@login_required
def other_page(request):
    # Your view logic for the other page goes here
    return render(request, 'App/home.html')

# singup page and its functionality
def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
       
            # Log the user in after signing up
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        user_form = SignUpForm()
       
    return render(request, 'App/signup.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                user.save()
                return redirect('profile')
            else:
                return HttpResponse("Your account is inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'App/login.html', {})


@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get_or_create(user=user)[0]
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileForm(instance=profile)
    return render(request, 'App/profile.html', {'profile': profile, 'profile_form': profile_form})

def user_logout(request):
    logout(request)
    return redirect('login')
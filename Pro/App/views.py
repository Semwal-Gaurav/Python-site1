from django.conf import settings

if 'mysql' in settings.DATABASES['default']['ENGINE']:
    DATABASE_ENGINE = 'MySQL'
    # print("Using MySQL database.")
else:
    DATABASE_ENGINE = 'Other'
    # print("Not using MySQL database.")



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForms, UserLogins
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import UserRegisterForm, UserLogin


# to redirect the page to another page
def change_path(request, new_path):
    return redirect(new_path)

# warning for login_required
@login_required
def other_page(request):
    # Your view logic for the other page goes here
    return render(request, 'App/home.html')

# home page
def home(request):
    return render(request, 'App/home.html')
# intro page
def intro(request):
    return render(request, 'App/intro.html')

# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect('login')

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

# singup page and its functionality
def register(request):
    if request.method == 'POST':
        form = UserRegisterForms(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['confirmpassword']:
                form.save()
                return redirect('login')  # Redirect to the login page
            else:
                messages.warning(request, 'Passwords do not match')
    else:
        form = UserRegisterForms()
    template_name = 'App/signup.html'
    context = {'form': form}
    return render(request, template_name, context)


def user_login(request):
    if request.method == 'POST':
        form = UserLogins(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = UserRegisterForm.objects.get(username=username)
               
            except UserRegisterForm.DoesNotExist:
                messages.error(request, 'Invalid username or password')
                return render(request, 'App/login.html', {'form': form})


            if user.password == password:
              
                request.session['user_id'] = user.id
                form.save()
                return redirect('intro') 
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = UserLogins()
    return render(request, 'App/login.html', {'form': form})



def profile(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = UserRegisterForm.objects.get(id=user_id)
            return render(request, 'App/profile.html', {'user': user})
        except UserRegisterForm.DoesNotExist:
            pass
    return redirect('/login/')




def user_logout(request):
    logout(request)
    return redirect('login')

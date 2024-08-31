from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import Register





# Create your views here.
@login_required
def index(request):

# Render the HTML template index.html with the data in the context variable.
   return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = User(username = form.cleaned_data['username'], email=form.cleaned_data['email'],)
            user.set_password(form.cleaned_data['password'])
            user.save()
           
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')  # Redirect to a home page after registration
    else:
        form = Register()

    return render(request, 'register.html', {'form': form})


   
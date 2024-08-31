from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):

# Render the HTML template index.html with the data in the context variable.
   return render(request, 'index.html')
   
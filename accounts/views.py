from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.http import Http404, HttpResponseBadRequest

from accounts.models import CustomUser
from accounts.forms import RegisterForm, LoginForm

# Create your views here.
@csrf_exempt
def register(request):
    if request.method == 'GET':
        form = RegisterForm
        return render(request, 'register.html', { 'form': form })

    if request.method == 'POST':
        # TODO: impl
        pass

    return HttpResponseBadRequest

@csrf_exempt
def login(request):
    if request.method == 'GET':
        form = LoginForm
        return render(request, 'login.html', { 'form': form })
    
    if request.method == 'POST':
        # TODO: impl
        pass

    return HttpResponseBadRequest

@csrf_exempt
@login_required(login_url='/account/login')
def logout(request):
    if request.method == 'GET':
        # TODO: impl
        pass
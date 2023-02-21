from django.views import View
from accounts.models import CustomUser
from django.shortcuts import render, redirect
from allauth.account import views
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from urllib import request
from accounts.forms import SignupUserForm
from django.contrib.auth import login,logout

class LoginView(views.LoginView):
  template_name = 'accounts/login.html'

class SignupView(views.SignupView):
  template_name = 'accounts/signup.html'
  form_class = SignupUserForm

def LogoutView(request):
    logout(request)
    return redirect('account_signin')

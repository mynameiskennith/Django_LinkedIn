from django.shortcuts import render,redirect
from datetime import datetime
#from django.contrib.auth.decorators import login_required
#above is replaced by
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today':datetime.today()}

# This program code is replced by the class view which can produce the same page similarly
# def home(request):
#     return render(request,'home/welcome.html',{'today':datetime.today()})

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url='/admin'

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request,'home/authorized.html',{})
    
class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceV(LogoutView):
    pass
    #template_name = 'home/logout.html'

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)
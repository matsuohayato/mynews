from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .forms import CustomUserCreationForm
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request, 'accounts/profile.html')
class loginView(TemplateView):
    template_name = 'login.html'

class logoutView(TemplateView):
    template_name = 'logout.html'

class SignUpSuccessView(View):
    template_name = 'signup_success.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:signup_success')
    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)
    
class SignUpSuccessView(TemplateView):
    template_name = 'signup_success.html'
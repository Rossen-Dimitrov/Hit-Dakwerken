from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth import forms as auth_form
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import login as auth_login
from django.views.generic import TemplateView

from hit_dakwerken.accounts.forms import AppUserRegisterForm

# from hit_dakwerken.accounts.models import AppUser
# from hit_dakwerken.settings import LOGIN_URL
#
#
UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    # model = AppUser
    form_class = AppUserRegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('register')

    #     success_url = LOGIN_URL
    def form_valid(self, form):
        result = super().form_valid(form)

        auth_login(self.request, self.object)

        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'account/login.html'
    # model = AppUser
    # form_class = AppUserRegisterForm


class DetailsUserView(auth_mixins.LoginRequiredMixin, views.DetailView):
    template_name = 'account/user_details.html'
    model = UserModel


class LogoutsUserView(views.View):
    def get(self, request):
        return render(request, 'account/logout.html')


class LogoutUserView(auth_views.LogoutView):
    pass

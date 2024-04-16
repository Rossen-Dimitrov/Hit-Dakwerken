from django.contrib.auth import views as auth_views, get_user_model, logout
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from hit_dakwerken.accounts.forms import AppUserRegisterForm, AppUserEditForm
from hit_dakwerken.accounts.models import AppUser, AppUserProfile
from django.contrib.auth import login as auth_login

from hit_dakwerken.query.models import Query

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    form_class = AppUserRegisterForm
    template_name = 'accounts/profile-register.html'

    def form_valid(self, form):

        user = form.save()

        AppUserProfile.objects.create(user=user)

        auth_login(self.request, user)

        return super().form_valid(form)

    def get_success_url(self):

        return reverse("profile details", kwargs={"pk": self.request.user.pk})


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    model = AppUser

    def get_success_url(self):
        # Redirect to the profile details page after successful login
        return reverse("profile details", kwargs={"pk": self.request.user.pk})


class DetailsUserView(auth_mixins.LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/profile-details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queries = Query.objects.filter(user=self.request.user)
        context['queries'] = queries

        return context


class EditUserView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = UserModel
    form_class = AppUserEditForm
    template_name = 'accounts/profile-edit.html'

    def get_object(self, queryset=None):
        return self.request.user.appuserprofile

    def get_success_url(self):
        return reverse("profile details", kwargs={
            "pk": self.object.pk,
        })


class DeleteUserView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('home')


def logout_view(request):
    logout(request)
    return redirect('home')

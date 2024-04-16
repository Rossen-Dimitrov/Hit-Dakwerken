from django.utils import timezone

from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from hit_dakwerken.query import models
from hit_dakwerken.query.forms import QueryCreateForm
from hit_dakwerken.settings import HOME_REDIRECT_URL


class QueryCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'query/query-add.html'
    form_class = QueryCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.published_on = timezone.now()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('query request details', kwargs={'pk': self.object.pk})

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form


class QueryDetailsView(views.DetailView):
    model = models.Query
    template_name = 'query/query-details.html'

    def get_success_url(self):
        return reverse('photo details', kwargs={
            'pk': self.object.pk
        })


class QueryEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = models.Query
    template_name = 'query/query-edit.html'
    success_url = HOME_REDIRECT_URL
    fields = ['content', 'image']


class QueryDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = models.Query
    template_name = 'query/query-delete.html'
    success_url = HOME_REDIRECT_URL

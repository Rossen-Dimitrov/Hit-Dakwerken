from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from hit_dakwerken.article.forms import ArticleCreateForm
from hit_dakwerken.article import models
from hit_dakwerken.settings import HOME_REDIRECT_URL


class ArticleCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model_form = ArticleCreateForm
    model = models.Article
    template_name = 'articles/create_article.html'
    success_url = reverse_lazy('home')
    fields = ['title', 'content', 'image']


class ArticleDetailsView(views.DetailView):
    model = models.Article
    template_name = 'articles/details_article.html'


class ArticleEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = models.Article
    template_name = 'articles/edit_article.html'
    success_url = HOME_REDIRECT_URL
    fields = ['title', 'content', 'image']


class ArticleDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = models.Article
    template_name = 'articles/article_confirm_delete.html'
    success_url = HOME_REDIRECT_URL
from django.shortcuts import render
from django.views import generic as views

from hit_dakwerken.article.models import Article


class HomePageView(views.ListView):
    model = Article
    template_name = 'common/home.html'


# def about_us(request):
#     return render(request, 'common/about_us.html')
#
#
# def contacts(request):
#     return render(request, 'common/contacts.html')

from django.shortcuts import render


def home_page(request):
    return render(request, 'common/home_page.html')


def projects(request):
    return render(request, 'common/projects.html')


def about_us(request):
    return render(request, 'common/about_us.html')


def contacts(request):
    return render(request, 'common/contacts.html')


def login(request):
    return render(request, 'common/login.html')

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from .models import *

menu = [{'title': "О сайте", 'url_name': "about"},
        {'title': "Добавиление статьи", 'url_name': "addpage"},
        {'title': "Обратная связь", 'url_name': "contact"},
        {'title': "Войти", 'url_name': "login"}
]


def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': "Главная страница",
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse("<h1>Добавление статьи</>")

def contact(request):
    return HttpResponse("<h1>Обратная связь</>")

def login(request):
    return HttpResponse("<h1>Войти</>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context=context)

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': "Отображение по рубрикам",
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', context=context)


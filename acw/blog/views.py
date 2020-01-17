from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import *
from django.utils import timezone
from datetime import datetime, timedelta, date


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Create your views here.


def model_test(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'blog/model-test.html', context)


def article_list(request, tag):
    if tag == '0':
        articles = get_list_or_404(Article)
    else:
        articles = get_list_or_404(Article, tags__name__in=[tag], publish=True)

    context = {
        'tag': tag,
        'articles': articles,
    }
    return render(request, 'blog/article-list.html', context)


def index(request):
    articles = get_list_or_404(Article)[0:6]
    context = {
        'articles': articles,
    }
    return render(request, 'blog/index.html', context)


def article(request, pk):
    try:
        # This is main view work
        article = get_object_or_404(Article, pk=pk, publish=True)
        context = {
            'article': article,
        }
        return render(request, 'blog/article.html', context)
    finally:
        # Hitcount update after return
        ip = get_client_ip(request)
        hit_logs = ArticleHitCount.objects.filter(
            ip=ip,
            article=article,
            date__lte=date.today(),
            date__gte=date.today()
        )
        if hit_logs.count() == 0:
            hits = ArticleHitCount(ip=ip, article=article)
            hits.save()
            article.hit_count += 1
            article.save()
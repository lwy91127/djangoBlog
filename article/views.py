from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    post_list = Article.objects.all()
    post_list = get_page(request,post_list,2)
    return render(request,'home.html',{'post_list':post_list})

def detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

def get_page(request, post_list, num=4):
    paginator = Paginator(post_list, num)
    try:
        page = request.GET.get('page')
        post_list = paginator.page(page)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    return post_list
# Create your views here.

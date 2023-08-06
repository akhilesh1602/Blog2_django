from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from main import models
from main.models import Article
# Create your views here.

def home(request):
    articles = Article.objects.order_by("-created_date")[0:5]
    data = {
        "articles" : articles,
    }
    return render(request, "home.html", data)


def articles(request):
    
    articles = Article.objects.order_by("-created_date")
    
    data = {
        "articles":articles,
        
    }
    return render(request, "articles.html", data)

def create_article(request):
    option = Article.categories_option
    data = {
        "option" : option,
    }

    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']

        Article.objects.create(title = title, description = description)

    return render(request, "create_article.html", data)

def get_article(request,pk):
    article = get_object_or_404(Article, pk=pk)
    data = {
        "article" : article ,
    }
    return render(request, "get_article.html", data)

def search(request):
    if request.method == "POST":
        query = request.POST["search_query"]
        posts = Article.objects.filter(title__contains=query)
        data = {
            "posts" : posts,
        }
        return render(request, "search.html", data)
    else:
        HttpResponse("Title not found")
    return render(request, "home.html")

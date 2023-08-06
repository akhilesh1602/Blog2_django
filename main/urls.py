from django.urls import path
from main import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("articles", views.articles, name="articles"),
    path("create_article", views.create_article, name = "create_article"),
    path("get_article/<int:pk>", views.get_article, name="get_article"),
    path("search", views.search, name = "search"),

]
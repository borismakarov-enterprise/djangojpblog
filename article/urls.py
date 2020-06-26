from django.contrib import admin
from django.urls import path
from article import views

urlpatterns = [
    path("dashboard/",views.dashboard,name="dashboard"),
    path("addart/",views.addart,name="addart"),
    path("article/<int:id>",views.detail,name = "detail"),
    path("update/<int:id>",views.updateArticle,name = "update"),
    path("delete/<int:id>",views.deleteArticle,name = "delete"),
    path("",views.articles,name = "article"),
    path("comment/<int:id>",views.addComment,name = "comment")
]

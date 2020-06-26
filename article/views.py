from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.contrib import messages
from article.models import Article,Comment
from article.forms import ArticleForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    
    return render(request,"index.xhtml")

def about(request):
    return render(request,"about.xhtml")

def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    
    return render(request,"dashboard.xhtml",{"articles":articles})

@login_required(login_url = "login")
def addart(request):
    from article.forms import ArticleForm
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarı ile oluşturuldu.")
        return redirect("dashboard")
    
    context = {
        "form" : form
    }
    return render(request,"addart.xhtml",context)

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    
    comments = article.comments.all()
    return render(request,"detail.xhtml",{"article":article,"comments":comments})

@login_required(login_url = "login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarı ile Güncellendi.")
        return redirect("dashboard")

    
    return render(request,"update.xhtml",{"form":form})

@login_required(login_url = "login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)

    article.delete()

    messages.success(request,"Makale başarı ile silindi")

    return redirect("dashboard")


def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.xhtml",{"articles":articles})

    articles = Article.objects.all()
    return render(request,"articles.xhtml",{"articles":articles})

def addComment(request,id):
    article = get_object_or_404(Article,id=id)

    if request.method == "POST":
        comment_author = request.user
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = comment_author)
        
        
        newComment.comment_content = comment_content
        
        newComment.article = article

        newComment.save()
    
    return redirect(reverse("detail",kwargs={"id":id}))



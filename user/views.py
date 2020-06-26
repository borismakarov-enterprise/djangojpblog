from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    """form = RegisterForm(request.POST or None)
    if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.success(request,"Başarı ile kayıt oldunuz.")
            return redirect("index")
    context = {
        "form" : form
    }
    messages.error(request,"Parolalar uyuşmuyor.")
    return render(request,"register.xhtml",context)"""
    
    
    
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.add_message(request,messages.SUCCESS,"Başarı ile kayıt oldunuz..")
            return redirect("index")
        
        else:
            form = RegisterForm()
            context = {
                "form" : form
            }
            messages.warning(request,"Parolalar uyuşmuyor.")
            return render(request,"register.xhtml",context)

            
    else:
        form = RegisterForm()
        context = {
            "form" : form
        }
        return render(request,"register.xhtml",context)

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password=password)
        if user is None:
            messages.info(request,"Kullanıcı adı veya parola hatalı")
            return render(request,"login.xhtml",context)

        messages.success(request,"Başarı ile  giriş yaptınız...")
        login(request,user)
        return redirect("index")
    return render(request,"login.xhtml",context)

@login_required(login_url = "login")
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarı ile çıkış yaptınız.")
    return redirect("index")

@login_required(login_url = "login")
def profile(request,id):
    user = User.objects.filter(id = id).first()
    return render(request,"profile.xhtml",{"user":user})
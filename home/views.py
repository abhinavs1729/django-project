from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import login,blogss
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("this is about")

def signup(request):
    user_name = "sn"
    pass_word = "io"
    if request.method == "POST":
        user_name = request.POST.get('username');
        pass_word = request.POST.get('password');
        new_user = login(username = user_name,password = pass_word,date = datetime.now());
        new_user.save();
        user = User.objects.create_user(user_name, "", pass_word);
        user.save();
        messages.success(request,"Account Succesfully Created")
    return render(request,'signup.html')
def loginuser(request):
    if request.method == "POST":
        user_name = request.POST.get('username');
        pass_word = request.POST.get('password');
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,"login.html")


    return render(request,"login.html")

def blog(request):
    blog_list = blogss.objects.all();
    return render(request,"blogs.html",{'blog_list':blog_list});

def create_blog(request):
    if request.method == "POST":
        title1 = request.POST.get('username');
        post1 = request.POST.get('subject');
        new_post = blogss(Title = title1 , Content =post1)
        new_post.save();
        print(post1,title1)
    return render(request, "create_blog.html")
import email
from email import message
from urllib import response
import django
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post,Category
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    posts = Post.objects.all()[::-1]
    cats = Category.objects.all()
    data = {
        'posts':posts,
        'cats':cats
    }
    return render(request,'index.html',data)

def post(request, url):
    post = Post.objects.get(url = url)
    cats = Category.objects.all()

    return render(request, 'posts.html',{'post': post, 'cats': cats})

def category(request,url):
    cat = Category.objects.get(url = url)
    cats = Category.objects.all()
    posts = Post.objects.filter(cat=cat)
    return render(request,'category.html',{'cat':cat, 'posts':posts,'cats':cats})

def blogs(request):
    all_post = Post.objects.all()
    cats = Category.objects.all()
    return render(request,'blogs.html',{'all_post':all_post,'cats':cats})

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'account is created for ' + user)
            return redirect('login')

    context = {'form' : form}
    return render(request,'signup.html',context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('main')
        else:
            messages.info(request,'username or password is incorrect...')

    return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def search(request):
    query = request.GET['query']
    if len(query) > 78 or len(query) == 0:
        allpost = []
    else:
        allpostTitle = Post.objects.filter(title__icontains = query)
        allpostContent = Post.objects.filter(content__icontains = query)
        allpost = allpostTitle.union(allpostContent)

    data = {
        'posts':allpost,
        'query':query,
    }
    return render(request,'search.html',data)
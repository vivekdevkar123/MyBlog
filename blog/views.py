import email
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post,Category
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def home(request):
    posts = Post.objects.all()[:11]
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
    posts = Post.objects.filter(cat=cat)
    return render(request,'category.html',{'cat':cat, 'posts':posts})


def blogs(request):
    all_post = Post.objects.all()
    return render(request,'blogs.html',{'all_post':all_post})
    
def login(request):
        if request.method== 'POST':
            email = request.POST['email']
            password = request.POST['password']

            user = auth.authenticate(email = email,password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                messages.info(request,'invalid credentials')
                return redirect('login')
        
        else:
            return render(request,'login.html')



def signup(request):

    if (request.method == 'POST'):

        email = request.POST('email')
        password1 = request.POST('password1')
        password2 = request.POST('password2')

        if(password1 == password2):
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            else:   
                user = User.objects.create_user(password=password1, email=email)
                user.save();
                print('user created')
                return redirect('login')
            
        else:
            messages.info(request,'password not matching..')    
            return redirect('signup')
    else:
        return render(request,'signup.html')


'''

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'register.html')

'''
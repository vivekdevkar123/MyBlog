from django.urls import path,include
from .views import home,post,category,blogs,login



urlpatterns = [
    path('',home),
    path('blogs/',blogs),
    path('login',login),
    path('blog/<slug:url>/', post),
    path('category/<slug:url>/',category),
]
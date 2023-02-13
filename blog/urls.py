from django.urls import path,include
from .views import home,post,category,blogs,signup,loginPage,logoutUser,search,custom_404
from django.conf.urls import handler404

handler404 = custom_404

urlpatterns = [
    path('',home,name='home'),
    path('blogs/',blogs),
    path('blog/<slug:url>/', post),
    path('category/<slug:url>/',category),
    path('signup',signup),
    path('login',loginPage, name='login'),
    path('logout/',logoutUser,name='logout'),
    path('search/',search,name='search'),
]
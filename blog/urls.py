from django.urls import path,include
from .views import home,post,category,blogs



urlpatterns = [
    path('',home),
    path('blogs/',blogs),
    path('blog/<slug:url>/', post),
    path('category/<slug:url>/',category),
]
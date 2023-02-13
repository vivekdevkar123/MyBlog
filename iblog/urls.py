from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf.urls import handler404



urlpatterns = [
    path('vivek-admin-pannel/', admin.site.urls),
    path('', include('blog.urls')),
    path('tinymce/', include('tinymce.urls')),
    
] 

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


handler404 = 'blog.views.custom_404'
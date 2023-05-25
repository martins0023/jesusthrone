"""jtweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views as home_views
from pages import views as pages_views
from blog import views as blog_views
from blog.views import BlogListView, BlogDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    
    #about page
    path('about/', pages_views.about, name='about'),
    
    #project page
    path('projects/', pages_views.project, name='project'),
    
    #blog pages
    #path('blog/', blog_views.blog, name='blog'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    
    #contact page
    path('contact/', pages_views.contact, name='contact'),
    
    #online giving page
    path('onlinegiving/', pages_views.onlinegiving, name='onlinegiving'),
    path('pastordesk/', pages_views.pastordesk, name='pastordesk'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
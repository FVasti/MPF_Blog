"""
URL configuration for mpf_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from pages.views import AboutView

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # si vas a permitir subir imágenes con ckeditor
    path('pages/', include('pages.urls')),
    
    path('messages/', include('messages_app.urls')),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Nuestra vista personalizada de signup
    path('accounts/', include('django.contrib.auth.urls')),  # login, logout, etc.
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', include('pages.urls')), # las URLs de los posts
    path('accounts/', include('accounts.urls')),

    path('messages_app/', include('messages_app.urls')),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


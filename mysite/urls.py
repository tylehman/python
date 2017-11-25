"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from user_account import views as user_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('about.urls')),
    url(r'^jobs/', include('jobs.urls')),
    url(r'^find_job/', include('find_job.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^user_account/', include('user_account.urls')),
    url(r'^home1/', user_views.home1, name='home1'),
    url(r'^user_account/login/', auth_views.login, {'template_name' : 'user_account/login.html'} ,name='login'),
    url(r'^logout/', auth_views.logout, {'next_page' : 'login'}, name='logout'),
]

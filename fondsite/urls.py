"""DIFsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from DIF import views as site_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url('admin/', admin.site.urls),
	url(r'^$', site_views.base, name='base'),
	url(r'wallet/$', site_views.wallet, name='wallet'),
	# Registration URLs
	url(r'^register/$', site_views.register, name='register'),
	url(r'^register/complete/$', site_views.registration_complete, name='registration_complete'),
	# Auth-related URLs:
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^loggedin/$', site_views.loggedin, name='loggedin'),
	url(r'^logout/$', auth_views.logout, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
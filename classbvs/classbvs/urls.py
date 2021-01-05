"""classbvs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from class1 import views
from class2 import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/', views.Hello.as_view()),
    path('classt/', views.HelloT.as_view()),
    url(r'^$', v.BookListView.as_view(), name='books'),
    url(r'^(?P<pk>\d+)/$', v.BookDetail.as_view(), name='detail'),
    path('create/', v.BookCreate.as_view()),
    url(r'^update/(?P<pk>\d+)/$', v.BookUpdate.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', v.BookDelete.as_view()),


]

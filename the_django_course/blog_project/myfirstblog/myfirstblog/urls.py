"""myfirstblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from myfirstblog import views
from django.urls import re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls), # for admin site
    path('about/',views.AboutView.as_view(),name='about'), # for about page
    re_path('post/updated/',views.post_detail,name='post_detail'),
    re_path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    #re_path('post/updated/',views.PostUpdateView.as_view(),name='post_edit'),
    # re_path('post/(?P<pk>\d+)/remove/',views.PostDeleteView.as_view(),name='post_remove'),
    # re_path('drafts/$',views.DraftListView.as_view(),name='post_draft_list'),
    # re_path('post/(?P<pk>\d+)/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    # re_path('comment/(?P<pk>\d+)/approve/',views.comment_approve,name='comment_approve'),
    # re_path('comment/(?P<pk>\d+)/remove/',views.comment_removed,name='comment_removed'),
    # re_path('post/(?P<pk>\d+)/publish/',views.post_publish,name='post_publish'),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path( r'^login/$',auth_views.LoginView.as_view(template_name="login.html"), name="login"), #for login page
    re_path( r'^logout/$',auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),

]

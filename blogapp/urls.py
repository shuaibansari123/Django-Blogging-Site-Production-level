from django.contrib import admin
from django.urls import path , re_path , include
from .import views

urlpatterns = [
    
    path('' , views.home , name='home_path_blogapp'),
    
    path('about-page' , views.about_view , name='about_path_blogapp'),
    path('contact-page' , views.contact_view , name='contact_path_blogapp'),


    path('blog/<int:pk>' , views.blogView , name='blogView_path_blogapp'),
    path('comment_ajax1-page/' , views.comment_ajax1 , name='comment_ajax1'),
    #path('test' , views.test , name='test'),
    #path('add_bio' , views.add_bio , name='add_bio'),
    path('edit_comment_ajax-page' , views.edit_comment_ajax , name="comment_edit_ajax1_path"),
    #likes
    path("like_path_url-page/", views.like_view, name="like_url"),
    #path('like_path_url/<int:pk>/' , views.like_view, name='like_url'),


    #AUTHENTICATING SYSTEM 
    #path('accounts/', include('django.contrib.auth.urls') ), 
    #path('test01/' , views.test01 , name='test01') , 

    path('signup-page' , views.mysignup , name='mysignup'),
    path('login-page' , views.MyLogin, name="my_login_url") , 
    path("logout", views.logout_request, name= "logout"),
    #path("nocobot" , views.index_view , name="nocobot_url") ,


# SOCIAL AUTH
    #path('oauth/', include('social_django.urls', namespace='social') , 



    
]


    
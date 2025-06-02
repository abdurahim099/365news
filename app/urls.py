from django.urls import path
from .views import index,author,blog_single,blog,contact,gallery_single,gallery,life_style,register,sport,technology,login,page_404
from django.views.generic import RedirectView




urlpatterns = [
    path('',RedirectView.as_view(url = 'home')),
    path('home/',index,name='home'),
    path('author/',author,name='author'),
    path('blog_single/',blog_single,name='blog_single'),
    path('blog/',blog,name='blog'),
    path('contact/',contact,name='contact'),
    path('gallery_single/',gallery_single,name='gallery_single'),
    path('gallery/',gallery,name='gallery'),
    path('life_style/',life_style,name='life_style'),
    path('register/',register,name='register'),
    path('sport/',sport,name='sport'),
    path('technology/',technology,name='technology'),
    path('login/',login,name='login'),
    path('404/',page_404,name= "page_404")
    

]

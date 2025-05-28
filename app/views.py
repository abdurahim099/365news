from django.shortcuts import render
from .models import Category, Blog
from utils.views import group_queryset
from django.core.paginator import Paginator

def index(request):
    blogs = Blog.objects.order_by('-id')[:5]
    blogs2 = Blog.objects.all()
    bussiness = Category.custom.get_category('Bussiness')
    sport = Category.custom.get_category('Sport')
    technology = Category.custom.get_category('Technology')
    life_style = Category.custom.get_category('Life Style')
    wheather = Category.custom.get_category('wheather')
    latest_news = Category.custom.get_category('latest_news')
    advertising = Category.custom.get_category('advertising')
    recent_posts = Category.custom.get_category('recent_posts')
    latest_articles = Category.custom.get_category('latest_articles')
    find_us_on_Facebook = Category.custom.get_category('Find_us_on_Facebook')
    get_Even_More = Category.custom.get_category('Get_Even_More')
    latest_reviews = Category.custom.get_category('latest_reviews')
    banner = Category.custom.get_category('banner')
    recent_new = Category.custom.filter(name__in = ["Politics","Technology"])

    gatgets = Category.custom.get_category("Gadgets_and_Technology")

    print(banner)

    gatgets_blog = Blog.objects.filter(category = gatgets)
    
    print(gatgets_blog,'--------------------------------------------------------------------------------------------')
    gatgets_paginator = Paginator(gatgets_blog,3)     
    page_number = request.GET.get('page',1)


    gatgets_by_page = gatgets_paginator.get_page(page_number)
    
    

    travel = Blog.objects.all()
    # print(find_us_on_Facebook)


    context = {
        'blogs': blogs,
        'blogs2': group_queryset(2, blogs2),
        'bussiness': bussiness,
        'sport': sport,
        'technology': technology,
        'life_style': life_style,
        'travel': group_queryset(6,travel),
        'recent_new':recent_new,
        'wheather': wheather,
        'latest_news': latest_news,
        'advertising': advertising,
        'recent_posts': recent_posts,
        'latest_articles': latest_articles,
        'Find_us_on_Facebook': find_us_on_Facebook,
        'get_Even_More': get_Even_More,
        'latest_reviews': latest_reviews,
        'banner': banner,
        "gatgets":gatgets,
        'gatgets_by_page' : gatgets_by_page
        

    }
    return render(request, 'index.html', context)



def blog(request):

    title = request.GET.get("title")
    blogs = Blog.objects.all()

    # if title:
    #     blogs = blogs.filter(title__icontains = title )

    context = {
        'blogs': blogs,
        'title': title
    }
    return render(request,'blog.html',context)

def contact(request):
    return render(request,'contact.html')
def gallery_single(request):
    return render(request,'gallery_single.html')
def gallery(request):
    return render(request,'gallery.html')
def life_style(request):
    return render(request, 'life_style.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def sport(request):
    return render(request,'sport.html')
def technology(request):
    return render(request,'technology.html')
def author(request):
    return render(request,'author.html')
def blog_single(request):
    return render(request,'blog_single.html')

# Create your views here.

def page_404(request):
    return render(request,'404.html')

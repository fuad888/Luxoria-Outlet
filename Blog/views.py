from django.shortcuts import render
from .models import Blogs,BlogCategory, SearchByInline , Blogpage
from accounts.models import MyUser

# Create your views here.

def Blog_page(request):
    Page = Blogpage.objects.first()
    context = {
        'site_banner': Page.image,
        'blog_title': Page.title,
        'blog_categories': BlogCategory.objects.all(),
        'search_by': SearchByInline.objects.all(),
        'blogs': Blogs.objects.all().order_by('-created_at')[:3],
    }
    return render(request, 'blog.html', context)


def blog_details(request, slug):
    Blog = Blogs.objects.get(slug=slug)
    context = {
        'blog': Blog,
        'blogs' : Blogs.objects.all().order_by('-created_at'),
        'blog_categories': BlogCategory.objects.all(),
        'search_by': SearchByInline.objects.all(),
        'User' : MyUser.objects.first(),
        
    }
    return render(request, 'blog-details.html', context=context)
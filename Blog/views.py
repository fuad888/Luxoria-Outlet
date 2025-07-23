from django.shortcuts import render
from .models import Blogs,BlogCategory, SearchByInline , Blogpage
from accounts.models import MyUser
from django.core.paginator import Paginator

# Create your views here.

from django.core.paginator import Paginator
from django.shortcuts import render

def Blog_page(request):
    page = Blogpage.objects.first()
    category = BlogCategory.objects.all()
    blog_list = Blogs.objects.all().order_by('-created_at')

    if "category" in request.GET:
        blog_list = Blogs.objects.filter(categories__slug=request.GET["category"]).order_by('-created_at')

    paginator = Paginator(blog_list, 3)  # Hər səhifədə 3 blog
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    context = {
        'site_banner': page.image,
        'blog_title': page.title,
        'blog_categories': category,
        'search_by': SearchByInline.objects.all(),
        'blogs': blogs,  # ✅ Doğru səhifələnmiş obyekt
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
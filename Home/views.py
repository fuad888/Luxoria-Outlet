from django.shortcuts import render
from .models import Homepage, Banner
from Blog.models import Blogs
from Shop.models import Product, Category

def home(request, *args, **kwargs):
    homepage = Homepage.objects.first()

    context = {
        'hero_image': homepage.hero_image.url if homepage and homepage.hero_image else '',
        'hero_title': homepage.hero_title if homepage else '',
        'hero_subtitle': homepage.hero_subtitle if homepage else '',
        'hero_description': homepage.hero_description if homepage else '',
        'banner_1': Banner.objects.first().image_1.url if Banner.objects.first() and Banner.objects.first().image_1 else '',
        'banner_2': Banner.objects.first().image_2.url if Banner.objects.first() and Banner.objects.first().image_2 else '',
        'blogs': Blogs.objects.all().order_by('-created_at')[:3],
        'categories': Category.objects.all(),
        'products': Product.objects.all().order_by('-created_at')[:8],
    }

    return render(request, 'index.html', context)

def blog_details(request, slug):
    blog = Blogs.objects.get(slug=slug)
    context = {
        'blog': blog,
        'blogs': Blogs.objects.all().order_by('-created_at'),
    }
    return render(request, 'blog-details.html', context=context)


def Search(request):
    query = request.GET.get('query')
    blogs = Blogs.objects.filter(title__icontains=query)
    context = {
        'blogs': blogs,
        'query': query,
    }
    return render(request, 'search.html', context=context)
from django.shortcuts import render
from Shop.models import shoppage as site_banner
from Shop.models import Category, Product

def Shop(request):
    context = {
        'shop_title': site_banner.objects.first().shop_title,
        'shop_banner': site_banner.objects.first().shop_banner,
        'products': Product.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'shop-grid.html', context=context)

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product,
        'related_products': Product.objects.filter(categories__in=product.categories.all()).exclude(id=product.id)[:4],
    }
    return render(request, 'shop-details.html', context=context)
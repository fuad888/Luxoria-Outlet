from django.shortcuts import render
from Shop.models import shoppage as site_banner
from Shop.models import Category, Product, Size, Color
from django.core.paginator import Paginator

def Shop(request):
    product = Product.objects.all()
    color= Color.objects.all()


    if "color" in request.GET.keys():
        product = Product.objects.filter(color__slug=request.GET["color"])
    
    if "category" in request.GET.keys():
        product = Product.objects.filter(categories__slug=request.GET["category"])

    if "size" in request.GET.keys():
        product = Product.objects.filter(size__name=request.GET["size"])

    paginator = Paginator(product, 2)   # Hər səhifədə 12 məhsul
    page_number = request.GET.get('page')
    product = paginator.get_page(page_number)

    context = {
        'shop_title': site_banner.objects.first().shop_title,
        'shop_banner': site_banner.objects.first().shop_banner,
        'products': product,
        'categories': Category.objects.all(),
        'sizes': Size.objects.all(),
        'colors': color,

    }
    return render(request, 'shop-grid.html', context=context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product,
        'related_products': Product.objects.filter(categories__in=product.categories.all()).exclude(id=product.id)[:4],
        'categories': Category.objects.all(),
        'sizes': Size.objects.all(),
        'colors': Color.objects.all(),

    }
    return render(request, 'shop-details.html', context=context)
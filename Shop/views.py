from django.shortcuts import render
from Shop.models import shoppage as site_banner

def Shop(request):
    context = {
        'shop_title': site_banner.objects.first().shop_title,
        'shop_banner': site_banner.objects.first().shop_banner,
    }
    return render(request, 'shop-grid.html', context=context)
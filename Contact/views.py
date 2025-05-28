from django.shortcuts import render, redirect
from Contact.form import SubscribeForm, ContactForm
from django.contrib import messages
from Contact.models import Contact,ContactPage

def contact(request):
    # Query the site_banner once to avoid querying twice
    banner = ContactPage.objects.first()
    context = {
        'contact_title': banner.contact_title,
        'contact_banner': banner.contact_banner,
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Müraciətiniz uğurla göndərildi!')
            return redirect('contact') 
        else:
            messages.error(request, 'Zəhmət olmasa, formu düzgün doldurun!')
            context['form'] = form 
    else:
        form = ContactForm()
        context['form'] = form

    return render(request, 'contact.html', context)

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Uğurla abunə oldunuz!')
            return redirect('home')
        else:
            messages.error(request, 'Siz artıq bizi izləyirisiniz!')
            return redirect('contact')
    else:
        form = SubscribeForm()
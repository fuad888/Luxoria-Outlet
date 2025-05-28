
from .models import Setting
from Contact.form import SubscribeForm

def setting_context(request):
    setting = Setting.objects.first()
    subscribe_form = SubscribeForm()
    
    return {
        'setting_obj': setting,
        'form': subscribe_form
    }

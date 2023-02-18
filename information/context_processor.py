from .models import About_Us

def show_info(request):
    info=About_Us.objects.last()
    return {'info':info}
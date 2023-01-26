from .models import category

def show_category(request):
    categories=category.objects.all()
    return {'categories':categories}
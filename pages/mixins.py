from django.http import Http404
from django.shortcuts import get_object_or_404
class fieldmixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields=['Title','Summary','Price','Author','page_count','cover','Category','seller','Information','exist']
            # if we have author field,top line must has contain author field
            
        elif request.user.is_seller:
            self.fields=['Title','Summary','Price','Author','page_count','cover','Category','Information','exist']
        else:
            raise Http404('you cant see this page')
        return super().dispatch(request, *args, **kwargs)

class superusermixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('you cant see this page')
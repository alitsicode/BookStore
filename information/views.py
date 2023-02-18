from django.shortcuts import render
from .models import About_Us,Contact_Us
from accounts.models import Customeuser
from django.views import generic
from django.utils.translation import gettext_lazy as _

from django.contrib import messages
from django.urls import reverse_lazy


def aboutus(request):
    our_info=About_Us.objects.last()
    users=Customeuser.objects.filter(is_seller=True)
    return render(request, 'information/aboutus.html',context={'us':our_info,'users':users})
# Create your views here.

class ContactUs(generic.CreateView):
    model=Contact_Us
    template_name='information/contactus.html'
    fields=['text']
    success_url=reverse_lazy('book_home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["our_info"] = About_Us.objects.last()
        return context
    
    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.user=self.request.user
        instance.save()
        messages.success(self.request, "your message successfuly send to us",'success')
        return super().form_valid(form)

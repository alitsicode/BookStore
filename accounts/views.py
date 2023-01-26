from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .models import Customeuser
from django.utils.translation import gettext_lazy as _
from .forms import profile_form
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Profile(LoginRequiredMixin,generic.UpdateView):
    model=Customeuser
    template_name='accounts/profile.html'
    form_class=profile_form
    success_url=reverse_lazy('book_home')
    def form_valid(self, form):
        messages.info(self.request,_('your profile successfuly updated'),'info')
    def get_object(self):
        return get_object_or_404(Customeuser,pk=self.request.user.pk)
    def get_form_kwargs(self):
        kwargs=super(Profile,self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs
from django.shortcuts import render,get_object_or_404,redirect
from .models import book,category,BookMark,Like
from accounts.models import Customeuser
from django.views import generic
from django.utils.translation import gettext_lazy as _

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Count,Q,Avg,Sum
from django.utils import timezone
from datetime import timedelta
from .mixins import fieldmixin,superusermixin
# Create your views here.

def Home(request):
    home_book=book.objects.all().order_by('-Created')[:6]
    last_month=timezone.now() - timedelta(days=30)
    topview=book.objects.all().annotate(count=Count('hits',filter=Q(hitsfilter__timecreated__gt=last_month))).order_by('-count','-Created')[:2]
    hot_product=book.objects.filter(exist = 'have').annotate(count=Count('comments',filter=Q(comments__posted__gt=last_month))).order_by('-count','-Created')[:2]
    return render(request, 'pages/home.html',context={'home_book':home_book,'topview':topview,'hot_product':hot_product})

class ListBook(generic.ListView):
    queryset=book.objects.all().order_by('-Created')
    paginate_by=9
    template_name='pages/list.html'
    context_object_name='object_list'

class DetailBook(LoginRequiredMixin,generic.DetailView):
    model=book
    template_name='pages/detail.html'
    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        bookdetail=get_object_or_404(book,pk=pk)
        ip_address=self.request.user.ip_address
        if ip_address not in bookdetail.hits.all():
            bookdetail.hits.add(ip_address)
        context = super().get_context_data(**kwargs)
        context['book'] = bookdetail
        if self.request.user.bookmark.filter(books=bookdetail,user=self.request.user).exists(): #related_name from user to find like or not
            context["besaved"] = True
        else:
            context["besaved"] = False
        if self.request.user.like.filter(books=bookdetail,user=self.request.user).exists(): #related_name from user to find like or not
            context["beliked"] = True
        else:
            context["beliked"] = False
        return context

class CreateBook(LoginRequiredMixin,fieldmixin,generic.CreateView):
    model=book
    template_name='pages/create.html'
    success_url=reverse_lazy('book_list')
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            instance=form.save(commit=False)
            instance.seller=self.request.user
            instance.save()
        messages.success(self.request,_("your product successfuly add"),'success')
        return super().form_valid(form)
class UpdateBook(LoginRequiredMixin,fieldmixin,generic.UpdateView):
    model=book
    template_name='pages/update.html'
    context_object_name='book'
    success_url=reverse_lazy('book_list')
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            instance=form.save(commit=False)
            instance.seller=self.request.user
            instance.save()
        messages.info(self.request,_("your product successfuly add"),'info')
        return super().form_valid(form)

class DeleteBook(LoginRequiredMixin,superusermixin,generic.DeleteView):
    model=book
    template_name='pages/delete.html'
    context_object_name='book'
    success_url=reverse_lazy('book_list')
    def form_valid(self, form):
        messages.error(self.request,_("your product successfuly deleted"),'danger')
        return super().form_valid(form)

class search_book(generic.ListView):
    template_name='pages/list.html'
    paginate_by=9
    def get_queryset(self):
        query=self.request.GET.get("search")
        object_list = book.objects.all().filter(Q(Title__icontains=query) | Q(Summary__icontains=query) | Q(Author__exact=query)) 
        return object_list

class filter_by_price(generic.ListView):
    template_name='pages/list.html'
    paginate_by=9
    def get_queryset(self):
        query1=int(self.request.GET.get("price1"))
        query2=int(self.request.GET.get("price2"))
        if query1 > query2:
            object_list = book.objects.all().filter(Q(Price__range=(query2,query1)))
        else:
            object_list = book.objects.all().filter(Q(Price__range=(query1,query2)))
        return object_list
    
# def book_by_category(request,pk):
#     categorie=get_object_or_404(category,pk=pk)
#     book_category=categorie.books.all()
#     return render(request, 'pages\list.html',context={'object_list':book_category})
    

# def book_by_seller(request,pk):
#     sellers=get_object_or_404(Customeuser,pk=pk)
#     book_seller=sellers.books.all()
#     return render(request,'pages\list.html',context={'object_list':book_seller})

class book_by_category(generic.ListView):
    template_name='pages/list.html'
    paginate_by=9
    model=category
    def get_context_data(self, **kwargs):
        pk=self.kwargs['pk']
        categorie=get_object_or_404(category,pk=pk)
        book_category=categorie.books.all()
        context = super().get_context_data(**kwargs)
        context["object_list"] = book_category
        return context


class book_by_seller(generic.ListView):
    template_name='pages/list.html'
    paginate_by=9
    def get_queryset(self):
        pk=self.kwargs['pk']
        sellers=get_object_or_404(Customeuser,pk=pk)
        object_list=sellers.books.all()
        return object_list
    
    
    

def bookmark_book(request,pk):
    my_book=get_object_or_404(book,pk=pk)
    try:
        save=BookMark.objects.get(books=my_book,user=request.user)
        save.delete()
    except:
        BookMark.objects.create(books=my_book,user=request.user)
    return redirect('book_detail',pk)

def like_book(request,pk):
    my_book=get_object_or_404(book,pk=pk)
    try:
        like=Like.objects.get(books=my_book,user=request.user)
        like.delete()
    except:
        Like.objects.create(books=my_book,user=request.user)
    return redirect('book_detail',pk)

class ShowBookmark(LoginRequiredMixin,generic.ListView):
    model=BookMark
    template_name='pages/bookmark.html'
    paginate_by=9
    context_object_name='bookmarked'

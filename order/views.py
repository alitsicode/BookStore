from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
import json
from .mixins import deletemixin
from django.http import Http404
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
import requests
# Create your views here.
from cart.cart import Cart
from django.views import generic
from .models import Order,OrderItem
from django.urls import reverse_lazy

class UserOrders(LoginRequiredMixin,generic.ListView):
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["cart"] = Cart(self.request)
		return context
	
	def get_queryset(self):
		object_list = Order.objects.filter(user=self.request.user).filter(paid=False) 
		return object_list
	template_name='order/listorder.html'

class DeleteOrder(deletemixin,LoginRequiredMixin,generic.DeleteView):
	model=Order
	template_name='order/deleteorder.html'
	context_object_name='userorder'
	success_url=reverse_lazy('userorders')
	def form_valid(self, form):
		messages.error(self.request,_("your Order successfuly deleted"),'danger')
		return super().form_valid(form)


class OrderDetailView(LoginRequiredMixin, View):

	def get(self, request, order_id):
		order = get_object_or_404(Order, id=order_id)
		if request.user == order.user:
			return render(request, 'order/order.html', {'order':order})
		else:
			return Http404('you cant see people order')


class OrderCreateView(LoginRequiredMixin, View):
	def get(self, request):
		cart = Cart(request)
		order = Order.objects.create(user=request.user)
		for item in cart:
			OrderItem.objects.create(order=order, product=item['product_obj'], price=item['product_obj'].Price, quantity=item['quantity'])
		cart.clear()
		return redirect('order_detail', order.id)



# sand box mode
# MERCHANT = 'ABFGbdhttyifkddfhrBFShggklerigoFJnfI'
# ZP_API_REQUEST = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
# ZP_API_VERIFY = "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
# ZP_API_STARTPAY = "https://sandbox.zarinpal.com/pg/StartPay/{authority}"
# ///////////////////////////////////////////////////////////////////////
MERCHANT = 'ABFGbdhttyifkddfhrBFShggklerigoFJnfI'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"


class OrderPayView(LoginRequiredMixin, View):
	def get(self, request, order_id):
		order = Order.objects.get(id=order_id)
		req_data = {
			"merchant_id": MERCHANT,
			"amount": order.get_total_price(),
			"callback_url": CallbackURL,
			"description": description,
		}
		req_header = {"accept": "application/json","content-type": "application/json'"}
		req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
			req_data), headers=req_header)
		authority = req.json()['data']['authority']
		if len(req.json()['errors']) == 0:
			return redirect(ZP_API_STARTPAY.format(authority=authority))
		else:
			e_code = req.json()['errors']['code']
			e_message = req.json()['errors']['message']
			return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")

class OrderVerifyView(LoginRequiredMixin, View):
	def get(self, request):
		order_id = request.session['order_pay']['order_id']
		order = Order.objects.get(id=int(order_id))
		t_status = request.GET.get('Status')
		t_authority = request.GET['Authority']
		if request.GET.get('Status') == 'OK':
			req_header = {"accept": "application/json",
						  "content-type": "application/json'"}
			req_data = {
				"merchant_id": MERCHANT,
				"amount": order.get_total_price(),
				"authority": t_authority
			}
			req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
			if len(req.json()['errors']) == 0:
				t_status = req.json()['data']['code']
				if t_status == 100:
					order.paid = True
					order.save()
					return HttpResponse('Transaction success.\nRefID: ' + str(
						req.json()['data']['ref_id']
					))
				elif t_status == 101:
					return HttpResponse('Transaction submitted : ' + str(
						req.json()['data']['message']
					))
				else:
					return HttpResponse('Transaction failed.\nStatus: ' + str(
						req.json()['data']['message']
					))
			else:
				e_code = req.json()['errors']['code']
				e_message = req.json()['errors']['message']
				return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
		else:
			return HttpResponse('Transaction failed or canceled by user')


# class OrderPayViewsandbox(LoginRequiredMixin, View):
# 	def get(self, request, order_id):
# 		order = Order.objects.get(id=order_id)
# 		CallbackURL = f'http://127.0.0.1:8000/order/verify_sandbox/{order.id}'
# 		req_data = {
# 			"MerchantID": MERCHANT,
# 			"Amount": order.get_total_price(),
# 			"CallbackURL": CallbackURL,
# 			"Description": description,
# 		}
# 		req_header = {"accept": "application/json","content-type": "application/json'"}
# 		req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
# 			req_data), headers=req_header)
# 		print(req.json())
# 		authority=req.json()['Authority']
# 		if 'errors' or len(req.json()['errors']) == 0:
# 			return redirect(ZP_API_STARTPAY.format(authority=authority),order.id)
# 		else:
# 			return HttpResponse('hi')

# class OrderVerifyViewsandbox(LoginRequiredMixin, View):
# 	def get(self, request,order_id):
# 		order = Order.objects.get(id=order_id)
# 		t_status = request.GET.get('Status')
# 		t_authority = request.GET['Authority']
# 		if request.GET.get('Status') == 'OK':
# 			req_header = {"accept": "application/json",
# 						  "content-type": "application/json'"}
# 			req_data = {
# 				"MerchantID": MERCHANT,
# 				"Amount": order.get_total_price(),
# 				"Authority": t_authority
# 			}
# 			req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
# 			if 'errors' or len(req.json()['errors']) == 0:
# 				t_status = req.json()['Status']
# 				print(t_status)
# 				if t_status == 100:
# 					order.paid = True
# 					order.save()
# 					return HttpResponse('Transaction success.\nRefID: ' + str(
# 						req.json()
# 					))
# 				elif t_status == 101:
# 					return HttpResponse('Transaction submitted : ' + str(
# 						req.json()
# 					))
# 				else:
# 					return HttpResponse('Transaction failed.\nStatus: ' + str(
# 						req.json()
# 					))
# 			else:
# 				return HttpResponse('noooo')
# 		else:
# 			return HttpResponse('Transaction failed or canceled by user')
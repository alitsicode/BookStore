from django.db import models
from accounts.models import Customeuser
from pages.models import book
from django.utils.translation import gettext_lazy as _

# Create your models here.

# models for save user's recieve information
class OrderInfo(models.Model):
	user=models.ForeignKey(Customeuser, verbose_name=_("user"), on_delete=models.CASCADE,related_name='orderinfo')
	name=models.CharField(_("firstname"), max_length=50)
	last_name=models.CharField(_("lastname"), max_length=50)
	address=models.CharField(_("address"), max_length=400)
	phone_number=models.CharField(_("phone"), max_length=11)
	postal_code=models.CharField(_("postal_code"), max_length=10)
	creted=models.DateTimeField(_("created"), auto_now_add=True)

	def __str__(self):
		return self.user
	

# models to save user's orders
class Order(models.Model):
	user = models.ForeignKey(Customeuser, on_delete=models.CASCADE, related_name='orders')
	info=models.ForeignKey(OrderInfo, verbose_name=_("info"), on_delete=models.CASCADE,related_name='order')
	paid = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('paid', '-updated')

	def __str__(self):
		return f'{self.user} - {str(self.id)}'

	def get_total_price(self):
		total = sum(item.get_cost() for item in self.items.all())
		return total

# models to save order's each items
class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
	product = models.ForeignKey(book, on_delete=models.CASCADE)
	price = models.IntegerField()
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return str(self.id)

	def get_cost(self):
		return self.price * self.quantity
from django.db import models
from accounts.models import Customeuser
from pages.models import book
# Create your models here.

class Order(models.Model):
	user = models.ForeignKey(Customeuser, on_delete=models.CASCADE, related_name='orders')
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


class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
	product = models.ForeignKey(book, on_delete=models.CASCADE)
	price = models.IntegerField()
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return str(self.id)

	def get_cost(self):
		return self.price * self.quantity
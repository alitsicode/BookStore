from django.contrib import admin
from .models import Order, OrderItem,OrderInfo
# Register your models here.
class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'updated','info', 'paid')
	list_filter = ('paid',)
	inlines = (OrderItemInline,)

@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
	list_display = ('user','name','last_name','address','phone_number','postal_code')
from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.

class OderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    raw_id_fields = ['product']


@admin.register(Order)
class OderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'address', 'postal_code', 'province', 'city',
                    'created', 'updated', 'paid']
    list_filter = ['created', 'updated', 'paid']
    inlines = [OderItemInline]

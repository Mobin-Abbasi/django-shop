from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product

@receiver(pre_save, sender=Product)
def calculate_new_price(sender, instance, **kwargs):
	percent_price = (instance.price / 100) * instance.off
	instance.new_price = instance.price - percent_price
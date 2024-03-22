from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from django.http import JsonResponse
# -----------------------test-----------------------
# from kavenegar import *


# Create your views here.


@require_POST
def add_to_cart(request, product_id):
    try:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product)
        context = {
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
        }

        # -----------------------test-----------------------

        # try:
        #     api = KavenegarAPI('49397957535136575A7A66484935584359464A5136726D574630496D744D4B4B707A6B7751506A433378303D')
        #     params = {
        #         'sender': '10008663',  # optional
        #         'receptor': '09214018144',  # multiple mobile number, split by comma
        #         'message': f'محصول {str(product)} به سبد خرید شما اضافه شد',
        #     }
        #     response = api.sms_send(params)
        #     print(response)
        # except APIException as e:
        #     print(e)
        # except HTTPException as e:
        #     print(e)

        # -----------------------\test-----------------------

        return JsonResponse(context)
    except:
        return JsonResponse({"error": "Invalid request."})


def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'cart/detail.html', context)


@require_POST
def update_quantity(request):
    item_id = request.POST.get('item_id')
    action = request.POST.get('action')
    try:
        product = get_object_or_404(Product, id=item_id)
        cart = Cart(request)
        if action == 'add':
            cart.add(product)
        elif action == 'decrease':
            cart.decrease(product)
        context = {
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
            'quantity': cart.cart[item_id]['quantity'],
            'total': cart.cart[item_id]['quantity'] * cart.cart[item_id]['price'],
            'final_price': cart.get_final_price(),
            'success': True,
        }
        return JsonResponse(context)
    except:
        return JsonResponse({'success': False, 'error': 'item not found'})


@require_POST
def remove_item(request):
    item_id = request.POST.get('item_id')
    try:
        product = get_object_or_404(Product, id=item_id)
        cart = Cart(request)
        cart.remove(product)
        context = {
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
            'final_price': cart.get_final_price(),
            'success': True,
        }
        return JsonResponse(context)
    except:
        return JsonResponse({'success': False, 'error': 'item not found'})
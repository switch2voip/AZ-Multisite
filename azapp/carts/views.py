from allauth.socialaccount.providers import stripe
from django.shortcuts import render , redirect
# from django.core.urlresolvers import reverse
from django.urls import reverse
from switch2voip.models import Product , Category, Variant
from .models import Cart, CartItem
from django.conf import settings
import stripe
stripe.api_key = "sk_test_rr3wMBxFaD0eJCtWvg9xQiow00mNqdldtL"

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    context = {
        'cart': cart_obj,
    }
    return render(request, "carts/cart.html",context)

def cart_add(request):
    product_id = request.POST.get('product_id')
    variant_name = request.POST.get('variant_field')
    quantity = request.POST.get('quantity_field')
    if not quantity:
        quantity = 1
    if product_id is not None:
        try:
            cart_obj, new_obj = Cart.objects.new_or_get(request)
            product = Product.objects.get(id=product_id)
            if variant_name:
                variant = Variant.objects.get(name=variant_name)
                item = CartItem.objects.create(item=product,item_cart=cart_obj, quantity=quantity, variant=variant)
            else:
                item = CartItem.objects.create(item=product,item_cart=cart_obj, quantity=quantity)
        except Product.DoesNotExist:
            return redirect("carts:cart")
        cart_obj.products.add(item)
        request.session['cart_items'] = cart_obj.products.count()
    return redirect("carts:cart")

def cart_remove(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            item = CartItem.objects.get(id=product_id)
        except Product.DoesNotExist:
            return redirect('carts:cart')
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        cart_obj.products.remove(item)
        item.delete()
        request.session['cart_items'] = cart_obj.products.count()
    return redirect("carts:cart")


def cart_update(request):
    product_id = request.POST.get('product_id')
    quantity = request.POST.get('update_quantity')
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_id is not None:
        try:
            item = CartItem.objects.filter(id=product_id)
        except Product.DoesNotExist:
            return redirect('carts:cart')
        item.update(quantity=quantity)
        cart_obj.coupon = None
        cart_obj.save()
    return redirect("carts:cart")



def index(request):
    return render(request, 'carts/checkout.html')



def charge(request):
    if request.method == 'POST':
        print('Date', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['name'],
            source=request.POST['stripeToken']
            )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='usd',
            description='Product Price'
            )

    return render(request,'carts/success.html')


def success(request):

    return render(request, 'carts/success.html')






##

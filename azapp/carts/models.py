from django.conf import settings
from django.db import models
from switch2voip.models import Product, Variant

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)



class CartItem(models.Model):
    item        = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    variant     = models.ForeignKey(Variant, related_name='variants', on_delete=models.CASCADE, blank=True, null=True)
    item_cart   = models.ForeignKey('Cart',related_name='carts',blank=True,null=True,on_delete=models.CASCADE)
    quantity    = models.PositiveIntegerField(default=1)

    def get_item_total(self):
        if self.variant:
            item_total = self.variant.price * self.quantity
        else:
            item_total = self.item.price * self.quantity
        return item_total

    def __str__(self):
        return str(self.id)




class Cart(models.Model):
    user        = models.ForeignKey(User ,related_name='users', on_delete=models.CASCADE, null=True, blank=True)
    products    = models.ManyToManyField(CartItem, blank=True)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

    def get_cart_total(self):
        products = self.products.all()
        cart_total = 0
        for x in products:
            if x.variant:
                cart_total += x.variant.price * x.quantity
            else:
                cart_total += x.item.price * x.quantity
        return cart_total


    def get_total(self):
        self.total = self.get_cart_total()
        self.save()
        return self.total

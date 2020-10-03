from django.utils import timezone
from django.shortcuts import render,  get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from carts.models import Cart , CartItem
from .models import Product , Category

class HomePageView(TemplateView):
    template_name = 'shop/products/list.html'
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        products = Product.objects.all()
        context['active'] = "home"
        context['products'] = "products"
        return context


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/products/list.html'
    paginate_by = 8

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context['active'] = 'services'
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context           = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        cart_item         = CartItem.objects.filter(item__id=self.kwargs['id'],item_cart=cart_obj)
        context['cart_item'] = cart_item
        context['cart'] = cart_obj
        context['active'] = 'services'
        return context


class ProductCategory(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/products/category.html'
    paginate_by = 8

    def get_queryset(self):
         self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
         return Product.objects.filter(category=self.category,available=True)

    def get_context_data(self, **kwargs):
         context = super(ProductCategory, self).get_context_data(**kwargs)
         context['category'] = self.category
         context['active'] = 'services'
         return context

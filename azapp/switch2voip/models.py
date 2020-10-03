from django.db import models
from django.urls import reverse
from django.db.models import Q
from django.db.models.signals import pre_save
from django.utils.timezone import make_aware
from azapp.utils import  unique_slug_generator

class ProductQuerySet(models.query.QuerySet):
    def available(self):
        return self.filter(available=True)
    def search(self, query):
        lookups =  (
        			   Q(name__icontains=query) |
        			   Q(price__iexact=query) |
        			   Q(tags__tag__iexact=query)
        		   )
        return self.filter(lookups).distinct()


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().available()

    def search(self, query):
        return self.get_queryset().available().search(query)

class Category(models.Model):
    name        = models.CharField(max_length=50, db_index=True)
    slug        = models.SlugField(max_length=200, db_index=True, blank=True, unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_at',)
        index_together = (('id', 'slug'),)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
         return reverse('shop:product_list_by_category', args=[self.slug])

class ProductTag(models.Model):
    tag     = models.CharField(max_length=120, blank=True, null=True)
    productid = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='tags')


class ProductPicture(models.Model):
    picture   = models.ImageField(upload_to='products/images', blank=True, null=True)
    productid = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='pictures')

class Product(models.Model):
    category      = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name          = models.CharField(max_length=120, db_index=True)
    slug          = models.SlugField(max_length=120, db_index=True, blank=True, unique=True)
    description   = models.TextField(blank=True)
    price         = models.DecimalField(max_digits=10, decimal_places=2)
    available     = models.BooleanField(default=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    ProductPicture = None
    ProductTag = None

    objects = ProductManager()

    class Meta:
        ordering = ('-updated_at',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('switch2voip:product_detail', args=[self.id,self.slug])



class Variant(models.Model):
    name    = models.CharField(max_length=120)
    price   = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')

    def __str__(self):
        return self.name






def slug_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_pre_save_receiver, sender=Product)
pre_save.connect(slug_pre_save_receiver, sender=Category)

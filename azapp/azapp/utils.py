import random
import string
from django.utils.text import slugify
from unidecode import unidecode
from django.template import defaultfilters

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def unique_order_id_generator(instance):
    order_new_id = random_string_generator(size=8)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_order_id_generator(instance)
    return order_new_id


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = defaultfilters.slugify(unidecode(new_slug))
    else:
        slug = defaultfilters.slugify(unidecode(instance.name))

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=3)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
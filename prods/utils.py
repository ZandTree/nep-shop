import random
import string
from django.utils.text import slugify


def make_random_string(chars=(string.ascii_lowercase +string.hexdigits),size=4):
    """
    return string made of random (ascii-chars,digits,*)of length = size
    """
    output = [random.choice(chars) for _ in range(size)]
    return "".join(output)


def make_unique_slug(instance,new_slug=None):
    """
    make unique slug for objects with attr= name and = slug.
    make slug based on name attr,check it existance. if yes,add a random_string
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Instance_Class = instance.__class__
    qs =  Instance_Class.objects.filter(slug=slug).exists()
    if qs:
        new_slug = "{slug}-{random_string}".format(slug=slug,random_string=make_random_string())
        # here call same function again to check whether its's unique
        # otherwise make another one
        #короче пойду на второй заход в попытке создать уникальную комби
        return make_unique_slug(instance,new_slug)
    return slug

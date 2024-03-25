from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    numbers = models.IntegerField(null=False)
    is_active = models.BooleanField(default=True)
    sale_count = models.IntegerField(default=0)
    slug = models.SlugField(editable=False,null=False,default='',db_index=True)
    # image_url = models.CharField(max_length=500,null=True,blank=True)
    image = models.ImageField(upload_to='images',null=True,blank=True)

    def save(self, *args, **kwargs):
        self.is_active = True if self.numbers>0 else False
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title

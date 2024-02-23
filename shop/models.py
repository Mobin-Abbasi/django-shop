from django.db import models
from django_jalali.db import models as jmodels
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='اسلاگ')

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=(['name']))
        ]
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    # relations
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='دسته بندی')
    # data
    name = models.CharField(max_length=255, verbose_name='نام')
    description = models.TextField(verbose_name='توشیحات')
    slug = models.CharField(max_length=255, unique=True, verbose_name='اسلاگ')
    inventory = models.PositiveIntegerField(default=0, verbose_name='موجودی')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    off = models.PositiveIntegerField(default=0, verbose_name='درصد تخفیف')
    new_price = models.PositiveIntegerField(default=0, verbose_name='قیمت پس از تخفیف')
    weight = models.PositiveIntegerField(default=0, verbose_name='وزن')
    # date
    created = jmodels.jDateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated = jmodels.jDateTimeField(auto_now=True, verbose_name='زمان اپدیت')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=(['-created']))
        ]
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name


class ProductFeature(models.Model):
    # relations
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    # data
    name = models.CharField(max_length=255, verbose_name='نام ویژگی')
    value = models.CharField(max_length=255, verbose_name='مقدار ویژگی')

    def __str__(self):
        return self.name + ':' + self.value


class Image(models.Model):
    # relations
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, verbose_name='محصول')
    # data
    file = models.ImageField(upload_to='product_images/%Y/%m/%d')
    title = models.CharField(max_length=255, verbose_name='عنوان', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    created = jmodels.jDateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=(['-created']))
        ]
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصویر ها'

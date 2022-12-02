from django.db import models

from abstraction.models import AbstractModel


def save_path(instance, filename):
    group = instance.product.group.subcategory.category.group.name.replace(' ', '_')
    category = instance.product.group.subcategory.category.name.replace(' ', '_')
    subcategory = instance.product.group.subcategory.name.replace(' ', '_')

    return 'product/{0}/{1}/{2}/{3}/{4}'.format(
        group,
        category,
        subcategory,
        instance.product.id,
        filename
    )


class Product(AbstractModel):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    TYPE_PRODUCT = [
        ('БУ', 'БУ'),
        ('Новое', 'Новое'),
    ]
    name = models.CharField(
        verbose_name='Название',
        max_length=255,
    )

    cost = models.FloatField(
        verbose_name='Цена',
    )

    type = models.CharField(
        verbose_name='Тип',
        max_length=255,
        choices=TYPE_PRODUCT,
    )

    group = models.ForeignKey(
        verbose_name='Группа',
        to='options.ProductGroup',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class ProductImage(AbstractModel):
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    image = models.ImageField(
        verbose_name='Изображение',
        upload_to=save_path
    )

    product = models.ForeignKey(
        verbose_name='Товар',
        to='product.Product',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return 'Изображение'

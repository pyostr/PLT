from django.db import models

from abstraction.models import AbstractModel


class Manufacturer(AbstractModel):
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    name = models.CharField(
        verbose_name='Название',
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.name


class Group(AbstractModel):
    """
    Группа товара производителя
    :ex:
        Manufacturer: Apple
        Group: Телефон
        Group: Планшет
    """
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    name = models.CharField(
        verbose_name='Название',
        max_length=255,
        unique=True,
    )
    manufacturer = models.ForeignKey(
        verbose_name='Производитель',
        to='options.Manufacturer',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name


class Category(AbstractModel):
    """
    Категория в группе
    :ex:
        Group: Телефон
        Category: iPhone
    """
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(
        verbose_name='Название',
        max_length=255,
        unique=True,
        db_index=True,
    )
    group = models.ForeignKey(
        verbose_name='Категория',
        to='options.Group',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name


class SubCategory(AbstractModel):
    """
    Подкатегория категории
    :ex:
        Category: iPhone
        SubCategory: iPhone 13
        SubCategory: iPhone 13 Pro
        SubCategory: iPhone 13 Pro Max
    """
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    name = models.CharField(
        verbose_name='Название',
        max_length=255,
        unique=True,
        db_index=True,
    )

    category = models.ForeignKey(
        verbose_name='Категория',
        to='options.Category',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name


class ProductGroup(AbstractModel):
    """
    Товар в подкатегории
    :ex:
        SubCategory: iPhone 13
        ProductGroup: iPhone 13 128 Black
        ProductGroup: iPhone 13 256 White
    """
    class Meta:
        verbose_name = 'Товарная группа'
        verbose_name_plural = 'Товарные группы'

    name = models.CharField(
        verbose_name='Название',
        max_length=255,
        unique=True,
        db_index=True,
    )

    subcategory = models.ForeignKey(
        verbose_name='Подкатегория',
        to='options.SubCategory',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name

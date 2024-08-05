from django.db import models


class BaseContents(models.Model):
    meta_title = models.CharField(max_length=250, blank=True, verbose_name='SEO заголовок', null=True)
    meta_description = models.TextField(blank=True, verbose_name='SEO описание', null=True)
    meta_keywords = models.TextField(blank=True, verbose_name='Поисковые слова', null=True)
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    status = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop_images', verbose_name='Фото', blank=True, null=True)
    url_slag = models.SlugField(max_length=200, verbose_name='URL', blank=True, null=True)
    created = models.TimeField(auto_now_add=True)
    update = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Categories(BaseContents, models.Model):
    parent_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Manufactures(BaseContents, models.Model):
    class Meta:
        db_table = 'manufacture'
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Products(BaseContents, models.Model):
    article = models.CharField(max_length=100, verbose_name='Артикул')
    price = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, verbose_name='Скидка в процентах')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Категория')
    manufacture = models.ForeignKey(to=Manufactures, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True,
                                    verbose_name='Производитель')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

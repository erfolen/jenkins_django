# # from django.db import models
#
#
# class ContentMixin:
#     meta_title = models.CharField(max_length=250, blank=True, verbose_name='SEO заголовок', null=True)
#     meta_description = models.TextField(blank=True, verbose_name='SEO описание', null=True)
#     meta_keywords = models.TextField(blank=True, verbose_name='Поисковые слова', null=True)
#     name = models.CharField(max_length=250, verbose_name='Наименование')
#     description = models.TextField(verbose_name='Описание', blank=True, null=True)
#     created = models.TimeField(auto_now_add=True)
#     update = models.TimeField(auto_now=True)
#     status = models.BooleanField(default=True)
#     sort_order = models.IntegerField(default=0)
#     image = models.ImageField(upload_to='shop_images', verbose_name='Фото', blank=True, null=True)
#     url_slag = models.SlugField(max_length=200, verbose_name='URL', blank=True, null=True)
#
#     class Meta:
#         abstract = True

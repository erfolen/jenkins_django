# Generated by Django 4.2.11 on 2024-06-02 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='SEO заголовок')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='SEO описание')),
                ('meta_keywords', models.TextField(blank=True, null=True, verbose_name='Поисковые слова')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created', models.TimeField(auto_now_add=True)),
                ('update', models.TimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('sort_order', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop_images', verbose_name='Фото')),
                ('url_slag', models.SlugField(blank=True, max_length=200, null=True, verbose_name='URL')),
                ('parent_id', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Manufactures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='SEO заголовок')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='SEO описание')),
                ('meta_keywords', models.TextField(blank=True, null=True, verbose_name='Поисковые слова')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created', models.TimeField(auto_now_add=True)),
                ('update', models.TimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('sort_order', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop_images', verbose_name='Фото')),
                ('url_slag', models.SlugField(blank=True, max_length=200, null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
                'db_table': 'manufacture',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='SEO заголовок')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='SEO описание')),
                ('meta_keywords', models.TextField(blank=True, null=True, verbose_name='Поисковые слова')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created', models.TimeField(auto_now_add=True)),
                ('update', models.TimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('sort_order', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop_images', verbose_name='Фото')),
                ('url_slag', models.SlugField(blank=True, max_length=200, null=True, verbose_name='URL')),
                ('article', models.CharField(max_length=100, verbose_name='Артикул')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Цена')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Скидка в процентах')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.categories', verbose_name='Категория')),
                ('manufacture', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.manufactures', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'product',
            },
        ),
    ]

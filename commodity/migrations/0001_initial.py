# Generated by Django 3.2.20 on 2023-07-27 12:00

import base_app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('color', '0001_initial'),
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('size', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommodityHaveCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='資料創建時間')),
                ('updated_datetime', models.DateTimeField(auto_now=True, verbose_name='資料最後更新時間')),
                ('belong_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.categorymodel', verbose_name='所屬類型')),
            ],
            options={
                'db_table': 'commodity_have_category',
            },
        ),
        migrations.CreateModel(
            name='CommodityHaveColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='資料創建時間')),
                ('updated_datetime', models.DateTimeField(auto_now=True, verbose_name='資料最後更新時間')),
                ('belong_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='color.colormodel', verbose_name='所屬顏色')),
            ],
            options={
                'db_table': 'commodity_have_color',
            },
        ),
        migrations.CreateModel(
            name='CommodityHaveSizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='資料創建時間')),
                ('updated_datetime', models.DateTimeField(auto_now=True, verbose_name='資料最後更新時間')),
            ],
            options={
                'db_table': 'commodity_have_size',
            },
        ),
        migrations.CreateModel(
            name='CommodityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='資料創建時間')),
                ('updated_datetime', models.DateTimeField(auto_now=True, verbose_name='資料最後更新時間')),
                ('code', models.CharField(default='', max_length=50, verbose_name='商品代碼')),
                ('name', models.CharField(default='', max_length=150, verbose_name='商品名稱')),
                ('price', models.IntegerField(default=0, verbose_name='商品價格')),
                ('inventory', models.IntegerField(default=0, verbose_name='商品庫存')),
                ('create_user', models.ForeignKey(on_delete=models.SET(base_app.models.get_unknown_user), related_name='commoditymodel_create_user', to=settings.AUTH_USER_MODEL, verbose_name='資料創建者')),
                ('have_category', models.ManyToManyField(related_name='commodity_have_category', through='commodity.CommodityHaveCategoryModel', to='category.CategoryModel', verbose_name='商品類型')),
                ('have_color', models.ManyToManyField(related_name='commodity_have_color', through='commodity.CommodityHaveColorModel', to='color.ColorModel', verbose_name='商品顏色')),
                ('have_size', models.ManyToManyField(related_name='commodity_have_size', through='commodity.CommodityHaveSizeModel', to='size.SizeModel', verbose_name='商品尺寸')),
                ('updated_user', models.ForeignKey(on_delete=models.SET(base_app.models.get_unknown_user), related_name='commoditymodel_updated_user', to=settings.AUTH_USER_MODEL, verbose_name='資料最後更新者')),
            ],
            options={
                'db_table': 'commodity',
            },
        ),
        migrations.AddField(
            model_name='commodityhavesizemodel',
            name='belong_commodity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.commoditymodel', verbose_name='所屬商品'),
        ),
        migrations.AddField(
            model_name='commodityhavesizemodel',
            name='belong_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='size.sizemodel', verbose_name='所屬尺寸'),
        ),
        migrations.AddField(
            model_name='commodityhavesizemodel',
            name='create_user',
            field=models.ForeignKey(on_delete=models.SET(base_app.models.get_unknown_user), related_name='commodityhavesizemodel_create_user', to=settings.AUTH_USER_MODEL, verbose_name='資料創建者'),
        ),
        migrations.AddField(
            model_name='commodityhavesizemodel',
            name='updated_user',
            field=models.ForeignKey(on_delete=models.SET(base_app.models.get_unknown_user), related_name='commodityhavesizemodel_updated_user', to=settings.AUTH_USER_MODEL, verbose_name='資料最後更新者'),
        ),
        migrations.AddField(
            model_name='commodityhavecolormodel',
            name='belong_commodity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.commoditymodel', verbose_name='所屬商品'),
        ),
        migrations.AddField(
            model_name='commodityhavecolormodel',
            name='create_user',
            field=models.ForeignKey(on_delete=models.SET(base_app.models.get_unknown_user), related_name='commodityhavecolormodel_create_user', to=settings.AUTH_USER_MODEL, verbose_name='資料創建者'),
        ),
        migrations.AddField(
            model_name='commodityhavecolormodel',
            name='updated_user',
            field=models.ForeignKey(on_delete=models.SET(base_app.models.get_unknown_user), related_name='commodityhavecolormodel_updated_user', to=settings.AUTH_USER_MODEL, verbose_name='資料最後更新者'),
        ),
        migrations.AddField(
            model_name='commodityhavecategorymodel',
            name='belong_commodity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.commoditymodel', verbose_name='所屬商品'),
        ),
        migrations.AddField(
            model_name='commodityhavecategorymodel',
            name='create_user',
            field=models.ForeignKey(on_delete=models.SET(base_app.models.get_unknown_user), related_name='commodityhavecategorymodel_create_user', to=settings.AUTH_USER_MODEL, verbose_name='資料創建者'),
        ),
        migrations.AddField(
            model_name='commodityhavecategorymodel',
            name='updated_user',
            field=models.ForeignKey(on_delete=models.SET(base_app.models.get_unknown_user), related_name='commodityhavecategorymodel_updated_user', to=settings.AUTH_USER_MODEL, verbose_name='資料最後更新者'),
        ),
    ]

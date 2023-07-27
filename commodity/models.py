# package
from django.db import models
# models
from base_app.models import BaseModel
from category.models import CategoryModel
from color.models import ColorModel
from size.models import SizeModel


class CommodityModel(BaseModel):
    code = models.CharField(default='', max_length=50, verbose_name='商品代碼')
    name = models.CharField(default='', max_length=150, verbose_name='商品名稱')
    price = models.IntegerField(default=0, verbose_name='商品價格')
    inventory = models.IntegerField(default=0, verbose_name='商品庫存')
    have_category = models.ManyToManyField(
        CategoryModel, through='CommodityHaveCategoryModel', through_fields=('belong_commodity', 'belong_category'),
        related_name='commodity_have_category', verbose_name='商品類型')
    have_color = models.ManyToManyField(
        ColorModel, through='CommodityHaveColorModel', through_fields=('belong_commodity', 'belong_color'),
        related_name='commodity_have_color', verbose_name='商品顏色')
    have_size = models.ManyToManyField(
        SizeModel, through='CommodityHaveSizeModel', through_fields=('belong_commodity', 'belong_size'),
        related_name='commodity_have_size', verbose_name='商品尺寸')

    class Meta:
        db_table = "commodity"


class CommodityHaveCategoryModel(BaseModel):
    belong_commodity = models.ForeignKey(CommodityModel, on_delete=models.CASCADE, verbose_name='所屬商品')
    belong_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name='所屬類型')

    class Meta:
        db_table = "commodity_have_category"


class CommodityHaveColorModel(BaseModel):
    belong_commodity = models.ForeignKey(CommodityModel, on_delete=models.CASCADE, verbose_name='所屬商品')
    belong_color = models.ForeignKey(ColorModel, on_delete=models.CASCADE, verbose_name='所屬顏色')

    class Meta:
        db_table = "commodity_have_color"


class CommodityHaveSizeModel(BaseModel):
    belong_commodity = models.ForeignKey(CommodityModel, on_delete=models.CASCADE, verbose_name='所屬商品')
    belong_size = models.ForeignKey(SizeModel, on_delete=models.CASCADE, verbose_name='所屬尺寸')

    class Meta:
        db_table = "commodity_have_size"

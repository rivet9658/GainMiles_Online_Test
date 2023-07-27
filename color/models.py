# package
from django.db import models

# models
from base_app.models import BaseModel


class ColorModel(BaseModel):
    code = models.CharField(default='', max_length=50, verbose_name='顏色代碼')
    name = models.CharField(default='', max_length=150, verbose_name='顏色名稱')

    class Meta:
        db_table = "color"

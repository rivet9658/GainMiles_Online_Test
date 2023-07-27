# package
from django.db import models

# models
from base_app.models import BaseModel


class SizeModel(BaseModel):
    code = models.CharField(default='', max_length=50, verbose_name='尺寸代碼')
    name = models.CharField(default='', max_length=150, verbose_name='尺寸名稱')

    class Meta:
        db_table = "size"

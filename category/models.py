# package
from django.db import models

# models
from base_app.models import BaseModel


class CategoryModel(BaseModel):
    code = models.CharField(default='', max_length=50, verbose_name='類型代碼')
    name = models.CharField(default='', max_length=150, verbose_name='類型名稱')

    class Meta:
        db_table = "category"

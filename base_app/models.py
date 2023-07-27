# package
import os
from dotenv import load_dotenv
from django.db import models
from django.contrib.auth.models import User

load_dotenv()


# 當綁定的使用者被刪除時，將該資料綁到匿名使用者上
def get_unknown_user():
    now_user, created = User.objects.get_or_create(username="unknown")
    if created:
        now_user.set_password(os.getenv("UNKNOWN_PASSWORD"))
        now_user.is_active = False
        now_user.save()
    return now_user


class BaseModel(models.Model):
    create_user = models.ForeignKey(User, on_delete=models.SET(get_unknown_user), verbose_name='資料創建者',
                                    related_name='%(class)s_create_user')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='資料創建時間')
    updated_user = models.ForeignKey(User, on_delete=models.SET(get_unknown_user), verbose_name='資料最後更新者',
                                     related_name='%(class)s_updated_user')
    updated_datetime = models.DateTimeField(auto_now=True, verbose_name='資料最後更新時間')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.create_user_id:
            self.create_user = get_unknown_user()
        if not self.updated_user_id:
            self.updated_user = get_unknown_user()
        super().save(*args, **kwargs)

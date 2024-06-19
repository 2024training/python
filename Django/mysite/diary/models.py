from django.db import models
from django.utils import timezone
import uuid
from django.conf import settings

class Diary(models.Model):
    # 編集不可
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(verbose_name='日付', default=timezone.now)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    text = models.CharField(verbose_name='本文', max_length=200)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='編集日時', blank=True, null=True)
    # 外部キー　ユーザーの消去に伴って日記データも消すという優れもの
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 文字列表現をタイトルに指定(管理画面で見やすく)(表示やデバッグのための機能なので、データベースクエリの検索条件にはなりえない)
    def __str__(self):
        return f"{self.text}({self.created_at.year}年{self.created_at.month}月{self.created_at.day}日)"




    
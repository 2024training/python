from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import UserManager

# ユーザーを操作するメソッドを提供
class CustomUserManager(UserManager):
    use_in_migrations = True

    # 内部メソッド
    def _create_user(self, email, username, password, **extra_fields):
        # create_user と create_superuser の共通処理
        if not email:
            raise ValueError('email must be set')
        if not username:
            raise ValueError('username must be set')

        user = self.model(email=email, username=username, **extra_fields)
        # ハッシュ化
        user.set_password(password)
        user.save(using=self._db)

        return user

    # 最初はまぁpasswordとemail書いてなくてもいいよ
    def create_user(self, username, email=None, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        # 管理者サイトへのアクセス権をON
        extra_fields.setdefault('is_staff', True)
        # system全体へのaccessを許可
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, username, password, **extra_fields)

class CustomUser(AbstractUser):
    # ユーザーマネージャーの使用
    objects = CustomUserManager()

    # 関連名を変更する
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

    # 文字列表現するときにemailになるように設定している。
    def __str__(self):
        return self.email

# 関連名を変更するためにデフォルトのユーザーモデルを上書きする
AUTH_USER_MODEL = 'accounts.CustomUser'
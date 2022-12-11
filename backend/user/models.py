import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    """ カスタムユーザーマネージャー """

    # ユーザを作成するメソッド
    def create_user(self, email, user_name, password=None):
        """ ユーザー作成 """

        if not email:
            raise ValueError('User must have an email address')

        # emailのドメインを小文字に変換
        email = self.normalize_email(email)
        # UserProfileモデルを参照してuserを定義
        user = self.model(email=email, user_name=user_name)
        # userが入力したパスワードをハッシュ化
        user.set_password(password)
        # settings.pyでdefaultに設定されているDBに保存
        user.save(using=self._db)

        return user

    def create_superuser(self, email, user_name, password):
        """ スーパーユーザー作成 """

        # 上記create_userを利用
        user = self.create_user(email, user_name, password)

        # superuserの権限を適用
        user.is_superuser = True
        # 管理画面にアクセスを許可するか
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """カスタマイズユーザーモデル"""

    """
    emailを利用したログイン認証に変更
    JWTトークン認証必須項目usernameからemailに変更される
    """
    USERNAME_FIELD = 'email'
    """管理者が管理コマンド上（ターミナル等）でユーザーを作成する時に表示されるリスト"""
    REQUIRED_FIELDS = ['user_name']

    # UserManagerのメソッドを使えるようにする
    objects = UserManager()

    class Meta:
        db_table = 'user'

    id = models.UUIDField(verbose_name='ユーザーID', primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField(verbose_name='ユーザーパスワード', max_length=128)
    email = models.EmailField(verbose_name='ユーザーメールアドレス', unique=True, max_length=200)
    user_name = models.CharField(verbose_name='ユーザー名', max_length=20)
    user_remark = models.CharField(verbose_name='ユーザー備考', max_length=250, blank=True)
    user_type = models.IntegerField(verbose_name='ユーザータイプ', default=1)
    create_date = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    last_login = models.DateTimeField(verbose_name='最終ログイン日付', auto_now=True)
    is_active = models.BooleanField(verbose_name='有効フラグ', default=True)
    is_staff = models.BooleanField(verbose_name='管理画面アクセスフラグ', default=False)

class UserLoginHistory(models.Model):
    """ユーザーログイン履歴モデル"""

    class Meta:
        db_table = 'login_history'

    user = models.OneToOneField(User, verbose_name='ユーザー', on_delete=models.CASCADE)
    login_date = models.DateTimeField(verbose_name='ログイン日付', auto_now_add=True)

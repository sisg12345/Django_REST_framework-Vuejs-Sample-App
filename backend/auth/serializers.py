from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import exceptions

from user.models import User

class TokenObtainPairSerializer(TokenObtainPairSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']

    @classmethod
    def get_token(cls, user):
        """トークン取得"""
        token = super(TokenObtainPairSerializer, cls).get_token(user)
        token['email'] = user.email

        return token

    def validate(self, data):
        """バリデーション"""
        # ユーザー情報取得取得
        user = User.objects.filter(email=data['email']).first()

        if not user:
            # ユーザーが存在しない場合
            raise exceptions.AuthenticationFailed('ユーザー名もしくはパスワード正しくありません。')
        elif not check_password(data['password'], user.password):
            # パスワード一致しない場合
            raise exceptions.AuthenticationFailed('ユーザー名もしくはパスワード正しくありません。')

        # 返却データからemailを削除
        del data['email']
        # 返却データからパスワードを削除
        del data['password']
        # ユーザーIDを返却データに追加
        data['user_id'] = user.id
        # ユーザー名を返却データに追加
        data['user_name'] = user.user_name
        # ユーザータイプを返却データに追加
        data['user_type'] = user.user_type
        # トークを取得
        token = self.get_token(user)
        # リフレッシュトークンを返却データに追加
        data["refresh"] = str(token)
        # アクセストークンを返却データに追加
        data["access"] = str(token.access_token)

        return data

class RegisterSerializer(serializers.ModelSerializer):
    """ユーザー登録用シリアライザ"""

    # パスワードの定義
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # パスワード確認用の定義
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['user_name', 'email', 'password', 'password_confirm']

    def validate(self, data):
        """バリデーション"""
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"入力されたパスワードが一致しません。"})

        return data

    def create(self, validated_data):
        """ユーザー登録"""
        user = User.objects.create(
            user_name=validated_data['user_name'],
            email=validated_data['email'],
            # パスワードハッシュ化
            password=make_password(validated_data['password'])
        )
        user.save()

        return user
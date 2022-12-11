from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    """ユーザーモデル用シリアライザ"""

    class Meta:
        # 対象のモデルクラスを指定
        model = User
        # 使用するデルのフィールド指定
        fields = ('id', 'email', 'user_name', 'user_type', 'user_remark', 'last_login', 'update_date')
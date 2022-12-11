from django.shortcuts import get_object_or_404

from .models import User

class UserQuerys:
    """ユーザーモデルオブジェクト取得クラス"""

    def get_user_list(self, params):
        """ユーザー一覧取得"""
        # 検索条件
        query_params = {}
        # 入力内容なしの検索条件を取り除き, like検索に設定
        for key, value in params.items():
            if value is not None:
                # 検索条件をlike検索に変換
                query_params[key+'__contains'] = value

        return User.objects.filter(**query_params).order_by('user_name', 'email')

    def get_user(self, user_id):
        """ユーザー取得"""
        return get_object_or_404(User, pk=user_id)
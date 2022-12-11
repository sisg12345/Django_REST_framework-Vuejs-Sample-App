from user.models import User

class LoginQuerys:
    """ログインユーザー情報取得クラス"""

    def get_user(self, email):
        """ユーザー情報取得"""
        return User.objects.get(email=email)
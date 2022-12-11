from .querys import LoginQuerys

class LoginSevices:
    """ログインのビジネスロジック,取得・登録・更新処理を行うクラス"""

    def __init__(self):
        """ログインユーザーモデルオブジェクト取得クラスのインスタンスを生成"""
        self.loginQuerys = LoginQuerys()

    def get_user(self, email):
        """ログインユーザー情報取得"""
        return self.loginQuerys.get_user(email)

from .querys import UserQuerys

class UserSevices:
    """ユーザーモデルのビジネスロジック,取得・登録・更新・削除処理を行うクラス"""

    def __init__(self):
        """ユーザーモデルオブジェクト取得クラスのインスタンスを生成"""
        self.userQuerys = UserQuerys()

    def get_user_list(self, params):
        """ユーザー一覧取得"""
        return self.userQuerys.get_user_list(params)

    def get_user(self, user_id):
        """ユーザー取得"""
        return self.userQuerys.get_user(user_id)

    def create_user(self, serializer):
        """ユーザー登録"""
        serializer.save()

    def update_user(self, serializer):
        """ユーザー更新"""
        serializer.save()

    def delete_user(self, userObject):
        """ユーザー削除"""
        userObject.delete()

from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from .services import UserSevices

class UserListAPIView(views.APIView):
    """ユーザーモデルの取得(一覧)APIクラス"""

    def __init__(self):
        """ユーザーモデルのビジネスロジッククラスのインスタンスを生成"""
        self.userSevices = UserSevices()

    def get(self, request):
        """ユーザー一覧取得"""
        # 対象オブジェクトを取得
        user_list = self.userSevices.get_user_list(request.GET)
        # シリアライザオブジェクトを作成
        serializer = UserSerializer(instance=user_list, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

class UserAPIView(views.APIView):
    """ユーザーモデルのCRUDAPIクラス"""

    def __init__(self):
        """ユーザーモデルのビジネスロジッククラスのインスタンスを生成"""
        self.userSevices = UserSevices()

    # TODO: ユーザー一覧画面にてユーザー登録できる処理を追加
    def post(self, request):
        """ユーザー登録"""
        # シリアライザオブジェクトを作成
        serializer = UserSerializer(data=request.data)
        # バリデーション
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクト登録
        self.userSevices.create_user(serializer)

        return Response(status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        """ユーザー更新"""
        # 更新対象オブジェクトを取得
        user = self.userSevices.get_user(user_id=pk)
        # シリアライザオブジェクトを作成
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        # バリデーション
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクト更新
        self.userSevices.update_user(serializer)

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        """ユーザー削除"""
        # 削除対象オブジェクトを取得
        user = self.userSevices.get_user(user_id=pk)
        # モデルオブジェクトを削除
        self.userSevices.delete_user(user)

        return Response(status=status.HTTP_204_NO_CONTENT)
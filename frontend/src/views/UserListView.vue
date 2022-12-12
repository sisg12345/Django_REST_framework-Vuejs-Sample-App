<template>
  <div id="user-list">
    <!-- 検索部 -->
    <UserSearchForm @searchUserList="searchUserList"></UserSearchForm>
    <br>
    <!-- テーブル部 -->
    <UserListTable ref="userListTable" @editUserInfo="editUserInfo" @deleteUserInfo="deleteUserInfo" @deleteMultiUserInfo="deleteMultiUserInfo"></UserListTable>
    <!-- モーダル -->
    <UserEditModal ref="userEditModal" @saveUserInfo="saveUserInfo"></UserEditModal>
  </div>
</template>
<script>
import { ref } from 'vue'
import UserSearchForm from '../components/userList/UserSearchForm.vue'
import UserListTable from '../components/userList/UserListTable.vue'
import UserEditModal from '../components/userList/UserEditModal.vue'
import axios from '../api/axios.js'

export default {
  name: 'UserListView',
  components: { UserSearchForm, UserListTable, UserEditModal },
  setup() {
    // ユーザー一覧データ
    // const userListData = reactive({})
    // UserListTable: ref参照
    const userListTable = ref(null)
    // UserEditModal: ref参照
    const userEditModal = ref(null)
    // グリッドの更新/削除後に再検索するためのパラメーター保持用
    var reSearchPrams = null

    // ユーザー検索
    const searchUserList = async (searchPrams) => {
      // 再検索用パラメーターに値をセット
      reSearchPrams = searchPrams

      // ユーザー検索
      await axios.get('api/v1/userList/', {
        params: searchPrams
      }).then((response) => {
        // TODO: 引数修正
        userListTable.value.doSearch(0, 10, response.data, "email", "asc")
      })
    }

    // ユーザー情報編集モーダルを表示
    const editUserInfo = (editUserData) => {
      userEditModal.value.showModal(editUserData)
    }

    // ユーザー情報を削除
    const deleteUserInfo = async (deleteUserId) => {
      await axios.delete('api/v1/user/' + deleteUserId + '/')
      .then(
        // グリッドデータを再取得
        await searchUserList(reSearchPrams)
      ).catch((error) => {
        // TODO: すでに更新されていたかチェック
        console.log(error)
      })
    }

    // ユーザーデータ複数件削除
    const deleteMultiUserInfo = (deleteUserIds) => {
      console.log(deleteUserIds)
    }

    // ユーザー情報を保存
    const saveUserInfo = async (saveUserData) => {
      await axios.patch('api/v1/user/' + saveUserData.userId + '/', {
        user_name: saveUserData.userName,
        email: saveUserData.userEmail,
        user_type: saveUserData.userType,
        user_remark: saveUserData.userRemark
      }).then(() => {
        // グリッドデータを再取得
        searchUserList(reSearchPrams)
      }).catch((error) => {
        // TODO: すでに更新されていたかチェック
        console.log(error)
      })
    }

    return {
      // userListData,
      userEditModal,
      userListTable,
      searchUserList,
      editUserInfo,
      deleteUserInfo,
      deleteMultiUserInfo,
      saveUserInfo
    }
  }
}
</script>
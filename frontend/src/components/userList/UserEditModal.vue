<template>
  <div id="userEditModal">
    <!-- Modal -->
    <div class="modal fade" id="userInfoEditModal" tabindex="-1" role="dialog" aria-labelledby="userInfoModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-xl modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="userInfoModalLabel">ユーザー情報</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div class="row">
              <div class="col-6 form-group">
                <!-- TODO aria-describedby -->
                <!-- ユーザーID -->
                <label for="userId" class="form-control-label">ユーザーID</label>
                <!-- TODO aria-describedby -->
                <input type="text" class="form-control" id="userId" aria-describedby="" v-model="userId" readonly>
              </div>
              <div class="col-6 form-group">
                <!-- ユーザー名 -->
                <label for="userName" class="form-control-label">ユーザー名</label>
                <input type="text" class="form-control" id="userName" aria-describedby="" v-model="userName">
              </div>
            </div>
            <div class="row">
              <div class="col-6 form-group">
                <!-- ユーザーメールアドレス -->
                <label for="userEmail" class="form-control-label">メールアドレス</label>
                <input type="email" class="form-control" id="userEmail" aria-describedby="" v-model="userEmail">
              </div>
              <div class="col-3 form-group">
                <!-- ユーザータイプ -->
                <label for="userType" class="form-control-label">ユーザータイプ</label>
                <select class="form-control" id="userType" v-model="userType">
                  <option>一般</option>
                  <option>管理者</option>
                </select>
              </div>
            </div>
            <div class="row">
              <div class="col-12 form-group">
                <!-- ユーザー備考 -->
                <label for="userRemark" class="form-control-label">備考</label>
                <textarea type="email" class="form-control" id="userRemark" aria-describedby="" v-model="userRemark"></textarea>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <!-- キャンセルボタン -->
            <CancelButton data-dismiss="modal"></CancelButton>
            <!-- 保存ボタン -->
            <SaveButton @click="saveUserInfo"></SaveButton>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import $ from 'jquery'
import { ref, reactive } from 'vue'
import CancelButton from '../Parts/CancelButton.vue'
import SaveButton from '../Parts/SaveButton.vue'

export default {
  name: 'UserEditModal',
  components: { SaveButton, CancelButton },
  emits: [ 'saveUserInfo' ],
  setup(props, context) {
    // ユーザーID
    const userId = ref(null)
    // ユーザー名
    const userName = ref(null)
    // ユーザーメールアドレス
    const userEmail = ref(null)
    // ユーザータイプ
    const userType = ref(null)
    // ユーザー備考
    const userRemark = ref(null)

    // 保存パラメーター: ユーザーデータを格納
    const saveUserData = reactive({
      userId: userId,
      userName: userName,
      userEmail: userEmail,
      userType: userType,
      userRemark: userRemark
    })

    // モーダルを表示時処理
    const showModal = (editUserData) => {
      // ユーザーIDをセット
      userId.value = editUserData.id
      // ユーザー名をセット
      userName.value = editUserData.user_name
      // メールアドレスをセット
      userEmail.value = editUserData.email
      // ユーザータイプをセット
      userType.value = editUserData.user_type
      // ユーザー備考をセット
      userRemark.value = editUserData.user_remark

      // モーダルを表示する
      $('#userInfoEditModal').modal('show')
    }

    // ユーザーデータ保存処理呼び出し
    const saveUserInfo = () => {
      // ユーザー情報保存処理を呼び出す
      context.emit('saveUserInfo', saveUserData)
      // モーダルを閉じる
      $('#userInfoEditModal').modal('hide')
    }

    return {
      userId,
      userName,
      userEmail,
      userType,
      userRemark,
      saveUserData,
      showModal,
      saveUserInfo
    }
  }
}
</script>
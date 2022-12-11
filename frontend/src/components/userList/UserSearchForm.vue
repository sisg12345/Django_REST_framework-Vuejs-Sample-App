<template>
  <div id="user-search-form">
    <div class="condition-background col-12 mb-2">
      <div class="row">
        <div class="col-6 form-group">
          <!-- ユーザーID入力欄 -->
          <label for="userId" class="form-control-label">ユーザーID</label>
          <!-- TODO aria-describedby -->
          <input type="text" class="form-control" id="userId" aria-describedby="" v-model="userId">
        </div>
        <div class="col-6 form-group">
          <!-- ユーザー名入力欄 -->
          <label for="userName" class="form-control-label">ユーザー名</label>
          <input type="text" class="form-control" id="userName" aria-describedby="" v-model="userName">
        </div>
      </div>
      <div class="row">
        <div class="col-6 form-group">
          <!-- ユーザーメールアドレス入力欄 -->
          <label for="userEmail" class="form-control-label">メールアドレス</label>
          <input type="email" class="form-control" id="userEmail" aria-describedby="" v-model="userEmail">
        </div>
        <div class="col-3 form-group">
          <!-- ユーザータイプ入力欄 -->
          <label for="userType" class="form-control-label">ユーザータイプ</label>
          <select class="form-control" id="userType" v-model="userType">
            <option>一般</option>
            <option>管理者</option>
          </select>
        </div>
      </div>
      <div class="row">
        <div class="col-3 form-group">
          <!-- ログイン日付From入力欄 -->
          <label for="loginDateFrom" class="form-control-label">ログイン日付 From</label>
          <DatePicker id="loginDateFrom" ref="loginDateFrom"></DatePicker>
        </div>
        <div class="col-3 form-group">
          <!-- ログイン日付To入力欄 -->
          <label for="loginDateTo" class="form-control-label">To</label>
          <DatePicker id="loginDateTo" ref="loginDateTo"></DatePicker>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row text-right">
        <div class="col-12">
          <!-- 検索ボタン -->
          <SearchButton @click="searchUserList"></SearchButton>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <!-- クリアボタン -->
          <ClearButton @click="clearCondition"></ClearButton>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { ref, reactive } from 'vue'
import SearchButton from '../Parts/SearchButton.vue'
import ClearButton from '../Parts/ClearButton.vue'
import DatePicker from '../Parts/DatePicker.vue'

export default {
  name: 'UserListSearchForm',
  components: { SearchButton, ClearButton, DatePicker },
  emits: [ 'searchUserList' ],
  setup(props, context) {
    // ユーザーID
    const userId = ref(null)
    // ユーザー名
    const userName = ref(null)
    // ユーザーメールアドレス
    const userEmail = ref(null)
    // ユーザータイプ
    const userType = ref(null)
    // ユーザーログイン日付From
    const loginDateFrom = ref(null)
    // ユーザーログイン日付To
    const loginDateTo = ref(null)
    // 検索パラメーター: 検索条件データを格納
    const searchPrams = reactive({
      id: userId,
      user_name: userName,
      email: userEmail,
      user_type: userType,
      // TODO: 検索条件にログイン日付を追加
      // loginDateFrom: loginDateFrom,
      // loginDateTo: loginDateTo
    })

    // ユーザー一覧検索
    const searchUserList = () => {
      context.emit('searchUserList', searchPrams)
    }

    // 検索条件クリア
    const clearCondition = () => {
      // 画面入力クリア
      userId.value = null
      userName.value = null
      userEmail.value = null
      userType.value = null
      loginDateFrom.value = null
      loginDateTo.value = null
    }

    return {
      userId,
      userName,
      userEmail,
      userType,
      loginDateFrom,
      loginDateTo,
      searchPrams,
      searchUserList,
      clearCondition
    }
  }
}
</script>
<style scoped>
.condition-background {
  background-color: whitesmoke;
}
.form-control-label {
  font-size: 12px;
}
</style>
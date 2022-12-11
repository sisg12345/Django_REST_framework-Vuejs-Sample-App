<template>
  <div id="login" class="d-flex align-items-center">
    <div class="container px-4 py-5 mx-auto">
      <div class="card card0">
        <div class="d-flex flex-lg-row flex-column-reverse">
          <div class="card card1">
            <div class="row justify-content-center my-auto">
              <div class="col-md-8 col-10 my-5">
                <h3 class="mb-5 text-center" v-if="registerMode">アカウントを作成</h3>
                <h3 class="mb-5 text-center" v-else-if="reissueMode">パスワードを再発行</h3>
                <h3 class="mb-5 text-center" v-else>ログイン</h3>
                <!-- エラーメッセージエリア -->
                <ErrorMessageArea :errorMessage="errorMessage" @closeMessage="errorMessage = null"></ErrorMessageArea>
                <!-- ユーザー名入力欄 -->
                <div class="form-group" v-if="registerMode">
                  <label for="userName" class="form-control-label">ユーザー名</label>
                  <input type="text" id="userName" name="userName" class="form-control" v-model="userName">
                </div>
                <!-- メールアドレス入力欄 -->
                <div class="form-group">
                  <label for="email" class="form-control-label">メールアドレス</label>
                  <input type="text" id="email" name="email" class="form-control" v-model="email">
                </div>
                <!-- パスワード入力欄 -->
                <div class="form-group" v-if="!reissueMode">
                  <label for="password" class="form-control-label">パスワード</label>
                  <input type="password" id="password" name="password" class="form-control" v-model="password">
                </div>
                <!-- パスワード確認入力欄 -->
                <div class="form-group" v-if="registerMode">
                  <label for="password-confirm" class="form-control-label">パスワード確認</label>
                  <input type="password" id="password" name="password-confirm" class="form-control" v-model="passwordConfirm">
                </div>
                <!-- 作成ボタン -->
                <div class="row justify-content-center my-3 px-3" v-if="registerMode">
                  <button class="btn-block btn-color" @click="register">作成</button>
                </div>
                <!-- 発行ボタン -->
                <div class="row justify-content-center my-3 px-3" v-else-if="reissueMode">
                  <button class="btn-block btn-color" @click="reissue">発行</button>
                </div>
                <!-- ログインボタン -->
                <div class="row justify-content-center my-3 px-3" v-else>
                  <button class="btn-block btn-color" @click="login">ログイン</button>
                </div>
                <!-- パスワードを忘れた場合リンク -->
                <div class="row justify-content-center my-2" v-if="reissueMode === false && registerMode === false">
                  <a href="#" @click="reissueMode = true">
                    <small>パスワードを忘れた場合</small>
                  </a>
                </div>
              </div>
            </div>
            <!-- 新しいアカウント作成ボタン -->
            <div class="bottom text-center mb-5" v-if="reissueMode === false && registerMode === false">
              <p href="#" class="sm-text mx-auto mb-3">新しいアカウントを作成
                <button class="btn btn-white ml-2" @click="registerMode = true">登録</button>
              </p>
            </div>
            <div class="bottom text-center mb-5" v-if="reissueMode || registerMode">
              <button class="btn btn-white ml-2" @click="registerMode = false, reissueMode = false">戻る</button>
            </div>
          </div>
          <div class="card card2">
            <div class="my-auto mx-md-5 px-md-5 right">
              <h3 class="text-white">タイトル</h3>
              <small class="text-white">説明</small>
            </div>
          </div>
        </div>
      </div>
    </div>
</div>
</template>
<script>
import { ref, watch } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import axios from '../api/axios.js'
import ErrorMessageArea from '../components/Parts/ErrorMessageArea.vue'

export default {
  name: 'LoginView',
  components: { ErrorMessageArea },
  setup() {
    // routerを使用するための初期化
    const router = useRouter()
    // storeを使用するための初期化
    const store = useStore()
    // 新規登録モード
    const registerMode = ref(false)
    // パスワード再発行モード
    const reissueMode = ref(false)
    // メールアドレス
    const email = ref(null)
    // パスワード
    const password = ref(null)
    // パスワード確認用
    const passwordConfirm = ref(null)
    // ユーザー名
    const userName = ref(null)
    // エラーメッセージ
    const errorMessage = ref(null)

    // ログイン
    const login = async () => {
      await axios.post('api/v1/login/', {
        email: email.value,
        password: password.value
      }).then((response) => {
        // ログイン情報をstoreに保存
        store.dispatch('auth/login', response.data)
        // ログイン後のトップページへ遷移
        router.push('/')
      }).catch((error) => {
        // 認証失敗の場合の処理
        if (error.response.status === 401) {
          // エラーメッセージを設定
          errorMessage.value = error.response.data.detail
        }
      })
    }

    // ユーザー登録
    const register = async () => {
      await axios.post('api/v1/register/', {
        user_name: userName.value,
        email: email.value,
        password: password.value,
        password_confirm: passwordConfirm.value
      }).then(() => {
        // 新規登録モードをオフにし、ログインモードに戻る
        registerMode.value = false
        }).catch((error) => {
        // メールアドレスの存在チェックエラーメッセージが返却された場合
        if (error.response.data.email !== undefined) {
          // メールアドレスの存在チェックエラーメッセージを設定
          errorMessage.value = error.response.data.email[0]
        }
      })
    }

    // パスワード再発行
    const reissue = () => {
      alert()
    }

    watch(
      // 新規労録モードもしくパスワード再発行モードが変更した場合に入力項目をクリアする
      [registerMode, reissueMode], () => {
        email.value = null
        password.value = null
        passwordConfirm.value = null
        userName.value = null        
      }
    )

    return {
      registerMode,
      reissueMode,
      email,
      password,
      passwordConfirm,
      userName,
      login,
      register,
      reissue,
      errorMessage
    }
  }
}
</script>
<style scoped>
#login {
  margin: 0;
  padding: 0;
  color: #000;
  overflow-x: hidden;
  height: 100%;
  background-image: linear-gradient(to right, #3F5EFB 0%, #FC466B 100%);
  height: 100vh;
}
input {
  border-radius: 50px !important;
  padding: 12px 15px 12px 15px !important;
  width: 100%;
  box-sizing: border-box;
  border: none !important;
  border: 1px solid #FC466B !important;
  font-size: 16px !important;
  color: #000 !important;
  font-weight: 400;
}
input:focus, textarea:focus {
  -moz-box-shadow: none !important;
  -webkit-box-shadow: none !important;
  box-shadow: none !important;
  border: 1px solid #3F5EFB !important;
  outline-width: 0;
  font-weight: 400;
}
button:focus {
  -moz-box-shadow: none !important;
  -webkit-box-shadow: none !important;
  box-shadow: none !important;
  outline-width: 0;
}
.card {
  border-radius: 0;
  border: none;
}
.card1 {
  width: 50%;
  padding: 40px 30px 10px 30px;
}
.card2 {
  width: 50%;
  background-image: linear-gradient(to right, #FC466B 0%, #3F5EFB 100%);
}
.form-control-label {
  font-size: 12px;
  margin-left: 15px;
}
.btn-color {
  border-radius: 50px;
  color: #fff;
  background-image: linear-gradient(to right, #FC466B 0%, #3F5EFB 100%);
  padding: 15px;
  cursor: pointer;
  border: none !important;
  margin-top: 40px;
}
.btn-color:hover {
  color: #fff;
  background-image: linear-gradient(to right, #3F5EFB, #FC466B);
}
.btn-white {
  border-radius: 50px;
  color: #D500F9;
  background-color: #fff;
  padding: 8px 40px;
  cursor: pointer;
  border: 2px solid #FC466B !important;
}
.btn-white:hover {
  color: #fff;
  background-image: linear-gradient(to right, #FC466B 0%, #3F5EFB 100%);
}
a {
  color: #000;
}
a:hover {
  color: #000;
}
.bottom {
  width: 100%;
  margin-top: 50px !important;
}
.sm-text {
  font-size: 15px;
}
@media screen and (max-width: 992px) {
  .card1 {
    width: 100%;
    padding: 40px 30px 10px 30px;
  }
  .card2 {
    width: 100%;
  }
  .right {
    margin-top: 100px !important;
    margin-bottom: 100px !important;
  }
}
@media screen and (max-width: 768px) {
  .container {
    padding: 10px !important;
  }
  .card2 {
    padding: 50px;
  }
  .right {
    margin-top: 50px !important;
    margin-bottom: 50px !important;
  }
}
</style>
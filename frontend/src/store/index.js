import { createStore } from 'vuex'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'

// 認証情報
const authModule = {
  namespaced: true,
  state: () => ({
    // ログイン状態: true: ログイン中, false: ログアウト中
    isLoggedIn: false,
    // ユーザーID
    userId: null,
    // ユーザー名
    userName: null,
    // ユーザータイプ(権限)
    userType: null,
  }),
  mutations: {
    // ユーザー情報をセット
    setUserInfo(state, userInfo) {
      // ログイン中状態に設定
      state.isLoggedIn = true
      // ユーザーIDをセット
      state.userId = userInfo.user_id
      // ユーザー名をセット
      state.userName = userInfo.user_name
      // ユーザータイプ(権限)をセット
      state.userType = userInfo.user_type
    },
    // トークン情報をセット
    setTokenInfo(state, tokenInfo) {
      // アクセストークンをローカルストレージに保存
      localStorage.setItem('accessToken', tokenInfo.access)
      // リフレッシュトークンをローカルストレージに保存
      localStorage.setItem('refreshToken', tokenInfo.refresh)
    },
    // ユーザー情報をクリア
    clearUserInfo(state) {
      // ログアウト中状態に設定
      state.isLoggedIn = false
      // ユーザーIDをクリア
      state.userId = null
      // ユーザー名をクリア
      state.userName = null
      // ユーザータイプ(権限)をクリア
      state.userType = null
    },
    // トークン情報をクリア
    clearTokenInfo() {
      // アクセストークンをローカルストレージから削除
      localStorage.removeItem('accessToken')
      // リフレッシュトークンをローカルストレージから削除
      localStorage.removeItem('refreshToken')
    },
    // アクセストークンを更新
    updateAccessToken(state, accessToken) {
      // 新しいアクセストークンをローカルストレージに保存
      localStorage.setItem('accessToken', accessToken)
    }
  },
  actions: {
    // ログイン
    login(context, userInfo) {
      // トークン情報をセット
      context.commit('setUserInfo', userInfo)
      // ユーザー情報をセット
      context.commit('setTokenInfo', userInfo)
    },
    // ログアウト
    logout(context) {
      // トークン情報をクリア
      context.commit('clearTokenInfo')
      // ユーザー情報をクリアする
      context.commit('clearUserInfo')
      // ログインページへ遷移
      router.push('/login')
    }
  }
}

export default createStore({
  modules: {
    auth: authModule
  },
  // stateの永続化設定
  plugins: [createPersistedState(
    {
      key: 'TemplateApp',
      paths: ['auth.isLoggedIn'],
      storage: localStorage
    }
  )]
})
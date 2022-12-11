import axios from 'axios'
import store from '@/store'

// axios初期設定
const api = axios.create({
  // ベースURL
  baseURL: 'http://localhost:8000/',
  // baseURL: process.env.VUE_APP_API_BASE_URL,
  // タイムアウト
  timeout: 5000,
  // ヘッダー
  headers: { 
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
  }
})

// リクエスト共通処理
api.interceptors.request.use(
  (request) => {
    // アクセストークを取得
    const accessToken = localStorage.getItem('accessToken')

    // アクセストークンをリクエストヘッダーに追加
    if (accessToken) {
      request.headers.Authorization = 'Bearer ' + accessToken
    }

    return request
  },
  (error) => {
    return Promise.reject(error)
  }
)

// レスポンス共通処理
api.interceptors.response.use(
  (response) => {
    return response
  },
  async (error) => {
     // 元のリクエスト情報
    const originalRequestConfig = error.config

    // 認証エラーの場合
    if (error.response && error.response.status === 401 && !originalRequestConfig._retry) {
      // 現在のエラーレスポンスに対してのみ有効に設定: 無限ループ対策
      originalRequestConfig._retry = true
      // 元のリクエストヘッダー情報の再代入: 再代入しないとエラーになる
      originalRequestConfig.headers = { ...originalRequestConfig.headers }
      // アクセストークン取得
      var token = await api.post('api/v1/token/refresh/', {
        refresh: localStorage.getItem('refreshToken')
      })

      if (token.status === 200) {
        // アクセストークンをローカルストレージに保存
        store.commit('auth/updateAccessToken', token.data.access)
        // 再送信リクエストヘッダーにアクセストークンをセット
        originalRequestConfig.headers.Authorization = 'Bearer ' + localStorage.getItem('accessToken')
        // アクセストークン更新前のリクエスト処理を再開
        return api.request(originalRequestConfig)
      } else {
        // アクセストークンの更新に失敗した場合
        // ログアウト処理を行いログインページへ遷移
        store.dispatch('auth/logout')
      }
    }

    return Promise.reject(error)
  }
)

export default api
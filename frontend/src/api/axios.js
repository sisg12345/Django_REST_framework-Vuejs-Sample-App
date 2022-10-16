import axios from 'axios'

// axios初期設定
const service = axios.create({
  // ベースURL
  baseURL: process.env.VUE_APP_API_BASE_URL,
  // タイムアウト
  timeout: 5000,
  // ヘッダー
  headers: {
  }
})

// リクエスト共通処理
service.interceptors.request.use(
  (request) => {
    return request
  },
  (error) => {
    return Promise.reject(error)
  }
)

// レスポンス共通処理
service.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    return Promise.reject(error)
  }
)

export default service
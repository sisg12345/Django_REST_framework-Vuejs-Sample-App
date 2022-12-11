import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'
import axios from '../api/axios.js'

const routes = [
  {
    path: '/',
    component: () => import(/* webpackChunkName: "main" */ '../views/MainView.vue'),
    children: [
      {
        path: '/',
        name: 'topPage',
        meta: { requiredAuth: true },
        component: () => import(/* webpackChunkName: "top" */ '../views/TopPageView.vue')
      },
      {
        path: '/userList',
        name: 'userList',
        meta: { requiredAuth: true },
        component: () => import(/* webpackChunkName: "user-list" */ '../views/UserListView.vue')
      },
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "login" */ '../views/LoginView.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    component: () => import(/* webpackChunkName: "not-found" */ '../views/NotFoundView.vue')
  }
]

// routerの設定
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// 画面遷移時に実行される処理
router.beforeEach((to, from, next) => {
  // ログイン情報を取得
  var isLoggedIn = store.state.auth.isLoggedIn

  // ログインが必要な画面に遷移しようとする場合
  if (to.matched.some(record => record.meta.requiredAuth)) {
    // ログインしていない場合
    if (!isLoggedIn) {
      // ログイン画面へ遷移
      next({ name: 'login' })
    } else {
      // ログインしている場合
      // リフレッシュトークンの有効チェック: 有効な場合は対象画面へ遷移, 無効な場合はログインへ遷移
      axios.post('api/v1/token/verify/', {
        token: localStorage.getItem('refreshToken')
      }).then(() => {
        // 対象画面へ遷移
        next()
      }).catch(() => {
        // ユーザー情報を破棄してログイン画面へ遷移
        store.dispatch('auth/logout')
      })
    }
  } else {
    // ログインが不要な画面の場合
    // 対象画面へ遷移
    next()
  }
})

export default router
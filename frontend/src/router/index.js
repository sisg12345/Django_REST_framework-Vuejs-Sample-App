import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import(/* webpackChunkName: "main" */ '../views/MainView.vue'),
    children: [
      {
        path: '/',
        name: 'topPage',
        component: () => import(/* webpackChunkName: "top" */ '../views/TopPageView.vue')
      },
      {
        path: '/login',
        name: 'login',
        component: () => import(/* webpackChunkName: "login" */ '../views/LoginView.vue')
      },
      {
        path: '/userList',
        name: 'userList',
        component: () => import(/* webpackChunkName: "user-list" */ '../views/UserListView.vue')
      },
      {
        path: '/:pathMatch(.*)*',
        component: () => import(/* webpackChunkName: "not-found" */ '../views/NotFoundView.vue')
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "login" */ '../views/LoginView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'topPage',
    component: () => import(/* webpackChunkName: "top-page" */ '../views/TopPageView.vue')
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

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
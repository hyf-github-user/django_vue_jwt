import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/home/Home.vue'
import Login from '../views/login/Login'
import { getToken } from '@/utils/auth'
import store from '@/store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/home',
    name: 'home',
    component: Home
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
// 路由守卫
router.beforeEach(async (to, from, next) => {
  // 判断是否有token
  const hasToken = getToken()
  if (hasToken) {
    if (to.path === '/login') {
      next()
    } else {
      // 判断是否有roles
      const hasRoles = store.getters.levels && store.getters.levels.length > 0
      if (hasRoles) {
        next()
      } else {
        // 获取身份信息
        // store.dispatch('GetInfo')
        store.dispatch('GetInfo')
        next()
      }
    }
  } else {
    if (to.path === '/login') {
      next()
    } else {
      next('/login')
    }
  }
})
export default router

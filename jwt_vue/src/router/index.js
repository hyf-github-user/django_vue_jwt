import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/login/Login'
import { getToken } from '@/utils/auth'
import store from '@/store'

Vue.use(VueRouter)

export const constantRoutes = [
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
    path: '/index',
    name: 'Index',
    component: () => import('../views/index/index.vue')
  },
  {
    path: '/404',
    component: () => import('@/views/error/index'),
    hidden: true
  }
]
export const asyncRoutes = [
  {
    path: '/home',
    name: 'home',
    component: () => import('../views/home/Home.vue'),
    meta: {
      roles: ['editor']
    }
  },
  {
    path: '/student',
    name: 'student',
    component: () => import('@/views/student/Student'),
    meta: {
      roles: ['admin']
    }
  },
  // 出错时弹出此窗口
  { path: '*', name: '404', redirect: '/404', hidden: true }
]

const router = new VueRouter({
  mode: 'history', // 去除URL带有的#号
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})
// 判断这个路由是否有权限访问
function hasPermission (roles, route) {
  if (route.meta && route.meta.roles) {
    return roles.some(role => route.meta.roles.includes(role))
  } else {
    return true
  }
}
// 根据身份权限过滤动态路由
export function filterAsyncRoutes (routes, roles) {
  const res = []
  routes.forEach(route => {
    const tmp = { ...route }
    if (hasPermission(roles, tmp)) {
      if (tmp.children) {
        // 进行递归过滤路由
        tmp.children = filterAsyncRoutes(tmp.children, roles)
      }
      res.push(tmp)
    }
  })
  return res
}
// 路由守卫
router.beforeEach(async (to, from, next) => {
  // 判断是否有token
  const hasToken = getToken()
  if (hasToken) {
    if (to.path === '/login') {
      console.log(router.getRoutes())
      next()
    } else {
      // 判断是否有roles
      const hasRoles = store.getters.levels && store.getters.levels.length > 0
      if (hasRoles) {
        next()
      } else {
        // 获取身份信息
        const { level } = await store.dispatch('GetInfo')
        let accessedRoutes
        if (level === '1') {
          accessedRoutes = filterAsyncRoutes(asyncRoutes, ['admin'])
        } else {
          accessedRoutes = filterAsyncRoutes(asyncRoutes, ['editor'])
        }

        console.log('accessedRoutes: ', accessedRoutes)
        for (let i = 0; i < accessedRoutes.length; i++) {
          router.addRoute(accessedRoutes[i])
        }
        console.log(router.getRoutes())
        store.commit('SET_ROUTES', accessedRoutes)
        // router.addRoute(accessedRoutes)
        next({ ...to, replace: true })
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

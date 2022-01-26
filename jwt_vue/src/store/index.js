import Vue from 'vue'
import Vuex from 'vuex'
import { getToken, setToken } from '@/utils/auth'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // 保存公共token
    token: getToken('token') || {}
  },
  mutations: {
    mSetTokenInfo (state, tokenObj) {
      state.token = tokenObj // 刷新会丢失所以进行持久化 调用上面storage.js文件里setItem方法保存token
      setToken('token', tokenObj)
    }
  },
  actions: {
  },
  modules: {
  }
})

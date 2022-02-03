import Vue from 'vue'
import Vuex from 'vuex'
import { getToken, setToken } from '@/utils/auth'
import { getInfo } from '@/api/user'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // 保存公共token
    token: getToken('token') || {},
    id: '',
    username: '',
    levels: []
  },
  mutations: {
    SET_TOKEN (state, token) {
      state.token = token // 刷新会丢失所以进行持久化 调用上面storage.js文件里setItem方法保存token
      setToken(token)
    },
    SET_ID: (state, id) => {
      state.id = id
    },
    SET_USERNAME: (state, username) => {
      state.username = username
    },
    SET_LEVELS: (state, level) => {
      state.levels = level
    }
  },
  actions: {
    GetInfo ({ commit, state }) {
      return new Promise((resolve, reject) => {
        // 向后台请求用户的身份权限信息
        getInfo(state.token).then(response => {
          commit('SET_ID', response.id)
          commit('SET_USERNAME', response.username)
          commit('SET_LEVELS', response.level)
        }).catch(error => {
          console.log(error)
        })
      })
    }
  },
  getters: {
    token (state) {
      return state.token
    },
    id (state) {
      return state.id
    },
    username (state) {
      return state.username
    },
    levels (state) {
      return state.levels
    }

  },
  modules: {}
})

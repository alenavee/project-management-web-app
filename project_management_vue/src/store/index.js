import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    isLoading: false,
    isAuthenticated: false,
    token: '',
    user: {
      id: 0,
      username: '',
    },
    department: {
      id: 0,
      name: '',
    }
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.username = localStorage.getItem('username')
        state.user.id = localStorage.getItem('userid')
        state.department.name = localStorage.getItem('department_name')
        state.department.id = localStorage.getItem('department_id')
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.user.id = 0
        state.user.username = ''
        state.department.id = 0
        state.department.name = ''
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    setUser(state, user) {
      state.user = user
    },
    setDepartment(state, department) {
      state.department = department

      localStorage.setItem('department_id', department.id)
      localStorage.setItem('department_name', department.name)
    }

  },
  actions: {
  },
  modules: {
  }
})


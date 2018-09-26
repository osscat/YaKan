import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    user: null,
    labels: [],
    members: []
  },
  getters: {
    getUser: state => {
      return state.user
    },
    getUserDisplayName: state => {
      if (!state.user) {
        return ''
      }
      if (state.user.last_name) {
        return state.user.last_name + ' ' + state.user.first_name
      } else {
        return state.user.username
      }
    },
    getLabels: state => {
      return state.labels
    },
    getMembers: state => {
      return state.members
    }
  },
  mutations: {
    setUser (state, user) {
      state.user = user
    },
    setLabels (state, value) {
      state.labels = value
    },
    setMembers (state, value) {
      state.members = value
    }
  }
})
export default store

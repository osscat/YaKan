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

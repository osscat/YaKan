import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    labels: [],
    members: []
  },
  getters: {
    getLabels: state => {
      return state.labels
    },
    getMembers: state => {
      return state.members
    }
  },
  mutations: {
    setLabels (state, value) {
      state.labels = value
    },
    setMembers (state, value) {
      state.members = value
    }
  }
})
export default store

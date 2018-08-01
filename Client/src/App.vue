<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'
import Header from './components/Header'

export default {
  name: 'App',
  components: {
    Header
  },
  beforeCreate: function () {
    axios.interceptors.response.use(
      response => response,
      error => {
        if (error.response.status === 401) {
          delete axios.defaults.headers.common['Authorization']
          this.$router.push({name: 'Login'})
        }
        return Promise.reject(error)
      }
    )
  }
}
</script>

<style>

</style>

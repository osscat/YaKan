<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  beforeCreate: function () {
    axios.interceptors.response.use(
      response => response,
      error => {
        if (error.response.status === 401) {
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

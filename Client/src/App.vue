<template>
  <el-container>
    <el-header>
      <Header/>
    </el-header>
    <el-container>
      <el-main>
        <div id="app">
          <router-view/>
        </div>
      </el-main>
    </el-container>
  </el-container>
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

/**
 *  ログインコンポーネント。
 */
<template>
  <div>
    <div class="flex-container">
      <div class="flex-container2">
        <div style="text-align:center;font-size:30px;">Welcome to Yakan!</div>
        <img src="../assets/yakan.jpg" />
        <br>
        <input v-model="username" type="text" placeholder="username">
        <input v-model="password" type="password" placeholder="password">
        <button @click="login()">GO</button>
        {{message}}
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const URL = process.env.API_BASE_URL + '/rest-auth/login/'

export default {
  name: 'Login',
  data () {
    return {
      message: null,
      username: null,
      password: null
    }
  },
  methods: {
    login: function () {
      this.message = null
      axios
        .post(URL, {
          username: this.username,
          password: this.password
        })
        .then(
          response => {
            axios.defaults.headers.common['Authorization'] = 'JWT ' + response.data.token
            this.$router.push({name: 'Top'})
          }
        )
        .catch(
          error => {
            if (error.response.data.non_field_errors) {
              this.message = error.response.data.non_field_errors[0]
            }
          }
        )
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.flex-container {
  display: flex;
  justify-content: center;
}
.flex-container2 {
  display: flex;
  flex-direction: column;
}
</style>

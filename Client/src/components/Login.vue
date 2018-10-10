/**
 *  ログインコンポーネント。
 */
<template>
  <div class="flex-container">
    <div class="flex-container2">
      <h2>Welcome to Yakan!</h2>
      <img src="../assets/yakan.jpg" width="300px" height="200px" />
      <br>
      <el-alert v-if="message" :title="message" type="error"></el-alert>
      <el-form ref="form" :model="form" label-width="100px" @submit.native.prevent="login">
        <el-form-item label="ユーザー名">
          <el-input name="username" v-model="form.username" autofocus="true" auto-complete="on"></el-input>
        </el-form-item>
        <el-form-item label="パスワード">
          <el-input name="password" type="password" v-model="form.password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" native-type="submit">ログイン</el-button>
        </el-form-item>
      </el-form>
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
      form: {
        username: null,
        password: null
      }
    }
  },
  methods: {
    login: function () {
      this.message = null
      axios
        .post(URL, {
          username: this.form.username,
          password: this.form.password
        })
        .then(
          response => {
            axios.defaults.headers.common['Authorization'] = 'JWT ' + response.data.token
            this.$router.push({name: 'Project'})
            this.$store.commit('setUser', response.data.user)
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
.el-alert {
  margin-bottom: 15px;
}
</style>

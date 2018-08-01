/**]
 *  ヘッダーコンポーネント。
 */
<template>
  <div>
    <div class="line"></div>
    <el-menu default-active="1"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="1" @click="$router.push({name: 'Project'})">プロジェクト一覧</el-menu-item>
      <el-menu-item index="9" @click="$router.push({name: 'UserAdmin'})">ユーザー管理</el-menu-item>
      <el-submenu index="10" class="loginuser">
        <template slot="title">{{ displayName }} さん</template>
        <el-menu-item index="10-1">ユーザー情報編集</el-menu-item>
        <el-menu-item index="10-2" @click="changePasswordFormVisible = true">パスワード変更</el-menu-item>
        <el-menu-item index="10-3" @click="logout">ログアウト</el-menu-item>
      </el-submenu>
    </el-menu>
    <ChangePasswordForm :visible.sync="changePasswordFormVisible" />
  </div>
</template>

<script>
import axios from 'axios'
import ChangePasswordForm from './ChangePasswordForm'

const URL_USER = process.env.API_BASE_URL + '/rest-auth/user/'
const URL_LOGOUT = process.env.API_BASE_URL + '/rest-auth/logout/'

export default {
  name: 'Header',
  data () {
    return {
      user: null,
      changePasswordFormVisible: false
    }
  },
  components: {
    ChangePasswordForm
  },
  mounted () {
    axios
      .get(URL_USER)
      .then(
        response => {
          this.user = response.data
        }
      )
  },
  computed: {
    displayName () {
      if (!this.user) {
        return ''
      }
      if (this.user.last_name) {
        return this.user.last_name + ' ' + this.user.first_name
      } else {
        return this.user.username
      }
    }
  },
  methods: {
    logout () {
      axios.post(URL_LOGOUT)
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style scoped>
.loginuser {
  float: right
}
</style>

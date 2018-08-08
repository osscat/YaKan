/**]
 *  ヘッダーコンポーネント。
 */
<template>
  <div>
    <div class="line"></div>
    <el-dropdown class="user-menu">
      <span class="el-dropdown-link">
        {{ displayName }} さん<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item @click.native="editAccountFormVisible = true">ユーザー情報編集</el-dropdown-item>
        <el-dropdown-item @click.native="changePasswordFormVisible = true">パスワード変更</el-dropdown-item>
        <el-dropdown-item @click.native="logout">ログアウト</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
    <el-menu default-active="/"
      mode="horizontal"
      router="true"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="/">プロジェクト</el-menu-item>
      <el-menu-item index="/userAdmin">ユーザー管理</el-menu-item>
    </el-menu>
    <EditAccountForm :visible.sync="editAccountFormVisible" :user="user" @save="loadUser" />
    <ChangePasswordForm :visible.sync="changePasswordFormVisible" />
  </div>
</template>

<script>
import axios from 'axios'
import EditAccountForm from './EditAccountForm'
import ChangePasswordForm from './ChangePasswordForm'

const URL_USER = process.env.API_BASE_URL + '/rest-auth/user/'
const URL_LOGOUT = process.env.API_BASE_URL + '/rest-auth/logout/'

export default {
  name: 'Header',
  data () {
    return {
      user: null,
      editAccountFormVisible: false,
      changePasswordFormVisible: false
    }
  },
  components: {
    EditAccountForm,
    ChangePasswordForm
  },
  mounted () {
    this.loadUser()
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
    loadUser () {
      axios
        .get(URL_USER)
        .then(
          response => {
            this.user = response.data
          }
        )
    },
    logout () {
      axios.post(URL_LOGOUT)
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style scoped>
.user-menu {
  float: right;
  z-index: 1;
  line-height: 60px;
  margin-right: 20px;
  color: white;
}
</style>

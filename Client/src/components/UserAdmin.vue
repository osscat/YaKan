/**
 *  ユーザー管理コンポーネント。
 */
<template>
  <div>
    <h2>ユーザー</h2>
    <el-table :data="users" :default-sort = "{prop: 'username', order: 'ascending'}">
      <el-table-column prop="username" label="ユーザー名" sortable></el-table-column>
      <el-table-column prop="last_name" label="姓" sortable></el-table-column>
      <el-table-column prop="first_name" label="名" sortable></el-table-column>
      <el-table-column prop="is_active" label="有効" sortable>
        <template slot-scope="{ row: user }">
          <span>{{user.is_active}}</span>
          <el-button v-if="user.is_active" type="danger" size="small" @click="toggleActive(user)">無効化する</el-button>
          <el-button v-if="!user.is_active" type="success" size="small" @click="toggleActive(user)">有効化する</el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="action">
      <el-button @click="formVisible = true">ユーザーを追加</el-button>
    </div>

    <el-dialog title="ユーザー追加" :visible.sync="formVisible">
      <el-alert v-if="message" :title="message" type="error"></el-alert>
      <el-form :model="form">
        <el-form-item label="ユーザー名">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="パスワード">
          <el-input type="password" v-model="form.password1"></el-input>
        </el-form-item>
        <el-form-item label="パスワード（確認）">
          <el-input type="password" v-model="form.password2"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="formVisible = false">キャンセル</el-button>
        <el-button type="primary" @click="save">保存</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import axios from 'axios'

const URL_LIST = process.env.API_BASE_URL + '/api/users/'
const URL_REGISTRATION = process.env.API_BASE_URL + '/rest-auth/registration/'

export default {
  name: 'UserAdmin',
  data () {
    return {
      users: null,
      message: null,
      formVisible: false,
      form: {
        username: null,
        password1: null,
        password2: null
      }
    }
  },
  mounted () {
    this.load()
  },
  methods: {
    load: function () {
      axios
        .get(URL_LIST)
        .then(
          response => {
            this.users = response.data
          }
        )
    },
    toggleActive: function (user) {
      this.message = null
      axios
        .patch(URL_LIST + user.id + '/', {
          is_active: !user.is_active
        })
        .then(
          response => {
            this.load()
          }
        )
        .catch(
          error => {
            this.message = error.response.data
          }
        )
    },
    save: function () {
      this.message = null
      axios
        .post(URL_REGISTRATION, {
          username: this.form.username,
          password1: this.form.password1,
          password2: this.form.password2
        })
        .then(
          response => {
            this.load()
            this.formVisible = false
          }
        )
        .catch(
          error => {
            this.message = error.response.data
          }
        )
    }
  }
}
</script>

<style>
.el-table .el-button {
  float: right;
}
.action {
  margin-top: 30px;
}
</style>

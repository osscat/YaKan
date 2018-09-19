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
          <span>{{user.is_active ? 'はい' : 'いいえ'}}</span>
          <span v-if="canDeactivate(user)">
            <el-button v-if="user.is_active" type="danger" size="small" @click="toggleActive(user)">無効化する</el-button>
            <el-button v-if="!user.is_active" type="success" size="small" @click="toggleActive(user)">有効化する</el-button>
          </span>
        </template>
      </el-table-column>
    </el-table>
    <div class="action">
      <el-button @click="formVisible = true">ユーザーを追加</el-button>
    </div>

    <el-dialog title="ユーザー追加" :visible.sync="formVisible" @closed="onClosed">
      <el-alert v-for="(error, index) in errors" :key="index" :title="error" type="error"></el-alert>
      <el-form :model="form" ref="form" :rules="rules">
        <el-form-item label="ユーザー名" prop="username">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="パスワード" prop="password1">
          <el-input type="password" v-model="form.password1"></el-input>
        </el-form-item>
        <el-form-item label="パスワード（確認）" prop="password2">
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
      errors: [],
      formVisible: false,
      form: {
        username: null,
        password1: null,
        password2: null
      },
      rules: {
        username: [
          { required: true, message: '入力してください', trigger: 'blur' }
        ],
        password1: [
          { required: true, message: '入力してください', trigger: 'blur' },
          { min: 8, message: '8文字以上にしてください', trigger: 'blur' }
        ],
        password2: [
          { required: true, message: '入力してください', trigger: 'blur' },
          { min: 8, message: '8文字以上にしてください', trigger: 'blur' }
        ]
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
    canDeactivate: function (user) {
      return !user.is_staff && !user.is_admin
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
    onClosed: function () {
      this.load()
      this.formVisible = false
      this.$refs.form.resetFields()
      this.errors = []
    },
    save: function () {
      this.$refs.form.validate(
        valid => {
          if (valid) {
            this.doSave()
          }
        }
      )
    },
    doSave: function () {
      this.errors = []
      axios
        .post(URL_REGISTRATION, {
          username: this.form.username,
          password1: this.form.password1,
          password2: this.form.password2
        })
        .then(
          response => {
            this.onClosed()
          }
        )
        .catch(
          error => {
            const response = error.response.data
            for (const key in response) {
              if (response.hasOwnProperty(key)) {
                this.errors.push(...response[key])
              }
            }
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

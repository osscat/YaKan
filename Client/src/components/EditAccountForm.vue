/**
 *  ユーザー情報変更画面コンポーネント。
 */
<template>
  <el-dialog title="ユーザー情報変更" width="400px" :visible.sync="dialogVisible" @open="onOpen" @closed="onClosed" :append-to-body="true">
    <el-alert v-for="(error, index) in errors" :key="index" :title="error" type="error"></el-alert>
    <el-form :model="form" ref="form" label-width="100px">
      <el-form-item label="ユーザー名" prop="username">
        <el-input v-model="form.username" :disabled="true"></el-input>
      </el-form-item>
      <el-form-item label="姓" prop="last_name">
        <el-input v-model="form.last_name"></el-input>
      </el-form-item>
      <el-form-item label="名" prop="first_name">
        <el-input v-model="form.first_name"></el-input>
      </el-form-item>
    </el-form>
    <span slot="footer" class="dialog-footer">
      <el-button @click="onClosed">キャンセル</el-button>
      <el-button type="primary" @click="save">保存</el-button>
    </span>
  </el-dialog>
</template>

<script>
import axios from 'axios'

const URL = process.env.API_BASE_URL + '/rest-auth/user/'

export default {
  name: 'EditAccountForm',
  props: ['visible'],
  data () {
    return {
      errors: [],
      dialogVisible: this.visible,
      form: {
        username: null,
        first_name: null,
        last_name: null
      }
    }
  },
  watch: {
    visible: function (value) {
      this.dialogVisible = value
    }
  },
  methods: {
    onOpen: function () {
      let user = this.$store.getters.getUser
      this.form.username = user.username
      this.form.first_name = user.first_name
      this.form.last_name = user.last_name
    },
    onClosed: function () {
      this.dialogVisible = false
      this.$emit('update:visible', false)
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
        .patch(URL, {
          first_name: this.form.first_name,
          last_name: this.form.last_name
        })
        .then(
          response => {
            this.onClosed()
            this.$store.commit('setUser', response.data)
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
.el-alert {
  margin-bottom: 20px;
}
</style>

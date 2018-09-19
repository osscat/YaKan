/**
 *  パスワード変更画面コンポーネント。
 */
<template>
  <el-dialog title="パスワード変更" width="500px" :visible.sync="dialogVisible" @closed="onClosed" :append-to-body="true">
    <el-alert v-for="(error, index) in errors" :key="index" :title="error" type="error"></el-alert>
    <el-form :model="form" ref="form" label-width="180px">
      <el-form-item label="新パスワード" :rules="rules" prop="new_password1">
        <el-input type="password" v-model="form.new_password1"></el-input>
      </el-form-item>
      <el-form-item label="新パスワード（確認）" :rules="rules" prop="new_password2">
        <el-input type="password" v-model="form.new_password2"></el-input>
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

const URL = process.env.API_BASE_URL + '/rest-auth/password/change/'

export default {
  name: 'ChangePasswordForm',
  props: ['visible'],
  data () {
    return {
      errors: [],
      dialogVisible: this.visible,
      form: {
        new_password1: null,
        new_password2: null
      },
      rules: [
        {
          required: true,
          message: '入力してください',
          trigger: 'blur'
        },
        {
          min: 8,
          message: '8文字以上にしてください',
          trigger: 'blur'
        }
      ]
    }
  },
  watch: {
    visible: function (value) {
      this.dialogVisible = value
    }
  },
  methods: {
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
        .post(URL, {
          new_password1: this.form.new_password1,
          new_password2: this.form.new_password2
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
.el-alert {
  margin-bottom: 20px;
}
</style>

/**
 *  プロジェクトを編集するダイアログフォームのコンポーネント。
 */
<template>
  <div>
    <el-alert v-for="(error, index) in errors" :key="index" :title="error" type="error"></el-alert>
    <el-form :model="form" ref="form" :rules="rules">
      <el-form-item label="プロジェクトタイトル" prop="title">
        <el-input :value="project.title" v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item label="プロジェクト説明" prop="description">
        <el-input type="textarea" rows="4" :value="project.description" v-model="form.description"></el-input>
      </el-form-item>
    </el-form>
    <span slot="footer" class="dialog-footer">
      <el-button @click="onClosed">キャンセル</el-button>
      <el-button type="primary" @click="updateProject">更新</el-button>
    </span>
  </div>
</template>

<script>
import axios from 'axios'

const PROJECT_URL = process.env.API_BASE_URL + '/api/projects/'

export default {
  name: 'AddTaskForm',
  props: ['project'],
  data () {
    return {
      errors: [],
      form: {
        title: this.project.title,
        description: this.project.description
      },
      rules: {
        title: [
          { required: true, message: '入力してください', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    onClosed: function () {
      this.$emit('close')
      this.form.title = this.project.title
      this.form.description = this.project.description
    },
    updateProject: function () {
      this.project.title = this.form.title
      this.project.description = this.form.description
      axios
        .put(PROJECT_URL + this.project.id + '/', this.project)
        .then(response => {
          console.log(response)
          this.onClosed()
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-table .el-button {
  float: right;
}
</style>

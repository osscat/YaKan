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
      <el-button type="primary">更新</el-button>
    </span>
  </div>
</template>

<script>
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

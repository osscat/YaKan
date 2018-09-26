/**
 *  プロジェクトを編集するダイアログフォームのコンポーネント。
 */
<template>
  <div>
    <el-form :model="form">
      <el-form-item label="プロジェクトタイトル">
        <el-input :value="project.title"></el-input>
      </el-form-item>
      <el-form-item label="プロジェクト説明">
        <el-input type="textarea" rows="4" :value="project.description"></el-input>
      </el-form-item>
    </el-form>
    <span slot="footer" class="dialog-footer">
      <el-button>キャンセル</el-button>
      <el-button type="primary">作成</el-button>
    </span>
  </div>
</template>

<script>
const TASK_POST_URL = process.env.API_BASE_URL + '/api/tasks/'

export default {
  name: 'AddTaskForm',
  props: ['project'],
  data () {
    return {
      errors: [],
      form: {
        title: null,
        manday: null,
        order: 0,
        user: null,
        label: null
      },
      rules: {
        title: [
          { required: true, message: '入力してください', trigger: 'blur' }
        ],
        manday: [
          { required: true, message: '入力してください', trigger: 'blur' }
        ],
        order: [
          { required: true, message: '入力してください', trigger: 'blur' }
        ]
      }
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

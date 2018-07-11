/**
 *  タスクを追加するボタンのコンポーネント。
 */
<template>
  <div style="float: right;">
    <el-button type="primary" icon="el-icon-plus" circle @click="dialogFormVisible = true"></el-button>
    <el-dialog title="タスク作成" :visible.sync="dialogFormVisible" :laneid="laneid">
        <AddTaskForm :laneid="this.laneid"></AddTaskForm>
    </el-dialog>
  </div>
</template>

<script>
import AddTaskForm from './AddTaskForm'

export default {
  name: 'AddTaskButton',
  props: ['laneid'],
  components: {
    AddTaskForm
  },
  data () {
    return {
      dialogFormVisible: false,
      formLabelWidth: '120px'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

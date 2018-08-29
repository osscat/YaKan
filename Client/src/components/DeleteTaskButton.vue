/**
 *  タスクを削除するボタンのコンポーネント。
 */
<template>
  <div class="delete-button">
    <el-button type="danger" icon="el-icon-delete" circle @click="openConfirm"></el-button>
  </div>
</template>

<script>
import axios from 'axios'
import { EV_TASK } from '../plugins/WebSocket'

const TASK_DELETE_URL = process.env.API_BASE_URL + '/api/tasks/'

export default {
  name: 'DeleteTaskButton',
  props: ['task'],
  methods: {
    openConfirm: function () {
      this.$confirm('タスクを削除しますか?', '削除確認', {
        confirmButtonText: '削除',
        cancelButtonText: 'キャンセル',
        type: 'Confirm'
      }).then(() => {
        this.deleteTask()
        this.$message({
          type: 'success',
          message: '削除しました。'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: 'キャンセルしました。'
        })
      })
    },
    deleteTask: function () {
      var url = TASK_DELETE_URL + this.task.id + '/'
      axios
        .delete(url)
        .then(response => {
          if (response.status === 204) {
            this.$webSocket.send(EV_TASK, this.task.lane_id)
          }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.delete-button {
  float: right;
  margin-top: 5px;
  margin-bottom: 5px;
}
</style>

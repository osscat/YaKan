/**
 *  レーンを削除するボタンのコンポーネント。
 */
<template>
  <div style="float: right;">
    <el-button type="danger" icon="el-icon-delete" circle @click="openConfirm"></el-button>
  </div>
</template>

<script>
import axios from 'axios'
import { EV_PROJECT } from '../plugins/WebSocket'

const LANE_DELETE_URL = process.env.API_BASE_URL + '/api/lanes/'
const TASK_DELETE_URL = process.env.API_BASE_URL + '/api/tasks/'

export default {
  name: 'DeleteLaneButton',
  props: ['lane'],
  methods: {
    openConfirm: function () {
      this.$confirm('レーンを削除しますか?', '削除確認', {
        confirmButtonText: '削除',
        cancelButtonText: 'キャンセル',
        type: 'Confirm'
      }).then(() => {
        this.deleteLane()
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
    deleteLane: function () {
      var url = LANE_DELETE_URL + this.lane.id + '/'
      axios
        .delete(url)
        .then(response => {
          console.log(response)
          if (response.status === 204) {
            this.deletetasks()
            this.$webSocket.send(EV_PROJECT, this.lane.project_id)
          }
        })
    },
    deletetasks: function () {
      // TODO:物理削除じゃなくて論理削除？
      var url = TASK_DELETE_URL + '?lane_id=' + this.lane.id
      axios
        .delete(url)
        .then(response => {
          console.log(response)
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

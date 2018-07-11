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

const LANE_DELETE_URL = 'http://localhost:8000/api/lanes/'
const TASK_DELETE_URL = 'http://localhost:8000/api/tasks/'

export default {
  name: 'DeleteLaneButton',
  props: ['laneid'],
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
      var url = LANE_DELETE_URL + this.laneid + '/'
      axios
        .delete(url)
        .then(response => {
          console.log(response)
          if (response.status === 204) {
            this.deletetasks()
          }
        })
      this.removeElement(this.laneid)
    },
    deletetasks: function () {
      // TODO:物理削除じゃなくて論理削除？
      var url = TASK_DELETE_URL + '?lane_id=' + this.laneid
      axios
        .delete(url)
        .then(response => {
          console.log(response)
        })
    },
    removeElement: function (id) {
      var data = this.$parent.$parent.lanes.filter(
        function (item, index) {
          if (item.id !== id) {
            return true
          }
        }
      )
      this.$parent.$parent.lanes = data
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

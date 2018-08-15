/**
 *  プロジェクトを削除するボタンのコンポーネント。
 */
<template>
  <el-button type="danger" icon="el-icon-delete" circle @click="openConfirm"></el-button>
</template>

<script>
import { EV_PROJECT_LIST } from '../plugins/WebSocket'
import axios from 'axios'

const PROJECT_DELETE_URL = process.env.API_BASE_URL + '/api/projects/'

export default {
  name: 'DeleteProjectButton',
  props: ['project'],
  methods: {
    openConfirm: function () {
      this.$confirm('プロジェクトを削除しますか?', '削除確認', {
        confirmButtonText: '削除',
        cancelButtonText: 'キャンセル',
        type: 'Confirm'
      }).then(() => {
        this.deleteProject()
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
    deleteProject: function () {
      var url = PROJECT_DELETE_URL + this.project.id + '/'
      axios
        .delete(url)
        .then(response => {
          this.$webSocket.send(EV_PROJECT_LIST)
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

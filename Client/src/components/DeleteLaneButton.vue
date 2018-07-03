/**
 *  レーンを削除するボタンのコンポーネント。
 */
<template>
  <button type="button" @click="deleteLane">
    削除
  </button>
</template>

<script>
import axios from 'axios'

const LANE_DELETE_URL = 'http://localhost:8000/api/lanes/'
const TASK_DELETE_URL = 'http://localhost:8000/api/tasks/'

export default {
  name: 'DeleteLaneButton',
  props: ['laneid'],
  methods: {
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

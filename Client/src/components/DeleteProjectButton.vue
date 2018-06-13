/**
 *  プロジェクトを削除するボタンのコンポーネント。
 */
<template>
  <button type="button" @click="deleteProject">
    削除
  </button>
</template>

<script>
import axios from 'axios'

const PROJECT_DELETE_URL = 'http://localhost:8000/api/projects/'

export default {
  name: 'DeleteProjectButton',
  props: ['project'],
  methods: {
    deleteProject: function () {
      var url = PROJECT_DELETE_URL + this.project.id + "/"
      axios
        .delete(url)
        .then(response => { console.log(response); this.project = null })
      this.removeElement(this.project.id)
    },
    removeElement: function (id) {
      var data = this.$parent.$parent.projects.filter(
        function (item, index) {
          if (item.id !== id) {
            return true
          }
        }
      )
      this.$parent.$parent.projects = data
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

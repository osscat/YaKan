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

const PROJECT_DELETE_URL = process.env.API_BASE_URL + '/api/projects/'

export default {
  name: 'DeleteProjectButton',
  props: ['project'],
  methods: {
    deleteProject: function () {
      var url = PROJECT_DELETE_URL + this.project.id + '/'
      axios
        .delete(url)
        .then(response => {
          this.$parent.$parent.$parent.$parent.send('delete')
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

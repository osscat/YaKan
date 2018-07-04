/**
 *  プロジェクトを追加するフォームのコンポーネント。
 */
<template>
  <form>
    プロジェクト名<input type="text" id="title" />
    <button type="button" @click="addProject">
      登録
    </button>
  </form>
</template>

<script>
import axios from 'axios'

const PROJECT_POST_URL = 'http://127.0.0.1:8000/api/projects/'

export default {
  name: 'AddProjectForm',
  methods: {
    addProject: function () {
      axios
        .post(PROJECT_POST_URL, {
          title: document.getElementById('title').value,
          owner_id: 3
        })
        .then(response => {
          this.$parent.projects.push(response.data)
          this.$parent.$parent.loadList()
          document.getElementById('title').value = ''
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

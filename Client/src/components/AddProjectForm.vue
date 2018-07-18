/**
 *  プロジェクトを追加するフォームのコンポーネント。
 */
<template>
  <form>
    <el-input id="title" class="newtitle" placeholder="Please input Project-Title" v-model="newtitle"></el-input>
    <el-button type="primary" @click="addProject">作成</el-button>
  </form>
</template>

<script>
import axios from 'axios'

const PROJECT_POST_URL = process.env.API_BASE_URL + '/api/projects/'

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
          this.$parent.$parent.send('add')
          document.getElementById('title').value = ''
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.newtitle {
  width: 200px;
}
</style>

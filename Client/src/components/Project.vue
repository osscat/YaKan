/**
 *  プロジェクトの一覧を表示するコンポーネント。
 */
<template>
  <div class="flex-container">
    <div v-for="project in projects" :key="project.id">
      <ProjectSub :project="project" />
    </div>
    <AddProjectForm />
  </div>
</template>

<script>
import axios from 'axios'
import ProjectSub from './ProjectSub'
import AddProjectForm from './AddProjectForm'

const LIST_URL = 'http://127.0.0.1:8000/api/projects/?format=json'

export default {
  name: 'Project',
  components: {
    ProjectSub,
    AddProjectForm
  },
  data () {
    return {
      projects: null
    }
  },
  mounted () {
    this.loadList()
  },
  methods: {
    loadList: function () {
      axios
        .get(LIST_URL)
        .then(response => (this.projects = response.data))
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.flex-container {
  display: flex;
  position: fixed;
  width: 100%;
  height: 100%;
  padding: 10px;
  overflow: scroll;
  background-color: #F5F5DC;
}
</style>

/**
 *  プロジェクトの一覧を表示するコンポーネント。
 */
<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item>プロジェクト一覧</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="search-sticky">
      <form>
        <el-input size="medium" placeholder="Project Name" class="search" v-model="word" @keyup.native="loadList(word)"></el-input>
        <el-button size="medium" type="info" icon="el-icon-search" @click="loadList(word)">検索</el-button>
      </form>
    </div>
    <br>
    <AddProjectForm />
    <br>
    <transition-group name="demo" tag="div" class="flex-project">
      <div v-for="project in projects" :key="project.id">
        <ProjectSub :project="project" />
      </div>
    </transition-group>
  </div>
</template>

<script>
import ProjectSub from './ProjectSub'
import AddProjectForm from './AddProjectForm'
import { EV_PROJECT } from '../plugins/WebSocket'
import axios from 'axios'

const LIST_URL = process.env.API_BASE_URL + '/api/projects2/filter/'

export default {
  name: 'Project',
  components: {
    ProjectSub,
    AddProjectForm
  },
  data () {
    return {
      projects: null,
      word: null
    }
  },
  mounted () {
    this.$webSocket.$on(EV_PROJECT, this.loadList)
    this.loadList()
  },
  methods: {
    loadList: function (word) {
      var url = LIST_URL + '?user_id=' + this.$store.getters.getUser.pk
      if (word) {
        url += '&title=' + word
      }
      axios
        .get(url)
        .then(
          response => {
            this.projects = JSON.parse(response.data)
          }
        )
    }
  }
}
</script>

<style scoped>
.search-sticky {
  width: 320px;
  overflow: visible;
  position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 60px;
  background: rgba(100,100,0,0.2);
  padding: 5px;
  z-index: 1;
}
.el-breadcrumb {
  margin-bottom: 20px;
}
.flex-project {
  width: 100%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
.flex-project2 {
  width: 100%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
.demo-enter-active, .demo-leave-active {
  transition: transform .5s, opacity .5s;
}
.demo-move:not(.demo-leave-active) {
  transition: transform .5s;
}
/* 消える時は縮小される */
.demo-leave-to {
  opacity: 0;
  transform: scale(0.8);
}
.demo-leave-active {
  position: absolute;
}
.search {
  margin-bottom: 10px;
  width: 200px;
}
</style>

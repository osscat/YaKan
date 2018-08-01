/**
 *  プロジェクトの一覧を表示するコンポーネント。
 */
<template>
  <div>
    <form>
      <i class="el-icon-search"></i>
      <span>検索</span>
      <el-input placeholder="Project Name" class="search" v-model="word" @keyup.native="loadList(word)"></el-input>
    </form>
    <transition-group name="demo" tag="div" class="flex-project">
      <div v-for="project in projects" :key="project.id">
        <ProjectSub :project="project" />
      </div>
    </transition-group>
    <AddProjectForm style="margin-top: 5px;"/>
  </div>
</template>

<script>
import ProjectSub from './ProjectSub'
import AddProjectForm from './AddProjectForm'
import axios from 'axios'

const LIST_URL = process.env.API_BASE_URL + '/api/projects/'
const SERVER_ADDRESS = process.env.SERVER_ADDRESS

var chatSocket

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
    this.initWebSocket()
    this.loadList()
  },
  methods: {
    initWebSocket: function () {
      var serverHost = SERVER_ADDRESS
      chatSocket = new WebSocket(
        'ws://' + serverHost +
        '/ws/chat/echo/')

      chatSocket.onmessage = this.onMessage

      chatSocket.onclose = function (e) {
        console.error('Chat socket closed unexpectedly')
      }
    },
    // **
    //  * 処理の種類を WebSocket でサーバーに送ります。
    //  * transaction : add, delete
    //  *
    send: function (transaction) {
      console.log(transaction)
      chatSocket.send(JSON.stringify({
        'transaction': transaction
      }))
    },
    onMessage: function (e) {
      this.loadList()
    },
    loadList: function (word) {
      var url = LIST_URL
      if (word) {
        url += '?title=' + word
      }
      axios
        .get(url)
        .then(
          response => {
            this.projects = response.data
            console.log(response.data)
          }
        )
    }
  }
}
</script>

<style scoped>
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

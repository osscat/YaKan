/**
 *  Top コンポーネント。
 */
<template>
  <div class="flex-container">
    <Header />
    <Project :projects="projects" />
  </div>
</template>

<script>
import axios from 'axios'
import Header from './Header'
import Project from './Project'

const LIST_URL = 'http://127.0.0.1:8000/api/projects/'

var chatSocket

export default {
  name: 'Login',
  data () {
    return {
      projects: null
    }
  },
  components: {
    Header,
    Project
  },
  mounted () {
    this.initWebSocket()
    this.loadList()
  },
  methods: {
    initWebSocket: function () {
      var serverHost = 'localhost:8000'
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
      axios
        .get(LIST_URL)
        .then(
          response => {
            this.projects = response.data
            this.search(word)
          }
        )
    },
    search: function (word) {
      if (!word) {
        return
      }
      var data = this.projects.filter(
        function (item, index) {
          if (item.title.indexOf(word) !== -1) {
            return true
          }
        }
      )
      console.log(data)
      this.projects = data
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.flex-container {
  display: flex;
  flex-wrap: wrap;
}
</style>

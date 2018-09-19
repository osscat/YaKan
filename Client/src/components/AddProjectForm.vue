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
import { EV_PROJECT } from '../plugins/WebSocket'
import axios from 'axios'

const PROJECT_POST_URL = process.env.API_BASE_URL + '/api/projects/'
const MEMBER_URL = process.env.API_BASE_URL + '/api/projectmembers/'
const URL_USER = process.env.API_BASE_URL + '/rest-auth/user/'

export default {
  name: 'AddProjectForm',
  data () {
    return {
      user: null,
      newtitle: null
    }
  },
  methods: {
    addMember: function (projectId, userId) {
      axios
        .post(MEMBER_URL, {
          project_id: projectId,
          user_id: userId
        })
    },
    addProject: function () {
      axios
        .post(PROJECT_POST_URL, {
          title: this.newtitle,
          owner_id: this.user.pk
        })
        .then(response => {
          this.$parent.projects.push(response.data)
          this.$webSocket.send(EV_PROJECT)
          this.newtitle = ''
          this.addMember(response.data.id, this.user.pk)
        })
    },
    loadUser: function () {
      axios
        .get(URL_USER)
        .then(
          response => {
            this.user = response.data
          }
        )
    }
  },
  mounted () {
    this.loadUser()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.newtitle {
  width: 200px;
}
</style>

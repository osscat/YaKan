/**
 *  担当者を選択するコンポーネント。
 */
<template>
  <div>
    <el-select v-model="value" filterable clearable remote reserve-keyword placeholder="Select User"
      :remote-method="remoteMethod"
      :loading="loading"
      @change="updateuser">
      <el-option
        v-for="user in users"
        :key="user.value"
        :label="user.label"
        :value="user.value">
      </el-option>
    </el-select>
  </div>
</template>

<script>
import axios from 'axios'

const USER_URL = process.env.API_BASE_URL + '/api/users/'
const PROJECTMEMBER_URL = process.env.API_BASE_URL + '/api/projectmembers/'

export default {
  name: 'SelectUser',
  props: ['projectid', 'selected'],
  data () {
    return {
      users: [],
      value: null,
      list: [],
      members: [],
      loading: false
    }
  },
  mounted () {
    this.loadProjectMembers() // TODO:1回だけ。
  },
  methods: {
    loadProjectMembers: function () {
      var url = PROJECTMEMBER_URL
      if (this.projectid) {
        url += ('?project_id=' + this.projectid)
      }
      axios
        .get(url)
        .then(
          response => {
            if (response.data && response.data.length > 0) {
              for (let i = 0; i < response.data.length; i++) {
                this.members.push(response.data[i].user_id)
              }
              if (this.members && this.members.length > 0) {
                this.loadUser() // 全ユーザーを取得
              }
            } else {
              console.log('プロジェクトメンバーがいません')
            }
          }
        )
    },
    loadUser: function () {
      axios
        .get(USER_URL)
        .then(
          response => {
            for (let i = 0; i < response.data.length; i++) {
              var userid = response.data[i].id
              var username = response.data[i].username
              if (this.members.indexOf(userid) > -1) { // プロジェクトメンバーのみ
                this.list.push({ value: userid, label: username })
              }
            }
            this.users = this.list
            if (this.selected) {
              this.value = this.selected
            }
          }
        )
    },
    updateuser: function () {
      if (this.value === '') {
        this.users = this.list
      }
      this.$parent.$parent.changeUser(this.value)
    },
    remoteMethod: function (query) {
      if (query !== '') {
        this.loading = true
        setTimeout(() => {
          this.loading = false
          this.users = this.list.filter(user => {
            return user.label.toLowerCase().indexOf(query.toLowerCase()) > -1
          })
        }, 200)
      } else {
        this.users = this.list
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

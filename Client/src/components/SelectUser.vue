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

export default {
  name: 'SelectUser',
  props: ['selected'],
  data () {
    return {
      users: [],
      value: null,
      list: [],
      loading: false
    }
  },
  mounted () {
    this.loadUser() // TODO:1回だけ。
  },
  methods: {
    loadUser: function () {
      axios
        .get(USER_URL)
        .then(
          response => {
            this.list = response.data.map(user => {
              return { value: user.id, label: user.username }
            })
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

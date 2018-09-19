/**
 *  プロジェクトのメンバーを表示、編集するコンポーネント。
 */
<template>
  <div class="project-member">
    <el-dropdown :hide-on-click="false">
      <span class="el-dropdown-link">
        メンバー<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item v-for="member in members" :key="member.id">
          <i class="el-icon-close" @click="removeMember(member)"></i>
          {{member.user.username}}
        </el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
    <el-select v-model="selectedId" placeholder="追加したいユーザー">
      <el-option
        v-for="user in selectableUsers"
        :key="user.id"
        :label="user.username"
        :value="user.id">
      </el-option>
    </el-select>
    <el-button type="primary" @click="addMember">追加</el-button>
  </div>
</template>

<script>
import axios from 'axios'

const MEMBER_URL = process.env.API_BASE_URL + '/api/projectmembers/'
const USER_URL = process.env.API_BASE_URL + '/api/users/'

export default {
  name: 'ProjectMember',
  props: ['projectid'],
  data () {
    return {
      members: null,
      selectableUsers: null,
      selectedId: null
    }
  },
  mounted () {
    this.load()
  },
  methods: {
    load: function () {
      Promise.all([
        axios.get(USER_URL),
        axios.get(MEMBER_URL + '?project_id=' + this.projectid)
      ]).then(responses => {
        const users = responses[0].data
        const members = responses[1].data
        this.members = members
          .map(member => {
            return {
              id: member.id,
              user: users.find(user => user.id === member.user_id)
            }
          })
          .filter(member => member.user)
        this.$store.commit('setMembers', this.members)

        const unselectableUsers = this.members.map(member => member.user)
        this.selectableUsers = users.filter(user => !unselectableUsers.includes(user))
      })
    },
    addMember: function () {
      axios
        .post(MEMBER_URL, {
          project_id: this.projectid,
          user_id: this.selectedId
        })
        .then(response => {
          this.selectedId = null
          this.load()
        })
    },
    removeMember: function (member) {
      this.$confirm(member.user.username + ' をメンバーから削除しますか?', '削除確認', {
        confirmButtonText: '削除',
        cancelButtonText: 'キャンセル',
        type: 'Confirm'
      }).then(() => {
        axios
          .delete(MEMBER_URL + member.id + '/')
          .then(response => {
            this.load()
          })
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.project-member {
  float: right;
}
.el-dropdown {
  margin-right: 10px;
}
.el-select {
  width: 180px;
}
.el-dropdown-menu .el-icon-close {
  float: right;
  margin-left: 20px;
  line-height: 36px;
}
</style>

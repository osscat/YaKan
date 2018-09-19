/**
 *  担当者を選択するコンポーネント。
 */
<template>
  <div>
    <el-select v-model="id" filterable clearable remote reserve-keyword placeholder="Select User"
      :remote-method="remoteMethod"
      :loading="loading"
      @change="updateuser"
      v-on:change="$emit('onSelect', id)">
      <el-option
        v-for="member in this.$store.getters.getMembers"
        :key="member.id"
        :label="member.user.username"
        :value="member.id">
      </el-option>
    </el-select>
  </div>
</template>

<script>
export default {
  name: 'SelectUser',
  props: ['selected'],
  data () {
    return {
      id: null,
      loading: false
    }
  },
  mounted () {
    this.loadProjectMembers()
  },
  methods: {
    loadProjectMembers: function () {
      if (this.selected) {
        this.id = this.selected
      }
    },
    updateuser: function () {
      const isFunc = typeof (this.$parent.$parent.changeUser)
      if (isFunc === 'function') {
        this.$parent.$parent.changeUser(this.id)
      }
    },
    remoteMethod: function (query) {
      if (query !== '') {
        this.loading = true
        setTimeout(() => {
          this.loading = false
          this.$store.getters.getMembers.filter(user => {
            return user.label.toLowerCase().indexOf(query.toLowerCase()) > -1
          })
        }, 200)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

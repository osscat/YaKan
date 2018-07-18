/**
 *  Asideコンポーネント。
 */
<template>
  <el-aside width="200px">
    <el-menu>
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-search"></i>
          <span slot="title">検索</span>
        </template>
        <input placeholder="Project Name" class="search" v-model="word" @keyup="loadList()"/>
      </el-submenu>
      <el-menu-item index="1">
        <i class="el-icon-menu"></i>
        <router-link to="/userAdmin">ユーザー管理</router-link>
      </el-menu-item>
    </el-menu>
  </el-aside>
</template>

<script>
export default {
  name: 'Aside',
  data () {
    return {
      word: null
    }
  },
  methods: {
    loadList: function () {
      this.$parent.$parent.loadList(this.word)
    }
  }
}
</script>

<style scoped>
.search {
  margin-left: 30px;
  width: 160px;
  background-color: #fff;
  background-image: none;
  border-radius: 4px;
  border: 1px solid #dcdfe6;
  box-sizing: border-box;
  color: #606266;
  display: inline-block;
  font-size: inherit;
  line-height: 40px;
  outline: 0;
  padding: 0 15px;
  transition: border-color .2s cubic-bezier(.645,.045,.355,1);
}
.el-aside {
  text-align: left;
}
.el-menu {
  height: 100vh;
}
</style>

/**
 *  ヘッダーコンポーネント。
 */
<template>
  <div>
    <div class="line"></div>
      <el-menu :default-active="activeIndex1"
        mode="horizontal"
        @select="handleSelectIndex"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b">
      <el-menu-item index="1">プロジェクト一覧</el-menu-item>
      <el-menu-item index="2" class="loginuser">
        ログインユーザー(アイコン)
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {
      activeIndex1: '1'
    }
  },
  methods: {
    handleSelectIndex (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>
.loginuser {
  float: right
}
</style>

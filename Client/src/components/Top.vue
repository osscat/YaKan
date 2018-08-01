/**
 *  Top コンポーネント。
 */
<template>
  <el-container>
    <el-header>
      <Header/>
    </el-header>
    <el-container>
      <el-main>
        <router-view/>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import Header from './Header'

export default {
  name: 'Top',
  components: {
    Header
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

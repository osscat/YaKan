/**
 *  Top コンポーネント。
 */
<template>
  <el-container>
    <el-header class="header-sticky">
      <Header />
    </el-header>
    <div style="padding:20px;">
      <router-view/>
    </div>
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
.header-sticky {
  position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 0;
  z-index: 1;
}
</style>

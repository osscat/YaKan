/**
 *  ログインコンポーネント。
 */
<template>
  <div>
    <div class="flex-container">
      <div class="flex-container2">
        <div style="text-align:center;font-size:30px;">Welcome to Yakan!</div>
        <img src="../assets/yakan.jpg" />
        <br>
        <button @click="transition()">GO</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  methods: {
    transition: function () {
      this.$router.push({name: 'Top'})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.flex-container {
  display: flex;
  justify-content: center;
}
.flex-container2 {
  display: flex;
  flex-direction: column;
}
</style>

/**
 *  タスクを表示するコンポーネント。
 */
<template>
  <div class="flex-container">
    id:{{ task.id }}<br>
    title:{{ task.title }}<br>
    user_id:{{ task.user_id }}<br>
    man_day:{{ task.man_day }}<br>
    status:{{ task.status }}
  </div>
</template>

<script>
export default {
  name: 'Task',
  props: ['task']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.flex-container {
  margin: auto;
  width: 85%;
  height: 150px;
  padding: 10px;
  background-color: whitesmoke;
}
</style>

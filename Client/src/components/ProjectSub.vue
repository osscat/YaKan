/**
 *  各プロジェクトの内容を表示するコンポーネント。
 *  親コンポーネントからプロジェクトのデータ(JSON)を渡してください。
 */
<template>
  <div class="flex-container-sub">
    {{ project.title }}<br>
    <DeleteProjectButton :project="project" />
  </div>
</template>

<script>
import DeleteProjectButton from './DeleteProjectButton'

export default {
  name: 'ProjectSub',
  components: {
    DeleteProjectButton
  },
  props: ['project']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.flex-container-sub {
  width: 200px;
  height: 200px;
  padding: 20px;
  background-color: lightyellow;
  border: solid;
}
</style>

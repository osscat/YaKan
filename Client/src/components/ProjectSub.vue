/**
 *  各プロジェクトの内容を表示するコンポーネント。
 *  親コンポーネントからプロジェクトのデータ(JSON)を渡してください。
 */
<template>
  <el-card class="pjcard">
    {{ project.title }}<br>
    <DeleteProjectButton :project="project" />
  </el-card>
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
.pjcard {
  width: 200px;
  height: 200px;
  padding: 10px 0;
  background-color: lightyellow;
  border: solid;
}
</style>

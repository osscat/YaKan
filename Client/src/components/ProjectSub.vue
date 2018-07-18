/**
 *  各プロジェクトの内容を表示するコンポーネント。
 *  親コンポーネントからプロジェクトのデータ(JSON)を渡してください。
 */
<template>
  <el-card class="pjcard">
    <el-button type="text" @click="moveToBoard">{{ project.title }}</el-button>
    <br>
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
  props: ['project'],
  methods: {
    moveToBoard: function () {
      this.$router.push({name: 'Board', params: { boardid: this.project.id }})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.pjcard {
  width: 200px;
  height: 200px;
  padding: 10px 0;
  margin-right: 5px;
  background-color: lightyellow;
  border: solid;
}
</style>

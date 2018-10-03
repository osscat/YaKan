/**
 *  各プロジェクトの内容を表示するコンポーネント。
 *  親コンポーネントからプロジェクトのデータ(JSON)を渡してください。
 */
<template>
  <el-card class="pjdesc" shadow="never" body-style="padding: 0px">
    <div style="font-size:12px;word-break:break-all;overflow:hidden">
      <el-tooltip class="item" effect="dark" :content=project.description placement="top-start">
        <div>
          {{ project.description }}
        </div>
      </el-tooltip>
    </div>
  </el-card>
</template>

<script>
export default {
  name: 'ProjectDesc',
  props: ['project']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.pjdesc {
  width: 160px;
  height: 100px;
  background-color: lightyellow;
  border: 0px;
}

</style>

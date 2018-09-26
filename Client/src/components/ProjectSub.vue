/**
 *  各プロジェクトの内容を表示するコンポーネント。
 *  親コンポーネントからプロジェクトのデータ(JSON)を渡してください。
 */
<template>
  <el-card class="pjcard">
    <el-button type="text" v-if="project" @click="moveToBoard">{{ project.title }}</el-button>
    <ProjectDesc :project="project" />
    <div>
      <div style="float:right">
        <el-button type="warning" icon="el-icon-edit" circle @click="dialogFormVisible = true" />
        <el-dialog title="プロジェクト編集" :visible.sync="dialogFormVisible">
          <EditProjectForm :project="project" />
        </el-dialog>
        <DeleteProjectButton :project="project" />
      </div>
    </div>
  </el-card>
</template>

<script>
import EditProjectForm from './EditProjectForm'
import ProjectDesc from './ProjectDesc'
import DeleteProjectButton from './DeleteProjectButton'

export default {
  name: 'ProjectSub',
  components: {
    EditProjectForm,
    ProjectDesc,
    DeleteProjectButton
  },
  data () {
    return {
      dialogFormVisible: false
    }
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

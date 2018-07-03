/**
 *  プロジェクトの一覧を表示するコンポーネント。
 */
<template>
  <div>
    <AddProjectForm />
    <transition-group name="demo" tag="div" class="flex-project">
      <div v-for="project in projects" :key="project.id">
        <ProjectSub :project="project" />
      </div>
    </transition-group>
  </div>
</template>

<script>
import ProjectSub from './ProjectSub'
import AddProjectForm from './AddProjectForm'

export default {
  name: 'Project',
  props: ['projects'],
  components: {
    ProjectSub,
    AddProjectForm
  }
}
</script>

<style scoped>
.flex-project {
  width: 100%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
.flex-project2 {
  width: 100%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
.demo-enter-active, .demo-leave-active {
  transition: transform .5s, opacity .5s;
}
.demo-move:not(.demo-leave-active) {
  transition: transform .5s;
}
/* 消える時は縮小される */
.demo-leave-to {
  opacity: 0;
  transform: scale(0.8);
}
.demo-leave-active {
  position: absolute;
}
</style>

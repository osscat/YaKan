/**
 *  レーンを表示するコンポーネント。
 */
<template>
  <div class="flex-container">
    <div>
      <h3>{{lane.title}}<DeleteLaneButton :laneid="lane.id" style="float: right;"></DeleteLaneButton></h3>
      <h4>レーン合計 : {{laneTotal}} (md)</h4>
    </div>
    <p v-for="task in tasks" :key="task.id">
      <Task :task="task" />
    </p>
    <AddTaskButton :laneid="lane.id" style="float: left" ></AddTaskButton>
  </div>
</template>

<script>
import axios from 'axios'
import Task from './Task'
import DeleteLaneButton from './DeleteLaneButton'
import AddTaskButton from './AddTaskButton'

const TASK_URL = process.env.API_BASE_URL + '/api/tasks/'

export default {
  name: 'Lane',
  components: {
    Task,
    DeleteLaneButton,
    AddTaskButton
  },
  props: ['lane'],
  data () {
    return {
      tasks: null
    }
  },
  mounted () {
    this.loadTask()
  },
  computed: {
    laneTotal: function () {
      var total = 0
      if (this.tasks) {
        this.tasks.forEach(task => {
          total += task.man_day
        })
      }
      return total
    }
  },
  methods: {
    loadTask: function () {
      axios.get(TASK_URL + '?lane_id=' + this.lane.id).then(response => (this.tasks = response.data))
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.flex-container {
  width: 20%;
  padding: 10px;
  background-color: lightblue;
}
</style>

/**
 *  レーンを表示するコンポーネント。
 */
<template>
  <div class="lane">
    <div>
      <span class="lane-title">{{lane.title}}</span><br>
      <DeleteLaneButton :laneid="lane.id" style="float: right;"></DeleteLaneButton>
      <span class="lane-total">{{laneTotal}} (md)</span>
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
.lane {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  display: -webkit-box;
  display: -moz-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: box;
  display: flex;
  -webkit-box-orient: vertical;
  -moz-box-orient: vertical;
  -o-box-orient: vertical;
  -webkit-flex-direction: column;
  -ms-flex-direction: column;
  flex-direction: column;
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  -o-box-flex: 1;
  -webkit-flex: 0 0 270px;
  -ms-flex: 0 0 270px;
  flex: 0 0 270px;
  position: relative;
  background: #dedede;
  height: 100%;
  border-left: 1px solid #ccc;
  padding: 10px;
  float: left;
  background-color: lightblue;
  width: 220px;
}
.lane p {
  margin-top: 5px;
  margin-bottom: 5px;
}
.lane-title {
  font-size: 1.2em;
}
.lane-total {
  font-size: 1em;
}
</style>

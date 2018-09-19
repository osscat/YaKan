/**
 *  タスクを表示するコンポーネント。
 */
<template>
  <div>
    <el-card class="task" :class="{ finished: task.status === 9 }" :body-style="bodyStyle">
      <div slot="header" class="task-header">
        <span class="task-title">{{task.title}}</span><br>
        <el-button class="togglebutton" type="text" @click="toggle">
          <i class="el-icon-arrow-down" v-bind:style="{'background-color': label.color}"></i>
        </el-button>
        <span>{{task.man_day}} (md)</span>
      </div>
      <div id="detail">
        <span>タイトル</span>
        <el-input type="textarea" v-model="task.title" @change="updateTask"></el-input>
        <span>工数(ManDay)</span>
        <el-input-number v-model="task.man_day" style="width: 100%" controls-position="right" :min="0" :max="99" @change="updateTask"/>
        <span>担当者</span>
        <SelectUser :selected="task.user_id" :projectid="projectid"></SelectUser>
        <span>ラベル</span>
        <SelectLabel :selected="task.label_id"></SelectLabel>
        <el-checkbox v-model="status" @change="changeStatus">完了</el-checkbox>
        <DeleteTaskButton :task="task" style="float: right;"></DeleteTaskButton>
      </div>
     </el-card>
  </div>
</template>

<script>
import axios from 'axios'
import SelectLabel from './SelectLabel'
import SelectUser from './SelectUser'
import DeleteTaskButton from './DeleteTaskButton'

const TASK_URL = process.env.API_BASE_URL + '/api/tasks/'
const LABEL_URL = process.env.API_BASE_URL + '/api/labels/'

export default {
  name: 'Task',
  components: {
    SelectLabel,
    SelectUser,
    DeleteTaskButton
  },
  props: ['projectid', 'task'],
  data () {
    return {
      bodyStyle: {
        display: null
      },
      label: {
        id: null,
        name: null,
        color: null
      },
      status: false
    }
  },
  mounted () {
    this.bodyStyle.display = 'none'
    this.loadLabel()
    this.showStatus()
  },
  methods: {
    toggle: function () {
      if (this.bodyStyle.display === 'none') {
        this.bodyStyle.display = 'block'
      } else {
        this.bodyStyle.display = 'none'
      }
    },
    showStatus: function () {
      this.status = (this.task.status === 9)
    },
    loadLabel: function () {
      if (this.task.label_id && this.task.label_id > 0) {
        axios
          .get(LABEL_URL + this.task.label_id + '/')
          .then(
            response => {
              this.label = response.data
              this.label.color = '#' + response.data.color
            }
          )
      } else {
        this.label.color = '#FFFFFF'
      }
    },
    changeLabel: function (labelid) {
      if (!labelid) {
        this.task.label_id = 0
      } else {
        this.task.label_id = labelid
      }
      this.updateTask()
      this.loadLabel()
    },
    changeUser: function (userid) {
      if (!userid) {
        this.task.user_id = 0
      } else {
        this.task.user_id = userid
      }
      this.updateTask()
    },
    changeStatus: function () {
      if (this.status) {
        this.task.status = 9
      } else {
        this.task.status = 0
      }
      this.updateTask()
    },
    updateTask: function () {
      axios
        .put(TASK_URL + this.task.id + '/', this.task)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.togglebutton {
  float: right;
  padding: 3px 0;
}
.task-header {
  width: 150px;
}
.task-title {
  font-size: 1em;
}
.finished {
  background-color: whitesmoke;
}
</style>

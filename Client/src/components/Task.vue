/**
 *  タスクを表示するコンポーネント。
 */
<template>
  <div>
    <el-card class="task" :body-style="bodyStyle">
      <div slot="header" class="header">
        <span>{{task.title}}</span>
        <el-button class="togglebutton" type="text" @click="toggle">
          <i class="el-icon-arrow-down"></i>
        </el-button>
      </div>
      <div id="detail">
        id:{{ task.id }}<br>
        title:{{ task.title }}<br>
        user_id:{{ task.user_id }}<br>
        man_day:{{ task.man_day }}<br>
        status:{{ task.status }}
      </div>
     </el-card>
  </div>
</template>

<script>
export default {
  name: 'Task',
  props: ['task'],
  data () {
    return {
      bodyStyle: {
        display: null
      }
    }
  },
  mounted () {
    this.bodyStyle.display = 'none'
  },
  methods: {
    toggle: function () {
      if (this.bodyStyle.display === 'none') {
        this.bodyStyle.display = 'block'
      } else {
        this.bodyStyle.display = 'none'
      }
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
</style>

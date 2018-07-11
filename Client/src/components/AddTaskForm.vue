/**
 *  タスクを追加するダイアログフォームのコンポーネント。
 */
<template>
    <div>
        <el-form>
            <el-form-item label="タイトル" :label-width="formLabelWidth">
                <el-input id="title" class="newtitle" placeholder="Please input Task-Title" v-model="newtitle"></el-input>
            </el-form-item>
            <el-form-item label="工数" :label-width="formLabelWidth">
                <el-input-number style="width: 130px;" v-model="newmanday" :min="0" :max="99"></el-input-number>
            </el-form-item>
            <el-form-item label="並び順" :label-width="formLabelWidth">
                <el-input-number style="width: 130px;" v-model="neworder"></el-input-number>
            </el-form-item>
            <el-form-item label="ラベル" :label-width="formLabelWidth">
                <el-input-number style="width: 130px;" v-model="newlabel"></el-input-number>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="closeDialog()">キャンセル</el-button>
            <el-button type="primary" @click="addTask()">作成</el-button>
        </span>
    </div>
</template>

<script>
import axios from 'axios'

const TASK_POST_URL = 'http://localhost:8000/api/tasks/'

export default {
  name: 'AddLaneForm',
  props: ['laneid', 'formLabelWidth'],
  data () {
    return {
      newtitle: null,
      newmanday: null,
      neworder: 0,
      newlabel: null
    }
  },
  mounted () {
    console.log('laneid2:' + this.laneid)
  },
  methods: {
    addTask: function () {
      axios
        .post(TASK_POST_URL, {
          title: this.newtitle,
          order: this.neworder,
          user_id: 0,
          man_day: this.newmanday,
          status: 0,
          lane_id: this.laneid,
          label_id: 0
        })
        .then(response => {
          console.log(response.status)
          this.$parent.$parent.$parent.loadTask()
          this.closeDialog()
        })
    },
    closeDialog: function () {
      this.$parent.$parent.dialogFormVisible = false
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.newtitle {
  width: 300px;
}
</style>

/**
 *  タスクを追加するダイアログフォームのコンポーネント。
 */
<template>
    <div>
        <el-form>
            <el-form-item label="タイトル" :label-width="formLabelWidth">
                <el-input type="textarea" id="title" class="newtitle" :rows="1" v-model="newtitle"></el-input>
            </el-form-item>
            <el-form-item label="工数" :label-width="formLabelWidth">
                <el-input-number style="width: 130px;" v-model="newmanday" :min="0" :max="99"></el-input-number>
            </el-form-item>
            <el-form-item label="並び順" :label-width="formLabelWidth">
                <el-input-number style="width: 130px;" v-model="neworder"></el-input-number>
            </el-form-item>
            <el-form-item label="ラベル" :label-width="formLabelWidth">
              <SelectLabel :selected="0" v-on:onSelect="labelselect"></SelectLabel>
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
import SelectLabel from './SelectLabel'
import { EV_TASK } from '../plugins/WebSocket'

const TASK_POST_URL = process.env.API_BASE_URL + '/api/tasks/'

export default {
  name: 'AddLaneForm',
  components: {
    SelectLabel
  },
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
          user_id: null,
          man_day: this.newmanday,
          status: 0,
          lane_id: this.laneid,
          label_id: this.newlabel
        })
        .then(response => {
          console.log(response.status)
          this.newtitle = null
          this.newmanday = null
          this.neworder = 0
          this.newlabel = null
          this.$webSocket.send(EV_TASK, this.laneid)
          this.closeDialog()
        })
    },
    closeDialog: function () {
      this.$parent.$parent.dialogFormVisible = false
    },
    labelselect: function (select) {
      this.newlabel = select
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

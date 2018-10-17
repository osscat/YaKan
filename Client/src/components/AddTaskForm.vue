/**
 *  タスクを追加するダイアログフォームのコンポーネント。
 */
<template>
  <div>
    <el-alert v-for="(error, index) in errors" :key="index" :title="error" type="error"></el-alert>
    <el-form :model="form" ref="form" :label-width="formLabelWidth" :rules="rules">
      <el-form-item label="タイトル" prop="title">
        <el-input v-model="form.title" type="textarea" :rows="2"></el-input>
      </el-form-item>
      <el-form-item label="工数" prop="manday">
        <el-input-number v-model="form.manday" :min="0" :max="99"></el-input-number>
      </el-form-item>
      <el-form-item label="担当者" prop="user">
        <SelectUser :selected="0" v-on:onSelect="userselect"></SelectUser>
      </el-form-item>
      <el-form-item label="ラベル" prop="label">
        <SelectLabel :selected="0" v-on:onSelect="labelselect"></SelectLabel>
      </el-form-item>
    </el-form>
    <span slot="footer" class="dialog-footer">
      <el-button @click="closeDialog">キャンセル</el-button>
      <el-button type="primary" @click="addTask">作成</el-button>
    </span>
  </div>
</template>

<script>
import axios from 'axios'
import SelectUser from './SelectUser'
import SelectLabel from './SelectLabel'
import { EV_TASK } from '../plugins/WebSocket'

const TASK_POST_URL = process.env.API_BASE_URL + '/api/tasks/'

export default {
  name: 'AddTaskForm',
  components: {
    SelectUser,
    SelectLabel
  },
  props: ['laneid', 'formLabelWidth'],
  data () {
    return {
      errors: [],
      form: {
        title: null,
        manday: null,
        order: 0,
        user: null,
        label: null
      },
      rules: {
        title: [
          { required: true, message: '入力してください', trigger: 'blur' }
        ],
        manday: [
          { required: true, message: '入力してください', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    addTask: function () {
      this.$refs.form.validate(
        valid => {
          if (valid) {
            this.doSave()
          }
        }
      )
    },
    doSave: function () {
      axios
        .post(TASK_POST_URL, {
          title: this.form.title,
          order: 0,
          man_day: this.form.manday,
          status: 0,
          lane_id: this.laneid,
          user_id: this.form.user,
          label_id: this.form.label
        })
        .then(response => {
          this.form.title = null
          this.form.manday = null
          this.form.order = 0
          this.form.user = null
          this.form.label = null
          this.$webSocket.send(EV_TASK, this.laneid)
          this.closeDialog()
        })
    },
    closeDialog: function () {
      this.$emit('close')
      this.$refs.form.resetFields()
      this.errors = []
    },
    labelselect: function (select) {
      if (select) {
        this.form.label = select
      } else {
        this.form.label = 0
      }
    },
    userselect: function (select) {
      if (select) {
        this.form.user = select
      } else {
        this.form.user = 0
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-table .el-button {
  float: right;
}
</style>

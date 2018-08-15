/**
 *  レーンを追加するフォームのコンポーネント。
 */
<template>
  <form>
    <el-input id="title" class="newtitle" placeholder="Please input Lane-Title" v-model="newtitle"></el-input>
    <el-button type="primary" @click="addLane">作成</el-button>
  </form>
</template>

<script>
import axios from 'axios'
import { EV_LANE } from '../plugins/WebSocket'

const LANE_POST_URL = process.env.API_BASE_URL + '/api/lanes/'

export default {
  name: 'AddLaneForm',
  props: ['projectid'],
  data () {
    return {
      newtitle: null
    }
  },
  mounted () {
    console.log(this.projectid)
  },
  methods: {
    addLane: function () {
      axios
        .post(LANE_POST_URL, {
          project_id: this.projectid,
          title: this.newtitle,
          status: 0,
          order: 1
        })
        .then(response => {
          this.$webSocket.send(EV_LANE, this.projectid)
          this.newtitle = ''
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.newtitle {
  width: 200px;
}
</style>

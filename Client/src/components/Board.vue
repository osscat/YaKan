/**
 *  プロジェクトを表示するコンポーネント。
 */
<template>
  <div v-if="board">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Project' }">プロジェクト一覧</el-breadcrumb-item>
      <el-breadcrumb-item>{{board ? board.title : ''}}</el-breadcrumb-item>
    </el-breadcrumb>
    <ProjectMember :projectid="boardid"></ProjectMember>
    <p>総工数 {{ allMd }} (md)</p>
    <div v-if="board" class="board">
      <div>
        <AddLaneForm :projectid="boardid"></AddLaneForm>
      </div>
      <draggable v-model="lanes" @change="onChange" :options="dragoptions" style="display: flex;">
        <p v-for="lane in lanes" :key="lane.id" style="margin-top: 0px;">
          <Lane :projectid="boardid" :lane="lane" v-on:calctotal="calc" />
        </p>
      </draggable>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import draggable from 'vuedraggable'
import Lane from './Lane'
import AddLaneForm from './AddLaneForm'
import ProjectMember from './ProjectMember'
import { EV_LANE } from '../plugins/WebSocket'

const LANE_URL = process.env.API_BASE_URL + '/api/lanes/'
const BOARD_URL = process.env.API_BASE_URL + '/api/projects/'
const LABEL_URL = process.env.API_BASE_URL + '/api/labels/'

export default {
  name: 'Board',
  components: {
    draggable,
    Lane,
    AddLaneForm,
    ProjectMember
  },
  props: ['boardid'],
  data () {
    return {
      board: null,
      lanes: null,
      lanetotal: {},
      dragoptions: {
        animation: 200,
        group: 'lanegroup'
      }
    }
  },
  mounted () {
    this.getBoard()
    this.loadLane()
    this.loadLabels()
    this.$webSocket.$on(EV_LANE, this.reloadLane)
  },
  computed: {
    allMd () {
      var all = 0
      if (this.lanetotal) {
        for (var t in this.lanetotal) {
          all += this.lanetotal[t]
        }
      }
      return all
    }
  },
  methods: {
    calc: function (l) {
      this.$set(this.lanetotal, l[0], l[1])
    },
    loadLane: function () {
      var url = LANE_URL + '?project_id=' + this.boardid
      axios
        .get(url)
        .then(
          response => (this.lanes = response.data)
        )
    },
    reloadLane: function (id) {
      if (id === this.boardid) {
        this.loadLane()
      }
    },
    getBoard: function () {
      axios
        .get(BOARD_URL + this.boardid + '/')
        .then(response => (this.board = response.data))
    },
    onChange: function (event) {
      if (event.moved) {
        // 並び順を更新する
        this.laneReOrder()
      }
    },
    laneReOrder: function () {
      var index = 0
      this.lanes.forEach(lane => {
        this.updateOrder(lane, index++)
      })
    },
    updateOrder: function (lane, index) {
      lane.order = index
      axios
        .put(LANE_URL + lane.id + '/', lane)
    },
    loadLabels: function () {
      axios
        .get(LABEL_URL)
        .then(
          response => {
            this.$store.commit('setLabels', response.data)
          }
        )
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-breadcrumb {
  margin-bottom: 20px;
}
.flex-container {
  float: left;
  width: 95%;
  margin: 5px;
  padding: 10px;
}
.board {
  -webkit-box-align: start;
  -moz-box-align: start;
  -o-box-align: start;
  -ms-flex-align: start;
  -webkit-align-items: flex-start;
  align-items: flex-start;
  display: -webkit-box;
  display: -moz-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: box;
  display: flex;
  -webkit-box-orient: horizontal;
  -moz-box-orient: horizontal;
  -o-box-orient: horizontal;
  -webkit-flex-direction: row;
  -ms-flex-direction: row;
  flex-direction: row;
  overflow-x: auto;
  overflow-y: auto;
  position: absolute;
  left: 20;
  right: 20;
  top: 20;
  bottom: 20;
}
.board p {
  padding-left: 5px;
}
</style>

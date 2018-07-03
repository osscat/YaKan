/**
 *  プロジェクトを表示するコンポーネント。
 */
<template>
  <div v-if="board" class="flex-container">
    <div>
      <h3>{{board.title}} / 全合計 : {{total}} (md)</h3>
    </div>
    <p v-for="lane in lanes" :key="lane.id">
      <Lane :lane="lane" />
    </p>
    <div>
      <AddLaneForm :projectid="board.id"></AddLaneForm>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Lane from './Lane'
import AddLaneForm from './AddLaneForm'

const LANE_URL = 'http://127.0.0.1:8000/api/lanes/'

export default {
  name: 'Board',
  components: {
    Lane,
    AddLaneForm
  },
  data () {
    return {
      total: 0,
      board: null,
      lanes: null
    }
  },
  mounted () {
    this.getBoard()
    this.loadLane()
  },
  methods: {
    loadLane: function () {
      axios.get(LANE_URL).then(response => (this.lanes = response.data))
    },
    // 後で消す
    getBoard: function (id) {
      axios
        .get('http://127.0.0.1:8000/api/projects/1/')
        .then(response => (this.board = response.data))
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.flex-container {
  float: left;
  width: 95%;
  margin: 5px;
  padding: 10px;
}
</style>

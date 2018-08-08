/**
 *  ラベルを選択するコンポーネント。
 */
<template>
  <div>
    <el-select v-model="value" clearable placeholder="Select Label" @change="updatelabel">
      <el-option
        v-for="label in labels"
        v-bind:style="{'background-color': '#' + label.color}"
        :key="label.id"
        :label="label.name"
        :value="label.id">
      </el-option>
    </el-select>
  </div>
</template>

<script>
import axios from 'axios'

const LABEL_URL = process.env.API_BASE_URL + '/api/labels/'

export default {
  name: 'SelectLabel',
  props: ['selected'],
  data () {
    return {
      value: null,
      labels: []
    }
  },
  mounted () {
    this.loadLabel() // TODO:1回だけでいい。
  },
  methods: {
    loadLabel: function () {
      axios
        .get(LABEL_URL)
        .then(
          response => {
            this.labels = response.data
            if (this.selected) {
              this.value = this.selected
            }
          }
        )
    },
    updatelabel: function () {
      this.$parent.$parent.changeLabel(this.value)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

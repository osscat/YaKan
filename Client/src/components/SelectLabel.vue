/**
 *  ラベルを選択するコンポーネント。
 */
<template>
  <div>
    <el-select v-model="value" clearable placeholder="Select Label"
      @change="updatelabel"
      v-on:change="$emit('onSelect', value)">
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
    this.loadLabel()
  },
  methods: {
    loadLabel: function () {
      this.labels = this.$store.getters.getLabels
      if (this.selected) {
        this.value = this.selected
      }
    },
    updatelabel: function () {
      const isFunc = typeof (this.$parent.$parent.changeLabel)
      if (isFunc === 'function') {
        this.$parent.$parent.changeLabel(this.value)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

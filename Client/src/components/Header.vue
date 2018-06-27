/**
 *  ヘッダーコンポーネント。
 */
<template>
  <div style="width:100%;height:100px;background-color:#FFFFAA">
    ヘッダー部分<br>
    検索：<input v-model="word" @keyup="loadList()" />
  </div>
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {
      word: null
    }
  },
  methods: {
    loadList: function () {
      this.$parent.loadList(this.word)
    }
  }
}
</script>

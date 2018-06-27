/**
 *  Top コンポーネント。
 */
<template>
  <div class="flex-container">
    <Header @childs-event="loadList" />
    <Project :projects="projects" />
  </div>
</template>

<script>
import axios from 'axios'
import Header from './Header'
import Project from './Project'

const LIST_URL = 'http://127.0.0.1:8000/api/projects/?format=json'

export default {
  name: 'Login',
  data () {
    return {
      projects: null
    }
  },
  components: {
    Header,
    Project
  },
  mounted () {
    this.loadList()
  },
  methods: {
    loadList: function (word) {
      axios
        .get(LIST_URL)
        .then(
          response => {
            this.projects = response.data
            this.search(word)
          }
        )
    },
    search: function (word) {
      if (!word) {
        return
      }
      var data = this.projects.filter(
        function (item, index) {
          if (item.title.indexOf(word) !== -1) {
            return true
          }
        }
      )
      console.log(data)
      this.projects = data
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.flex-container {
  display: flex;
  flex-wrap: wrap;
}
</style>

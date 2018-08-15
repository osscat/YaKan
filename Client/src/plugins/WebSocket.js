export const EV_PROJECT_LIST = 'projects'
export const EV_PROJECT = 'project'

const URL = 'ws://' + process.env.SERVER_ADDRESS + '/ws/chat/echo/'

const webSocket = {
  install: function (Vue, options) {
    Vue.prototype.$webSocket = new Vue({
      data: {
        socket: new WebSocket(URL)
      },
      created: function () {
        this.socket.onmessage = this.onMessage
      },
      methods: {
        send: function (event, id) {
          const data = { 'target': event }
          if (id) {
            data.id = id
          }
          this.socket.send(JSON.stringify(data))
        },
        onMessage: function (e) {
          const data = JSON.parse(e.data)
          this.$emit(data.target, data.id)
        }
      }
    })
  }
}
export default webSocket

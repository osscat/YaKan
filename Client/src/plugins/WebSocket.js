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
        send: function (transaction) {
          this.socket.send(JSON.stringify({
            'transaction': transaction
          }))
        },
        onMessage: function () {
          this.$emit('message')
        }
      }
    })
  }
}
export default webSocket

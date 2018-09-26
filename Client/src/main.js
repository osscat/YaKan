// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/ja'
import router from './router'
import store from './store'
import WebSocket from './plugins/WebSocket'

Vue.use(ElementUI, { locale })
Vue.use(WebSocket)

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  if (to.name === 'Login') {
    next()
  } else if (store.getters.getUser) {
    next()
  } else {
    next({name: 'Login'})
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})

import Vue from 'vue'
import Router from 'vue-router'
import Top from '@/components/Top'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Top',
      component: Top
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})

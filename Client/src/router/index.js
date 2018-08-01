import Vue from 'vue'
import Router from 'vue-router'
import Top from '@/components/Top'
import Project from '@/components/Project'
import UserAdmin from '@/components/UserAdmin'
import Login from '@/components/Login'
import Board from '@/components/Board'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Top,
      children: [
        {
          path: '',
          name: 'Project',
          component: Project
        },
        {
          path: 'Board',
          name: 'Board',
          component: Board,
          props: true
        },
        {
          path: 'userAdmin',
          name: 'UserAdmin',
          component: UserAdmin
        }
      ]
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})

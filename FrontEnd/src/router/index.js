import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/views/Login'
import MainView from '@/views/MainView'
import Profile from '@/views/Profile'
import Activity from '@/views/Activity'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/main',
      name: 'main',
      component: MainView
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    },
    {
      path: '/activity',
      name: 'activity',
      component: Activity
    }
  ]
})

import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Pipeline from '@/components/Pipeline'
import Build from '@/components/Build'
import getAxios from '@/utils/axios.js'

Vue.prototype.$http = getAxios()
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/pipeline',
      name: 'pipeline',
      component: Pipeline
    },
    {
      path: '/build/:pipeline_id',
      name: 'build',
      component: Build
    }
  ]
})



import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import vuetify from './plugins/vuetify';

import { ipcRenderer } from "electron";

Vue.use(VueRouter)
Vue.config.productionTip = false

import FormComponent from './components/FormComponent.vue'
import WelcomeComponent from './components/WelcomeComponent.vue'
import AboutComponent from './components/AboutComponent.vue'
import TutorialComponent from './components/TutorialComponent.vue'
import RetrievalComponent from './components/RetrievalComponent.vue'

const router = new VueRouter({
  routes: [
    {
      path: '*',
      component: WelcomeComponent
    },
    {
      path: '/analysis',
      component: FormComponent
    },
    {
      path: '/about',
      component: AboutComponent
    },
    {
      path: '/tutoral',
      component: TutorialComponent
    },
    {
      path: '/retrieve',
      component: RetrievalComponent
    }
  ]
})

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')

ipcRenderer.on('about', ()  => {
  router.push('/about')
})

ipcRenderer.on('tutorial', ()  => {
  router.push('/tutorial')
})

ipcRenderer.on('analysis', ()  => {
  router.push('/analysis')
})

ipcRenderer.on('main', () => {
  router.push('/')
})

ipcRenderer.on('retrieve', () => {
  router.push('/retrieve')
})
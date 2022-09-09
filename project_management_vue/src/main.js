import Vue from 'vue'
import App from './App.vue'
import router from './router'
import {store} from './store'
import vuetify from "@/plugins/vuetify";
import axios from 'axios'

Vue.config.productionTip = false

axios.defaults.baseURL = 'http://127.0.0.1:8000'


new Vue({
  router,
  store,
  axios,
  vuetify,
  render: h => h(App)
}).$mount('#app')

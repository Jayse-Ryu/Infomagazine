// Official plugins
import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import './plugins/axios'
import './plugins/vue-cookie'
import AWS from 'aws-sdk'

// Custom plugins
import Header from './Header'
import VeeValidate from 'vee-validate'
import Paginate from 'vuejs-paginate'
import VTooltip from 'v-tooltip'
import VueDraggableResizable from 'vue-draggable-resizable'

// Set custom components
Vue.component('app-header', Header)
Vue.component('paginate', Paginate)
Vue.component('vue-draggable-resizable', VueDraggableResizable)

// Vue use
Vue.use(VeeValidate)
Vue.use(VTooltip)
Vue.use(VueDraggableResizable)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  AWS,
  render: h => h(App),
}).$mount('#app')

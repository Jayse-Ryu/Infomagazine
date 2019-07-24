// Essential
import Vue from 'vue'
import App from './App.vue'
// Official vue plugins
import store from './store'
import router from './router'
// Official plugins
import AWS from 'aws-sdk'
import VeeValidate from 'vee-validate'
import Paginate from 'vuejs-paginate'
import VTooltip from 'v-tooltip'
import VueDraggableResizable from 'vue-draggable-resizable'
// Plugins
import './plugins/axios'
import './plugins/vue-cookie'
import './plugins/date-picker'
import './plugins/vue-json-excel'

// Custom plugins
import Header from './Header'

// Set custom components
Vue.component('app-header', Header)
Vue.component('paginate', Paginate)
Vue.component('vue-draggable-resizable', VueDraggableResizable)

// Vue use
Vue.use(VeeValidate)
Vue.use(VTooltip)
Vue.use(VueDraggableResizable)
Vue.use(AWS)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  AWS,
  render: h => h(App),
}).$mount('#app')

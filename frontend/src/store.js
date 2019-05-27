import Vue from 'vue'
import Vuex from 'vuex'
import router from './router'
// import Decoder from 'jwt-decode'
import VueCookie from 'vue-cookie'

Vue.use(Vuex)
Vue.use(VueCookie)

export default new Vuex.Store({
  state: {
    // authUser: localStorage.getItem('authUser'),
    authUser: Vue.cookie.get('authUser'),
    isAuthenticated: false,
    // jwt: localStorage.getItem('token'),
    jwt: Vue.cookie.get('token'),
    endpoints: {
      obtainJWT: 'http://localhost/api/auth/',
      refreshJWT: 'http://localhost/api/auth-refresh/',
      baseUrl: 'http://localhost/api/'
    },
    pageOptions: {
      loading: false,
      landing: {
        page: 1,
        option: 0,
        text: ''
      },
      organization: {
        page: 1,
        option: 0,
        text: ''
      },
      company: {
        page: 1,
        option: 0,
        text: ''
      },
      user: {
        page: 1,
        option: 0,
        text: ''
      }
    }
  },
  mutations: {
    setAuthUser(state, {authUser}) {
      Vue.set(state, 'authUser', JSON.stringify(authUser))
      // localStorage.setItem('authUser', JSON.stringify(authUser))
    },
    setToken(state, newToken) {
      // localStorage.setItem('token', newToken)
      state.jwt = newToken
    },
    removeToken(state) {
      // localStorage.removeItem('token')
      state.jwt = null
      state.authUser = {}
      state.isAuthenticated = false
      Vue.cookie.delete('token')
      Vue.cookie.delete('authUser')
    }
  },
  actions: {
    obtainToken(self, data) {
      console.log('obtainToken action')
      this.commit('setToken', data.token)
      this.commit('setAuthUser', {
        authUser: data.user,
        isAuthenticated: true
      })
    },
    // refreshToken () {
    //   const payload = {
    //     token: this.state.jwt
    //   }
    //   axios.post(this.state.endpoints.refreshJWT, payload)
    //       .then((response) => {
    //         this.commit('setToken', response.data.token)
    //         // Get auth user
    //         if (this.state.jwt != null) {
    //           // If jwt object is really exist in local store
    //           const token = this.state.jwt
    //           const decoded = Decoder(token)
    //           const user_id = decoded.user_id
    //           axios.get(this.state.endpoints.baseUrl + 'user/' + user_id + '/')
    //               .then((response) => {
    //                 if (response.data) {
    //                   let user_obj = response.data
    //                   this.commit('setAuthUser', {
    //                     authUser: user_obj,
    //                     isAuthenticated: true
    //                   })
    //                 }
    //               })
    //               .catch((error) => {
    //                 console.log('get Auth user failed..', error)
    //               })
    //         }
    //       })
    //       .catch((error) => {
    //         console.log('Refresh error..', error)
    //       })
    // },
    inspectToken() {
      console.log('inspectToken action')
      const token = Vue.cookie.get('token')
      const authUser = Vue.cookie.get('authUser')

      if (token && authUser) {
        let store_user = JSON.parse(this.state.authUser)
        let store_token = this.state.jwt
        if (Object.keys(store_user).length === 0 && store_user.constructor === Object && !store_token) {
          console.log('inspectToken : filling vuex as cookie')
          this.commit('setToken', token)
          this.commit('setAuthUser', {
            authUser: authUser,
            isAuthenticated: true
          })
          console.log('commit done.')
        } else {
          console.log('inspectToken : vuex already filled')
        }
      } else {
        console.log('cookie not exist')
        // If no token then send to login page
        this.commit('removeToken')
        alert('로그인 후 이용 가능합니다.')
        router.currentRoute.meta.forced = 'yes'
        router.push('/')
      }
    }
  }
})

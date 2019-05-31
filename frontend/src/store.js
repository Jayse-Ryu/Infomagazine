import Vue from 'vue'
import Vuex from 'vuex'
import router from './router'
import Decoder from 'jwt-decode'
import VueCookie from 'vue-cookie'

Vue.use(Vuex)
Vue.use(VueCookie)

export default new Vuex.Store({
  state: {
    // authUser: localStorage.getItem('authUser'),
    // authUser: Vue.cookie.get('authUser'),
    authUser: {},
    isAuthenticated: false,
    // jwt: localStorage.getItem('token'),
    // jwt: Vue.cookie.get('token'),
    jwt: '',
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
      localStorage.setItem('authUser', JSON.stringify(authUser))
    },
    setToken(state, newToken) {
      // localStorage.setItem('token', newToken)
      // state.jwt = newToken
      try {
        Vue.cookie.set('token', newToken, {expires: '5m'})
      } catch (error) {
        console.log('set cookie error', error)
      }
    },
    removeToken(state) {
      localStorage.removeItem('authUser')
      // state.authUser = {}
      // state.jwt = null
      state.isAuthenticated = false
      Vue.cookie.delete('token')
      // Vue.cookie.delete('authUser')
    }
  },
  actions: {
    obtainToken(self, data) {
      // console.log('obtainToken action')
      const decoded = Decoder(data.token)
      const user = {
        id: decoded.user_id,
        email: decoded.email,
        username: decoded.username,
        is_superuser: decoded.is_superuser,
        is_staff: decoded.is_staff,
        access_role: decoded.access_role
      }

      this.commit('setToken', data.token)
      this.commit('setAuthUser', {
        authUser: user,
        isAuthenticated: true
      })

      axios.defaults.headers.common['Authorization'] = `JWT ${this.state.jwt}`
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
      // console.log('inspectToken action')
      const token = Vue.cookie.get('token')
      let authUser = localStorage.getItem('authUser')

      if (token !== null && authUser !== null) {
        // let store_user = this.state.authUser
        // let store_token = this.state.jwt
        // if (Object.keys(store_user).length === 0 && store_user.constructor === Object && !store_token) {
        //   this.commit('setToken', token)
        //   this.commit('setAuthUser', {
        //     authUser: JSON.parse(authUser),
        //     isAuthenticated: true
        //   })
        //   axios.defaults.headers.common['Authorization'] = `JWT ${this.state.jwt}`
        //   // console.log('axios default header?', axios.defaults.headers)
        // }

        return true
      } else if (token !== null && !authUser) {
        const decoded = Decoder(token)
        const user = {
          id: decoded.user_id,
          email: decoded.email,
          username: decoded.username,
          is_superuser: decoded.is_superuser,
          is_staff: decoded.is_staff,
          access_role: decoded.access_role
        }

        this.commit('setAuthUser', {
          authUser: user,
          isAuthenticated: true
        })

        return true
      } else {
        // If no token then send to login page
        this.commit('removeToken')

        return false
      }
    }
  }
})

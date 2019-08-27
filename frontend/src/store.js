import Vue from 'vue'
import Vuex from 'vuex'
// import router from './router'
import Decoder from 'jwt-decode'
import VueCookie from 'vue-cookie'

Vue.use(Vuex)
Vue.use(VueCookie)

export default new Vuex.Store({
  state: {
    // authUser: localStorage.getItem('authUser'),
    // authUser: Vue.cookie.get('authUser'),
    // authUser: {},
    isAuthenticated: false,
    endpoints: {
      obtainJWT: process.env.VUE_APP_ENV_obtainJWT,
      refreshJWT: process.env.VUE_APP_ENV_refreshJWT,
      baseUrl: process.env.VUE_APP_ENV_baseUrl
    },
    user_campaign: {
      organization: -1,
      company: -1
    },
    user_create: {
      id: 0
    },
    pageOptions: {
      header: false,
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
      // Vue.set(state, 'authUser', JSON.stringify(authUser))
      localStorage.setItem('authUser', JSON.stringify(authUser))
    },
    setToken(state, newToken) {
      // localStorage.setItem('token', newToken)
      // state.jwt = newToken
      try {
        Vue.cookie.set('token', newToken, {expires: '300m'})
      } catch (error) {
        console.log('Set token cookie error', error)
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
      const decoded = Decoder(data.token)

      const user = {
        id: decoded.user_id,
        email: decoded.email,
        username: decoded.username,
        is_superuser: decoded.is_superuser,
        is_staff: decoded.is_staff,
        access_role: decoded.access_role,
      }

      this.commit('setToken', data.token)
      this.commit('setAuthUser', {
        authUser: user,
        isAuthenticated: true
      })

      // axios.defaults.headers.common['Authorization'] = `JWT ${this.state.jwt}`
      axios.defaults.headers.common['Authorization'] = `Bearer ${data.token}`

      return true
    },
    refreshToken(token) {
      // console.log('refreshToken action')
      // const payload = {
      //   token: token
      // }
      //
      // // Refresh endpoint
      // axios.post(this.state.endpoints.refreshJWT, payload)
      //   .then((response) => {
      //     console.log('refresh response', response)
      //     this.dispatch('obtainToken', response.data.token)
      //
      //     return true
      //   })
      //   .catch((error) => {
      //     console.log('Refresh token error.', error)
      //
      //     return false
      //   })
    },
    inspectToken() {

      const token = Vue.cookie.get('token')

      if (token !== null) {
        // Token is existed
        let decoded = Decoder(token)
        let exp = decoded.exp
        let three_min = 3 * 60

        if ((Date.now() / 1000) > exp) {
          // If token is expired
          // console.log('If token is expired')
          this.commit('removeToken')

          return false
        } /*else if((Date.now() / 1000) < exp && (Date.now() / 1000) > exp - three_min) {
          console.log('If token is refresh period')
          // this.dispatch('refreshToken', token)
          axios.post(this.state.endpoints.refreshJWT, token)
            .then((response) => {
              console.log('refresh is done?', response)
            })
            .catch((error) => {
              console.log('refresh is error?', error)
            })
        }*/ else {
          // Token is not expired
          // console.log('If token is nice')
          // Forced push user data by token
          const user = {
            id: decoded.user_id,
            email: decoded.email,
            username: decoded.username,
            is_superuser: decoded.is_superuser,
            is_staff: decoded.is_staff,
            access_role: decoded.access_role,
          }

          this.commit('setAuthUser', {
            authUser: user,
            isAuthenticated: true
          })

          // axios.defaults.headers.common['Authorization'] = `JWT ${this.state.jwt}`
          axios.defaults.headers.common['Authorization'] = `Bearer ${token}`

          return true
        }

      } else {
        // Token is null
        this.commit('removeToken')

        return false
      }
    }
  }
})

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
    // authUser: {},
    isAuthenticated: false,
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
      // Vue.set(state, 'authUser', JSON.stringify(authUser))
      localStorage.setItem('authUser', JSON.stringify(authUser))
    },
    setToken(state, newToken) {
      // localStorage.setItem('token', newToken)
      // state.jwt = newToken
      try {
        Vue.cookie.set('token', newToken, {expires: '10m'})
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

      // axios.defaults.headers.common['Authorization'] = `JWT ${this.state.jwt}`
      axios.defaults.headers.common['Authorization'] = `Bearer ${data.token}`
    },
    refreshToken() {
      let token = Vue.cookie.get('token')
      const payload = {
        token: token
      }
      // Refresh endpoint
      axios.post(this.state.endpoints.refreshJWT, payload)
        .then((response) => {
          this.dispatch('obtainToken', response.data.token)

          return true
        })
        .catch((error) => {
          console.log('Refresh token error.', error)

          return false
        })
    },
    inspectToken() {
      // console.log('inspectToken action')
      const token = Vue.cookie.get('token')
      const authUser = localStorage.getItem('authUser')

      if (token !== null && authUser !== null) {
        // Both exist
        this.dispatch('inspectProgress', token)
          .then(() => {
            return true
          })
          .catch((error) => {
            console.log('Inspect - both exist error', error)
            return false
          })
      } else if (token !== null && !authUser) {
        // Only token exist
        this.dispatch('inspectProgress', token)
          .then(() => {
            return true
          })
          .catch((error) => {
            console.log('Inspect - only token exist error', error)
            return false
          })
      } else {
        // Both are null
        this.commit('removeToken')

        return false
      }
    },
    inspectProgress(token) {
      const decoded = Decoder(token)
      const exp = decoded.exp
      const orig_iat = decoded.orig_iat
      const a_day = 86400 // 24*60*60
      const thirty_minutes = 1800 // 30*60

      if ((Date.now() / 1000) > exp) {
        // If token expired then send to login page
        this.commit('removeToken')
        // alert('로그인 시간이 만료되었습니다.')
        router.currentRoute.meta.forced = 'yes'
        router.push('/')
        return false
      } else if ((Date.now() / 1000) > exp - thirty_minutes && (Date.now() / 1000) < orig_iat + a_day) {
        // If token expire in less than 30 minutes but still in refresh period then refresh
        this.dispatch('refreshToken')
          .then(() => {
            return true
          })
          .catch((error) => {
            console.log('Inspect token refresh await error.', error)
            return false
          })
      }
      // /if date
    }
  }
})

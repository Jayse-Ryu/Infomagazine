import Vue from 'vue'
import Vuex from 'vuex'
import router from "./router"
import Decoder from 'jwt-decode'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authUser: {},
    userAccess: {},
    isAuthenticated: false,
    jwt: localStorage.getItem('token'),
    endpoints: {
      obtainJWT: 'http://localhost/api/api-token-auth/',
      refreshJWT: 'http://localhost/api/api-token-refresh/',
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
    setAuthUser (state, {
      authUser,
      isAuthenticated
    }) {
      Vue.set(state, 'authUser', authUser)
      Vue.set(state, 'isAuthenticated', isAuthenticated)
    },
    setAccess (state, {
      userAccess
    }) {
      Vue.set(state, 'userAccess', userAccess)
    },
    updateToken (state, newToken) {
      localStorage.setItem('token', newToken)
      state.jwt = newToken
    },
    removeToken (state) {
      localStorage.removeItem('token')
      state.jwt = null
      state.authUser = {}
      state.userAccess = {}
      state.isAuthenticated = false
    }
  },
  actions: {
    obtainToken (self, pay) {
      const payload = {
        account: pay.account,
        password: pay.password
      }
      axios.post(this.state.endpoints.obtainJWT, payload)
          .then((response) => {
            this.commit('updateToken', response.data.token)
            return this.dispatch('inspectToken')
          })
          .then(() => {
            router.push('/gateway')
          })
          .catch(() => {
            // Check the account or password
            alert('아이디와 비밀번호를 확인해주세요.')
          })
    },
    refreshToken () {
      const payload = {
        token: this.state.jwt
      }
      axios.post(this.state.endpoints.refreshJWT, payload)
          .then((response) => {
            this.commit('updateToken', response.data.token)
            // Get auth user
            if (this.state.jwt != null) {
              // If jwt object is really exist in local store
              const token = this.state.jwt
              const decoded = Decoder(token)
              const user_id = decoded.user_id
              axios.get(this.state.endpoints.baseUrl + 'user/' + user_id + '/')
                  .then((response) => {
                    if (response.data) {
                      let user_obj = response.data
                      this.commit('setAuthUser', {
                        authUser: user_obj,
                        isAuthenticated: true
                      })
                    }
                    return axios.get(this.state.endpoints.baseUrl + 'user_access/' + user_id + '/')
                  })
                  .then((response) => {
                    this.commit('setAccess', {
                      userAccess: response.data
                    })
                  })
                  .catch((error) => {
                    console.log('get Auth user failed..', error)
                  })
            }
          })
          .catch((error) => {
            console.log('Refresh error..', error)
          })
    },
    inspectToken () {
      const token = this.state.jwt
      if (token) {
        const decoded = Decoder(token)
        const exp = decoded.exp
        const orig_iat = decoded.orig_iat
        const a_day = 86400 // 7*24*60*60
        const thirty_minutes = 1800 // 30*60
        if ((Date.now() / 1000) > exp) {
          // If token expired then send to login page
          this.commit('removeToken')
          alert('로그인 시간이 만료되었습니다.')
          router.currentRoute.meta.forced = 'yes'
          router.push('/')
          return 'remove token'
        } else if ((Date.now() / 1000) > exp - thirty_minutes && (Date.now() / 1000) < orig_iat + a_day) {
          // If token expire in less than 30 minutes but still in refresh period then refresh
          this.dispatch('refreshToken')
              .then(() => {
                console.log('refresh done.')
              })
        } else {
          // Get auth user
          if (this.state.jwt != null) {
            // If jwt object is really exist in local store
            const token = this.state.jwt
            const decoded = Decoder(token)
            const user_id = decoded.user_id
            axios.get(this.state.endpoints.baseUrl + 'user/' + user_id + '/')
                .then((response) => {
                  if (response.data) {
                    let user_obj = response.data
                    this.commit('setAuthUser', {
                      authUser: user_obj,
                      isAuthenticated: true
                    })
                  }
                  return axios.get(this.state.endpoints.baseUrl + 'user_access/' + user_id + '/')
                })
                .then((response) => {
                  this.commit('setAccess', {
                    userAccess: response.data
                  })
                })
                .catch((error) => {
                  console.log('get Auth user failed..', error)
                })
          }
        }
      } else {
        // If no token then send to login page
        this.commit('removeToken')
        alert('로그인 후 이용 가능합니다.')
        router.currentRoute.meta.forced = 'yes'
        router.push('/')
        return 'remove token'
      }
    }
  }
})

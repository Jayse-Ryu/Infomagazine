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
    removeToken(state) {
      localStorage.removeItem('authUser')
      state.isAuthenticated = false
      Vue.cookie.delete('SESSION')
      Vue.cookie.delete('csrftoken')
    }
  },
  actions: {
    obtainToken(self, data) {

      let token = Vue.cookie.get('SESSION')
      let decoded = Decoder(token)

      let information = {
        id: decoded.id,
        email: decoded.email,
        username: decoded.username,
        is_superuser: decoded.is_superuser,
        is_staff: decoded.is_staff,
        access_role: decoded.access_role,
      }

      this.commit('setAuthUser', {
        authUser: information,
        isAuthenticated: true
      })

      this.dispatch('get_additional_info', information.id)

      // axios.defaults.headers.common['Authorization'] = `JWT ${this.state.jwt}`
      // axios.defaults.headers.common['Authorization'] = `Bearer ${data.token}`

      return true
    },
    inspectToken() {
      // Inspect and Refresh both.
      let token = Vue.cookie.get('SESSION')

      if (token !== null) {
        // Token is existed
        let decoded = Decoder(token)
        let exp = decoded.exp
        let three_hours = 3 * 60 * 60
        // let five_and_fifty_nine = 5 * 60 * 60 + 59 * 60 + 30

        if ((Date.now() / 1000) > exp) {
          // If token is expired
          this.commit('removeToken')

          return false
        } else if ((Date.now() / 1000) < exp && (Date.now() / 1000) > exp - three_hours) {
          // If token in refresh period.
          return axios.post(this.state.endpoints.refreshJWT, token)
            .then(() => {

              let token_ref = Vue.cookie.get('SESSION')
              let decoded_ref = Decoder(token_ref)

              let information = {
                id: decoded_ref.id,
                email: decoded_ref.email,
                username: decoded_ref.username,
                is_superuser: decoded_ref.is_superuser,
                is_staff: decoded_ref.is_staff,
                access_role: decoded_ref.access_role,
              }

              this.commit('setAuthUser', {
                authUser: information,
                isAuthenticated: true
              })

              this.dispatch('get_additional_info', information.id)

              return true
            })
            .catch((error) => {
              console.log('refresh is error?', error)
              this.commit('removeToken')

              return false
            })

        } else {
          // Token is alive
          // Forced push user data by token
          let information = {
            id: decoded.id,
            email: decoded.email,
            username: decoded.username,
            is_superuser: decoded.is_superuser,
            is_staff: decoded.is_staff,
            access_role: decoded.access_role,
          }

          this.commit('setAuthUser', {
            authUser: information,
            isAuthenticated: true
          })

          this.dispatch('get_additional_info', information.id)

          // axios.defaults.headers.common['Authorization'] = `JWT ${this.state.jwt}`
          // axios.defaults.headers.common['Authorization'] = `Bearer ${token}`

          return true
        }

      } else {
        // Token is null or empty
        this.commit('removeToken')

        return false
      }
    },
    get_additional_info(self, user_id) {
      // Add user campaign information
      if (user_id !== null) {
        axios.get(this.state.endpoints.baseUrl + 'users/' + user_id + '/')
          .then((response) => {
            if (response.data.data.info.organization !== null) {
              this.state.user_campaign.organization = response.data.data.info.organization
            } else if (response.data.data.info.company) {
              this.state.user_campaign.company = response.data.data.info.company
            }
          })
          .catch((error) => {
            console.log('Get additional info error', error)
          })
      }
    }
  }
})

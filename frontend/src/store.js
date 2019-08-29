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
    // setToken(state, newToken) {
    //   // localStorage.setItem('token', newToken)
    //   // state.jwt = newToken
    //   try {
    //     Vue.cookie.set('token', newToken, {expires: '300m'})
    //   } catch (error) {
    //     console.log('Set token cookie error', error)
    //   }
    // },
    removeToken(state) {
      localStorage.removeItem('authUser')
      // state.authUser = {}
      // state.jwt = null
      state.isAuthenticated = false
      // Vue.cookie.delete('JWT')
      // Vue.cookie.delete('csrftoken')
      // Vue.cookie.delete('token')
      // Vue.cookie.delete('authUser')
      Vue.cookie.delete('SESSION')
    }
  },
  actions: {
    obtainToken(self, data) {

      const decoded = Decoder(data.token)

      // this.commit('removeToken')

      // const information = {
      //   id: data.id,
      //   email: data.email,
      //   username: data.username,
      //   is_superuser: data.is_superuser,
      //   is_staff: data.is_staff,
      //   access_role: data.access_role,
      //   expire: data.expired_data
      // }

      const information = {
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

      // this.get_additional_info(data.id)
      this.dispatch('get_additional_info', information.id)

      // axios.defaults.headers.common['Authorization'] = `JWT ${this.state.jwt}`
      // axios.defaults.headers.common['Authorization'] = `Bearer ${data.token}`

      return true
    },
    refreshToken(self, token) {
      console.log('refreshToken')

      // // Refresh endpoint
      axios.post(this.state.endpoints.refreshJWT)
        .then((response) => {
          console.log('refresh response', response)
          // this.dispatch('obtainToken', response.data.token)

          return true
        })
        .catch((error) => {
          console.log('Refresh token error.', error)

          return false
        })
    },
    inspectToken() {
      const token = Vue.cookie.get('SESSION')

      // let decoded = Decoder(token)
      // let exp = decoded.exp
      // console.log('jwt exp is?', exp)
      // console.log(token)

      const user_storage = localStorage.getItem('authUser')

      // if (user_storage !== null) {
      //
      //   // console.log('construc', user_storage.constructor)
      //   // console.log('length', Object.keys(user_storage).length)
      //
      //   if (Object.keys(user_storage).length !== 0 && user_storage.constructor === Object) {
      //     // console.log('starage is not null? ')
      //     let user = JSON.parse(user_storage)
      //     this.commit('setAuthUser', {
      //       authUser: user,
      //       isAuthenticated: true
      //     })
      //
      //     if (this.state.user_campaign.organization === -1 && this.state.user_campaign.company === -1) {
      //       this.dispatch('get_additional_info', user.id)
      //     }
      //     return true
      //   } else {
      //     // console.log('starage is null? ')
      //     this.commit('removeToken')
      //     return false
      //   }
      // } else {
      //   // console.log('starage is null? ')
      //   this.commit('removeToken')
      //   return false
      // }


      // // Object.keys(obj).length === 0 && obj.constructor === Object
      // if (Object.keys(user_storage).length !== 0 && user_storage.constructor === Object) {
      //   console.log('starage is not null? ')
      //   let user = JSON.parse(user_storage)
      //   this.commit('setAuthUser', {
      //     authUser: user,
      //     isAuthenticated: true
      //   })
      //
      //   if (this.state.user_campaign.organization === -1 && this.state.user_campaign.company === -1) {
      //     this.dispatch('get_additional_info', user.id)
      //   }
      //   return true
      // } else {
      //   console.log('starage is null? ')
      //   this.commit('removeToken')
      //   return false
      // }


      if (token !== null) {
        // Token is existed
        let decoded = Decoder(token)
        let exp = decoded.exp
        let two_hours = 2 * 60 * 60
        let five_and_fifty_nine = 5 * 60 * 60 + 59 * 60 + 30

        if ((Date.now() / 1000) > exp) {
          // If token is expired
          // console.log('If token is expired')
          this.commit('removeToken')

          return false
        } else if ((Date.now() / 1000) < exp && (Date.now() / 1000) > exp - five_and_fifty_nine) {
          // console.log('If token is refresh period')
          // this.dispatch('refreshToken', token)
          // axios.post(this.state.endpoints.refreshJWT, token)
          //   .then((response) => {
          //     console.log('refresh is done?', response)
          //     return true
          //   })
          //   .catch((error) => {
          //     console.log('refresh is error?', error)
          //     return false
          //   })

          const information = {
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

          this.dispatch('refreshToken', token)
            .then((response) => {
              if (response === true) {
                return true
              } else {
                return false
              }
            })
            .catch((error) => {
              console.log('refresh call fail', error)
              return false
            })

        } else {
          // Token is not expired
          // console.log('If token is nice')
          // Forced push user data by token
          const information = {
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
        // Token is null
        this.commit('removeToken')

        return false
      }
    },
    get_additional_info(self, user_id) {
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

import Vue from 'vue'
import Router from 'vue-router'
import Store from './store'
import './plugins/vue-cookie'

Vue.use(Router)

const router = new Router({
// export default new Router({
  routes: [
    {
      path: 'error',
      name: 'A404',
      component: () => import('./views/A404.vue'),
      meta: {
        signed: false
      }
    },
    {
      path: '/',
      name: 'sign_in',
      component: () => import('./views/Signin.vue'),
      meta: {
        signed: false
      }
    },
    {
      path: '/signup',
      name: 'sign_up',
      component: () => import('./views/Signup.vue'),
      meta: {
        signed: false,
        protect_leave: 'yes'
      }
    },
    {
      path: '/gateway',
      name: 'gateway',
      component: () => import('./views/Gateway.vue'),
      meta: {
        signed: true,
        auth_grade: 'guest'
      }
    },
    {
      path: '/landing',
      name: 'landing_list',
      component: () => import('./views/LandingList.vue'),
      meta: {
        signed: true,
        auth_grade: 'client'
      }
    },
    {
      path: '/landing/create',
      name: 'landing_create',
      component: () => import('./views/LandingCreate.vue'),
      meta: {
        signed: true,
        auth_grade: 'marketer',
        protect_leave: 'yes'
      }
    },
    {
      path: '/landing/detail/:landing_id',
      name: 'landing_detail',
      component: () => import('./views/LandingDetail.vue'),
      meta: {
        signed: true,
        auth_grade: 'client',
        protect_leave: 'yes'
      }
    },
    {
      path: '/landing/preview/:landing_id',
      name: 'preview',
      component: () => import('./components/preview/preview.vue'),
      meta: {
        signed: true,
        auth_grade: 'marketer',
      }
    },
    {
      path: '/organization',
      name: 'organization_list',
      component: () => import('./views/OrganizationList.vue'),
      meta: {
        signed: true,
        auth_grade: 'marketer'
      }
    },
    {
      path: '/organization/detail/:organization_id',
      name: 'organization_detail',
      component: () => import('./views/OrganizationDetail.vue'),
      meta: {
        signed: true,
        auth_grade: 'marketer',
        protect_leave: 'yes'
      }
    },
    {
      path: '/organization/create',
      name: 'organization_create',
      component: () => import('./views/OrganizationCreate.vue'),
      meta: {
        signed: true,
        auth_grade: 'staff',
        protect_leave: 'yes'
      }
    },
    {
      path: '/company',
      name: 'company_list',
      component: () => import('./views/CompanyList.vue'),
      meta: {
        signed: true,
        auth_grade: 'marketer'
      }
    },
    {
      path: '/company/create',
      name: 'company_create',
      component: () => import('./views/CompanyCreate.vue'),
      meta: {
        signed: true,
        auth_grade: 'marketer',
        protect_leave: 'yes'
      }
    },
    {
      path: '/company/detail/:company_id',
      name: 'company_detail',
      component: () => import('./views/CompanyDetail.vue'),
      meta: {
        signed: true,
        auth_grade: 'marketer',
        protect_leave: 'yes'
      }
    },
    {
      path: '/db/detail/:landing_id',
      name: 'db_detail',
      component: () => import('./views/DBDetail.vue'),
      meta: {
        signed: true,
        auth_grade: 'client'
      }
    },
    {
      path: '/users',
      name: 'user_list',
      component: () => import('./views/UserList.vue'),
      meta: {
        signed: true,
        auth_grade: 'staff'
      }
    },
    {
      path: '/users/detail/:user_id',
      name: 'user_detail',
      component: () => import('./views/UserDetail.vue'),
      meta: {
        signed: true,
        auth_grade: 'staff'
      }
    },
    {
      path: '/users/create',
      name: 'user_create',
      component: () => import('./views/UserCreate.vue'),
      meta: {
        signed: true,
        auth_grade: 'marketer',
        protect_leave: 'yes'
      }
    },
    {
      path: '/myinfo',
      name: 'my_info',
      component: () => import('./views/MyInfo.vue'),
      meta: {
        signed: true,
        auth_grade: 'guest',
        protect_leave: 'yes'
      }
    },
    {
      path: '/page/:base',
      name: 'page',
      component: () => import('./views/Page.vue'),
      alias: '/page/:base/:url',
      meta: {
        signed: false
      }
    }
  ],
  base: process.env.BASE_URL,
  mode: 'history',
  // eslint-disable-next-line
  scrollBehavior() {
    return {
      x: 0,
      y: 0
    }
  }
})

router.beforeEach((to, from, next) => {
  // console.log('router from', from)
  // console.log('router to', to)

  // When user access_code not matched with router
  let access_denied = () => {
    // console.log('Access denied')
    if (from.meta.protect_leave === 'yes') {
      alert('권한이 없는 페이지입니다.')
      from.meta.protect_leave = 'no'
      next({name: 'gateway'})
      router.push({name: 'sign_in'})
    } else {
      alert('권한이 없는 페이지입니다.')
      next({name: 'gateway'})
      router.push({name: 'sign_in'})
    }
  }

  // Check authentication by token, authUser
  let work = () => {
    // console.log('work')
    let authUser = JSON.parse(localStorage.getItem('authUser'))
    // let authUser = JSON.parse(localStorage.getItem('authUser'))
    // let token = Vue.cookie.get('token')
    // console.log('router auth user is ', authUser)

    let admin = authUser.is_superuser
    let staff = authUser.is_staff
    let marketer = [0, 1]
    let client = [0, 1, 2]
    let guest = [0, 1, 2, 3]

    if (to.meta.auth_grade === 'guest') {
      if (staff || admin || guest.includes(authUser.access_role)) {
        next()
      } else {
        access_denied()
      }
    } else if (to.meta.auth_grade === 'client') {
      if (staff || admin || client.includes(authUser.access_role)) {
        next()
      } else {
        access_denied()
      }
    } else if (to.meta.auth_grade === 'marketer') {
      if (staff || admin || marketer.includes(authUser.access_role)) {
        next()
      } else {
        access_denied()
      }
    } else if (to.meta.auth_grade === 'staff') {
      if (staff || admin) {
        next()
      } else {
        access_denied()
      }
    }
    // The last next work for router default (NECESSARY)
    next()
  }

  // Check access needs or router exist
  let intro = () => {
    // console.log('intro')
    if (!to.meta.signed) {
      // When router try to access very basic pages
      // But, Excluding logged user access to sign-in page
      if (to.name === 'sign_in') {
        // Inspect return is set True or false
        Store.dispatch('inspectToken')
          .then((response) => {
            // console.log('inspect 1 res ', response)
            if (response === true) {
              next({name: 'landing_list'})
            } else {
              next()
            }
          })
          .catch((error) => {
            console.log('Router-intro inspect 1 crashed.', error)
          })
      } else {
        // If not 'to' sign_in, signed meta is null
        if (!to.name || to.name === null || to.name === '') {
          next({name: 'A404'})
        } else {
          next()
        }
      }
    } else if (!to.name || to.name === null || to.name === '') {
      // If meta signed?
      // If component is not exist, push to 404 page
      next({name: 'A404'})
    } else {
      // Remained router is Cookie check
      Store.dispatch('inspectToken')
        .then((response) => {
          // console.log('inspect 2 res ', response)
          if (response === true) {
            work()
          } else {
            // Cookie is not available
            if (from.meta.protect_leave === 'yes') {
              from.meta.protect_leave = 'no'
              alert('로그인이 필요합니다.')
              next({name: 'sign_in'})
            } else {
              alert('로그인이 필요합니다.')
              next({name: 'sign_in'})
            }
          }
        })
        .catch((error) => {
          console.log('Router-intro inspect 2 crashed!', error)
        })
    }
  }

  // Check first before meta
  let before_check = () => {
    // console.log('before_check')
    if (from.meta.protect_leave) {
      // Prevent router error with meta is undefined
      if (from.meta.protect_leave === 'yes') {
        // Are you sure to leave this page?
        if (confirm('정말 떠나시겠습니까?')) {
          intro()
        }
      } else if (from.meta.protect_leave === 'no') {
        // If request is forced
        // Set meta as default again
        from.meta.protect_leave = 'yes'
        intro()
      }
    } else {
      // If leave meta is none
      intro()
    }
  }

  // Router Before each starts with 'before check'
  before_check()
})

export default router

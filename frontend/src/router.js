import Vue from 'vue'
import Router from 'vue-router'
import Store from './store'

Vue.use(Router)

const router = new Router({
// export default new Router({
  routes: [
    {
      path: 'error',
      name: 'A404',
      component: () => import(/* webpackChunkName: "A404" */ './views/A404.vue')
    },
    {
      path: '/',
      name: 'sign_in',
      component: () => import('./views/Signin.vue')
    },
    {
      path: '/signup',
      name: 'sign_up',
      component: () => import('./views/Signup.vue'),
      meta: {
        protect_leave: 'yes'
      }
    },
    {
      path: '/gateway',
      name: 'gateway',
      component: () => import('./views/Gateway.vue'),
      meta: {
        signed: true
      }
    },
    {
      path: '/landing',
      name: 'landing_list',
      component: () => import('./views/LandingList.vue'),
      meta: {
        signed: true,
        auth_grade: 'customer'
      }
    },
    {
      path: '/landing/create',
      name: 'landing_create',
      component: () => import('./views/LandingCreate.vue'),
      meta: {
        signed: true,
        auth_grade: 'manager',
        protect_leave: 'yes'
      }
    },
    {
      path: '/landing/detail/:landing_id',
      name: 'landing_detail',
      component: () => import('./views/LandingDetail.vue'),
      meta: {
        signed: true,
        auth_grade: 'customer',
        protect_leave: 'yes'
      }
    },
    {
      path: '/organization',
      name: 'organization_list',
      component: () => import('./views/OrganizationList.vue'),
      meta: {
        signed: true,
        auth_grade: 'manager'
      }
    },
    {
      path: '/organization/detail/:organization_id',
      name: 'organization_detail',
      component: () => import('./views/OrganizationDetail.vue'),
      meta: {
        signed: true,
        auth_grade: 'manager',
        protect_leave: 'yes'
      }
    },
    {
      path: '/company',
      name: 'company_list',
      component: () => import('./views/CompanyList.vue'),
      meta: {
        signed: true,
        auth_grade: 'customer'
      }
    },
    {
      path: '/company/create',
      name: 'company_create',
      component: () => import('./views/CompanyCreate.vue'),
      meta: {
        signed: true,
        auth_grade: 'manager',
        protect_leave: 'yes'
      }
    },
    {
      path: '/company/detail/:company_id',
      name: 'company_detail',
      component: () => import('./views/CompanyDetail.vue'),
      meta: {
        signed: true,
        auth_grade: 'customer',
        protect_leave: 'yes'
      }
    },
    {
      path: '/db/detail/:landing_id',
      name: 'db_detail',
      component: () => import('./views/DBDetail.vue'),
      meta: {
        signed: true,
        auth_grade: 'customer'
        // protect_leave: 'no'
      }
    },
    {
      path: '/users',
      name: 'user_list',
      component: () => import('./views/UserList.vue'),
      meta: {
        signed: true,
        auth_grade: 'manager'
      }
    },
    {
      path: '/users/detail/:user_id',
      name: 'user_detail',
      component: () => import('./views/UserDetail.vue'),
      meta: {
        signed: true,
        auth_grade: 'manager'
      }
    },
    {
      path: '/myinfo',
      name: 'my_info',
      component: () => import('./views/MyInfo.vue'),
      meta: {
        signed: true,
        protect_leave: 'yes'
      }
    },
    {
      path: '/page/:base',
      name: 'page',
      component: () => import('./views/Page.vue'),
      alias: '/page/:base/:url'
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
  console.log('router before from', from)
  console.log('router before to', to)
  // Check authentication by token
  let work = () => {
    // eslint-disable-next-line
    if (!to.name || to.name == null || to.name == '') {
      // If user try to access 'none' page.
      next({name: 'A404'})
    } else {
      if (to.path === '/' || to.path === '') {
        next()
      } else {
        if (to.meta.signed) {
          if (window.localStorage.token || Store.state.authUser.id) {
            if (to.meta.auth_grade) {
              // Auth grade filter
              let auth = to.meta.auth_grade
              if (auth === 'superuser') {
                if (Store.state.authUser.is_superuser) {
                  next()
                } else {
                  next({name: 'gateway'})
                }
              } else if (auth === 'staff') {
                if (Store.state.authUser.is_staff) {
                  next()
                } else {
                  next({name: 'gateway'})
                }
              } else if (auth === 'manager') {
                if (Store.state.userAccess.access === 1) {
                  if (to.name === 'organization_detail') {
                    // eslint-disable-next-line
                    if (Store.state.userAccess.organization == to.params.organization_id || Store.state.authUser.is_staff) {
                      next()
                      // eslint-disable-next-line
                    } else if (Store.state.userAccess.organization != to.params.organization_id && !Store.state.authUser.is_staff) {
                      next({name: 'organization_list'})
                    } else {
                      next()
                    }
                  }
                } else {
                  next({name: 'gateway'})
                }
              } else if (auth === 'customer') {
                if (Store.state.userAccess.access >= 1) {
                  next()
                } else {
                  next({name: 'gateway'})
                }
              }
            }
            // /Auth grade filter
          } else {
            // Store has not token or Auth user not exist
            next({name: 'sign_in'})
          }
        } else {
          // If no sign meta, Let them go to next.
          next()
        }
      }
      // The last next work for router default (NECESSARY)
      next()
    }
  }
  // Set let user go rightly or not
  let intro = () => {
    if (to.path === '/' || to.path === '' || to.name === 'sign_up' || to.name === 'page' || to.name === 'A404') {
      next()
    } else {
      if (from.name == null && to.name !== 'gateway') {
        // When user randomly access to not public page and gateway page.
        work()
      } else {
        // If not but still don't have authentication
        if (Store.state.authUser.id == null) {
          Store.dispatch('inspectToken')
              .then(() => {
                work()
              })
        } else {
          // Or user have authentication
          work()
        }
      }
    }
  }
  // Check meta(from.leave) first
  if (from.meta.protect_leave) {
    if (from.meta.protect_leave === 'yes') {
      // Are you sure to leave this page?
      // eslint-disable-next-line
      if (from.meta.forced == 'yes') {
        from.meta.forced = 'no'
        intro()
      } else {
        if (confirm('정말 떠나시겠습니까?')) {
          intro()
        }
      }
    } else if (from.meta.protect_leave === 'no') {
      from.meta.protect_leave = 'yes'
      intro()
    }
  } else {
    intro()
  }
})

export default router

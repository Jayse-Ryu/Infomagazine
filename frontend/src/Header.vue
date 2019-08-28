<template>
  <div class="nav_king" id="nav_king">
    <div class="nav_wrap">
      <nav class="navbar navbar-light bg-light navbar-expand-md">

        <!-- Logo and nav, buttons. -->
        <router-link to="/landing" class="logo_wrap navbar-brand">
        <span class="logo">
          <img src="./assets/logo3.png" alt="Infomag logo">
        </span>
        </router-link>

        <button class="navbar-toggler" data-toggle="collapse" data-target="#navbarCollapse">
          <span class="navbar-toggler-icon"></span>
        </button>

        <!-- Staff area -->
        <div v-if="user_obj && user_obj.is_staff || user_obj.is_superuser" class="collapse navbar-collapse"
             id="navbarCollapse">
          <!-- Gateway for staff -->
          <ul class="navbar-nav ml-auto">
            <li class="navbar-item">
              <router-link to="/landing">
                <div class="nav-link text-center">랜딩페이지</div>
              </router-link>
            </li>
            <li class="navbar-item">
              <router-link to="/organization">
                <div class="nav-link text-center">관리조직</div>
              </router-link>
            </li>
            <li class="navbar-item">
              <router-link to="/company">
                <div class="nav-link text-center">고객업체</div>
              </router-link>
            </li>
            <li class="navbar-item">
              <router-link to="/users">
                <div class="nav-link text-center">회원관리</div>
              </router-link>
            </li>
            <li class="navbar-item">
              <router-link to="/myinfo">
                <div class="nav-link current_user font text-center" v-model="header_name">{{ header_name }}</div>
              </router-link>
            </li>
            <li class="navbar-item">
              <input type="button" class="btn btn-dark w-100 pb-1 pt-1 text-center" @click="logout" value="로그아웃">
            </li>
          </ul>
        </div>
        <!-- /Staff area -->

        <!-- Not staff User area -->
        <div v-else-if="user_obj && !user_obj.is_staff && !user_obj.is_superuser" class="collapse navbar-collapse"
             id="navbarCollapse">

          <!-- user is marketer. 0 owner / 1 marketer -->
          <ul v-if="[0,1].includes(user_obj.access_role)"
              class="navbar-nav ml-auto">
            <li class="navbar-item">
              <router-link to="/landing">
                <div class="nav-link text-center">랜딩페이지</div>
              </router-link>
            </li>
            <li class="navbar-item">
              <router-link :to="'/organization/detail/' + $store.state.user_campaign.organization">
                <div class="nav-link text-center">관리소속</div>
              </router-link>
            </li>
            <li class="navbar-item">
              <router-link to="/company">
                <div class="nav-link text-center">고객업체</div>
              </router-link>
            </li>
            <li class="navbar-item">
              <router-link to="/myinfo">
                <div class="nav-link current_user font text-center" v-model="header_name">{{ header_name }}</div>
              </router-link>
            </li>
            <li class="navbar-item">
              <input type="button" class="btn btn-dark w-100 pb-1 pt-1 text-center" @click="logout" value="로그아웃">
            </li>
          </ul>
          <!-- / -->

          <!-- user access is client -->
          <ul v-if="user_obj.access_role == 2" class="navbar-nav ml-auto">
            <li class="navbar-item">
              <router-link to="/landing">
                <div class="nav-link text-center">랜딩페이지</div>
              </router-link>
            </li>
            <li class="navbar-item">
              <!--<router-link to="/myinfo">-->
              <div class="nav-link current_user font text-center" v-model="header_name">{{ header_name }}</div>
              <!--</router-link>-->
            </li>
            <li class="navbar-item">
              <input type="button" class="btn btn-dark w-100 pb-1 pt-1 text-center" @click="logout" value="로그아웃">
            </li>
          </ul>
          <!-- / -->

          <!-- user access is guest -->
          <ul v-if="user_obj.access_role == 3" class="navbar-nav ml-auto">
            <li class="navbar-item">
              <router-link to="/gateway">
                <div class="nav-link text-center">홈페이지</div>
              </router-link>
            </li>
            <li class="navbar-item">
              <router-link to="/myinfo">
                <div class="nav-link current_user font text-center" v-model="header_name">{{ header_name }}</div>
              </router-link>
            </li>
            <li class="navbar-item">
              <input type="button" class="btn btn-dark w-100 pb-1 pt-1 text-center" @click="logout" value="로그아웃">
            </li>
          </ul>
          <!-- / -->

          <!-- If user access is none -->
          <ul v-else-if="user_obj.failed" class="navbar-nav ml-auto">
            <li class="navbar-item">
              <router-link to="/">
                <div class="nav-link text-center">로그인</div>
              </router-link>
            </li>
            <li class="navbar-item">
              <router-link to="/signup">
                <div class="nav-link text-center">회원가입</div>
              </router-link>
            </li>
          </ul>
          <!-- / -->
        </div>
        <!-- /User area -->

      </nav>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'app-header',
    data: () => ({
      contribute: [
        {
          sign: 'senior_back_Aug.2019',
          name: 'Soo-kyeom Kim',
          git: 'https://github.com/sookyeomKim'
        },
        {
          sign: 'junior_front_Aug.2019',
          name: 'Dong-geun Jayse Ryu',
          git: 'https://github.com/Jayse-Ryu'
        }
      ]
    }),
    mounted() {
      let block = [
        '',
        'A404',
        'page',
        'sign_in',
        'sign_up'
      ]
      let that = this
      that.$nextTick(function () {
        if (block.includes(this.$route.name)) {
          // document.getElementById('nav_king').style.display = 'none'
          document.getElementById('nav_king').setAttribute('style', 'display: none;')
          this.$store.state.pageOptions.header = false
        } else {
          // document.getElementById('nav_king').style.display = 'block'
          document.getElementById('nav_king').setAttribute('style', 'display: block;')
          this.$store.state.pageOptions.header = true
        }
      })
      let dev = this.contribute
      for (let key in dev) {
        if (document.getElementById(dev[key].sign)) {
          break
        } else {
          let val = 'dev / ' + dev[key].name + ' - ' + dev[key].git
          let dev_script = document.createElement('input')
          dev_script.setAttribute('type', 'hidden')
          dev_script.setAttribute('id', dev[key].sign)
          dev_script.setAttribute('value', val)
          document.body.appendChild(dev_script)
        }
      }
    },
    methods: {
      logout() {
        if (confirm('로그아웃 하시겠습니까?')) {
          this.$store.commit('removeToken')
          if (this.$router.currentRoute.meta.protect_leave === 'yes') {
            this.$router.currentRoute.meta.protect_leave = 'no'
          }
          this.$router.push({
            name: 'sign_in'
          })
        }
      }
    },
    computed: {
      header_name() {
        let local_user = localStorage.getItem('authUser')
        let username = ''

        if (!local_user) {
          username = 'None'
        } else {
          if (JSON.parse(local_user).username == '') {
            username = '이름없음'
          } else {
            username = JSON.parse(local_user).username
          }
        }

        return username
      },
      user_obj() {
        let local_user = localStorage.getItem('authUser')
        let user_json = {}

        if (!local_user) {
          user_json = {
            'is_staff': false,
            'is_superuser': false,
            'access_role': 3,
            'failed': true,
            'organization': -1,
            'company': -1
          }
        } else {
          user_json = JSON.parse(local_user)
        }
        return user_json
      }
    }
  }
</script>

<style scoped lang="scss">
  li .router-link-exact-active {
    color: #287BFF;

    div {
      // background-color: #00737a;
      color: #287BFF !important;
      font-weight: bold;
    }
  }

  li .router-link-active {
    color: #287BFF;

    div {
      color: #287BFF !important;
      font-weight: bold;
    }
  }

  .current_user {
    color: cadetblue !important;
  }

  @media (max-width: 350px) {
    .logo_wrap {
      max-width: 210px !important;

      .logo {
        img {
          width: 80%;
        }
      }
    }
  }
</style>

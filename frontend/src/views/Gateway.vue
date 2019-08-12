<template>
  <div class="main">

    <div class="text_navigation">
      <router-link to="/">로그인</router-link>
      <span>></span>
      <router-link to="/gateway">홈페이지</router-link>
    </div>

    <div class="container m-auto text-center">
      <div v-if="$store.state.user_campaign.organization*1 == 0" class="select_org">
        <h3 class="w-100 mb-4">환영합니다 <span class="text-info">{{ user_name }}</span> 마케터님</h3>
        <p class="mb-2">인포매거진은 마케팅 업체인 <span class="text-success">조직</span>과</p>
        <p class="mb-2">고객 업체인 <span class="text-success">업체</span>로 구분되어 있습니다.</p>
        <p class="mb-4">본인이 속한 조직을 선택하여 가입을 완료하세요!</p>

        <input v-if="organization_list.length*1 == 0" class="form-control col-md-11 m-auto" type="text" v-model="search"
               placeholder="사업자 번호">
        <button v-if="organization_list.length*1 == 0" type="button" class="w-100 btn btn-primary mt-3 col-md-11"
                @click="org_search">사업자 번호 검색
        </button>

        <select v-if="organization_list.length*1 > 1"
                class="form-control col-md-11 m-auto"
                name="org_list"
                id="org_list"
                v-model="org_selected">
          <option value="-1" selected>조직을 선택하세요</option>
          <option v-for="item in organization_list" :value="item.id">
            {{ item.org_name }} / {{ item.org_sub_name }}
          </option>
        </select>

        <button v-if="organization_list.length*1 > 1" type="button" class="w-100 btn btn-primary mt-3 col-md-11"
                @click="org_select">선택하기
        </button>
        <button v-if="organization_list.length*1 > 1" type="button" class="w-100 btn btn-dark mt-3 col-md-11 mt-2"
                @click="org_reset">돌아가기
        </button>
      </div>

      <div v-else>
        <h4>
          <span class="text-info">{{ user_name }}</span> 마케터님은 현재
          <!--          <span class="text-primary">{{ requested.org_name }} ({{ requested.org_sub_name }})</span>-->
          승인대기 중 입니다.
        </h4>
        <p class="mt-4">관리자 승인 후 서비스 이용 가능합니다.</p>

        <!--<button type="button" class="btn btn-danger mt-4 col-sm-4" @click="org_cancel">요청 취소</button>-->

      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "gateway",
    data: () => ({
      user_name: '',
      org_selected: -1,
      organization_list: [],
      requested: {},
      search: ''
    }),
    mounted() {
      this.check_access()

      if (this.user_obj.username == '') {
        this.user_name = '이름없음'
      } else {
        this.user_name = this.user_obj.username
      }

    },
    methods: {
      info_update(id) {
        axios.get(this.$store.state.endpoints.baseUrl + 'users/' + id + '/')
          .then((response) => {
            if (response.data.data.info.organization) {
              this.$store.state.user_campaign.organization = response.data.data.info.organization
            } else if (response.data.data.info.company) {
              this.$store.state.user_campaign.company = response.data.data.info.company
            }
          })
          .catch((error) => {
            console.log('Get user info error', error)
          })
      },
      check_access() {
        if (!this.user_obj.failed) {
          if (this.user_obj.is_staff || this.user_obj.is_superuser) {
            // // Staff, Superuser push to landing list page
            this.$router.push({
              name: 'landing_list'
            })
          } else if ([0, 1, 2].includes(this.user_obj.access_role)) {
            // Marketer but already got access from staff.
            this.$router.push({
              name: 'landing_list'
            })
          }
        }
      },
      org_search() {
        let crn = this.search
        /* (crn.replace(/-/gi, '')).replace(/\ /gi, '') */
        axios.get(this.$store.state.endpoints.baseUrl + 'organizations/?org_crn=' + (crn.replace(/-/gi, '')).replace(/\ /gi, ''))
          .then((response) => {
            if (response.data.data.count == 0) {
              alert('해당하는 조직이 없습니다.')
            } else if (response.data.data.count == 1) {
              let name = response.data.data.results[0].org_name
              if (confirm(name + ' 조직에 가입하시겠습니까?')) {
                this.user_patch(response.data.data.results[0].id)
              }
            } else {
              this.organization_list = response.data.data.results
            }
          })
          .catch((error) => {
            console.log(error)
          })
      },
      org_select() {
        if (this.org_selected == -1) {
          alert('조직을 선택해주세요.')
          document.getElementById('org_list').focus()
        } else {
          this.user_patch(this.org_selected)
        }
      },
      user_patch(id) {
        // // Update actual user
        let form = {
          email: this.user_obj.email,
          info: {
            organization: id
          }
        }

        axios.patch(this.$store.state.endpoints.baseUrl + 'users/' + this.user_obj.id + '/', form)
          .then((response) => {
            console.log('updated?', response.data)
            this.info_update(this.user_obj.id)
          })
          .catch((error) => {
            console.log('An error occurred during patch user.', error)
          })
      },
      org_reset() {
        this.organization_list = []
        this.search = ''
      },
      org_cancel() {
        if (confirm('조직 가입 요청을 취소하시겠습니까?')) {
          let form = {
            info: {
              organization: -1
            }
          }
          axios.patch(this.$store.state.endpoints.baseUrl + 'users/' + this.user_obj.id + '/', form)
            .then((response) => {
              console.log('updated?', response.data)
              this.info_update(this.user_obj.id)
            })
            .catch((error) => {
              console.log('An error occurred during patch user.', error)
            })
        }
      }
    },
    computed: {
      user_obj() {
        // Get user information
        let local_user = localStorage.getItem('authUser')
        let user_json = {}

        if (!local_user) {
          user_json = {
            'is_staff': false,
            'is_superuser': false,
            'info': {
              'access_role': 3
            },
            'failed': true
          }
        } else {
          user_json = JSON.parse(local_user)
          this.info_update(user_json.id)
        }

        return user_json
      }
    }
  }
</script>

<style lang="scss" scoped>
  .select_org {
    p {
      font-size: 1.1em;
    }
  }
</style>

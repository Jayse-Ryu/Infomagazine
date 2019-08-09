<template>
  <div class="main">

    <div class="text_navigation">
      <router-link to="/">로그인</router-link>
      <span>></span>
      <router-link to="/gateway">홈페이지</router-link>
    </div>

    <div class="container m-auto text-center">
      <div v-if="user_org == null || user_org == -1" class="select_org">
        <h3 class="w-100 mb-4">환영합니다 <span class="text-info">{{ user_name }}</span> 마케터님</h3>
        <p class="mb-2">인포매거진은 마케팅 업체인 <span class="text-success">조직</span>과</p>
        <p class="mb-2">고객 업체인 <span class="text-success">업체</span>로 구분되어 있습니다.</p>
        <p class="mb-4">본인이 속한 조직을 선택하여 가입을 완료하세요!</p>
        <select class="form-control col-md-11 m-auto" name="org_list" id="org_list"
                v-model="org_selected">
          <option value="-1" selected>조직을 선택하세요</option>
          <option v-for="item in organization_list" :value="item.id">
            {{ item.org_name }} / {{ item.org_sub_name }}
          </option>
        </select>

        <button type="button" class="w-100 btn btn-primary mt-3 col-md-11" @click="org_select">선택하기</button>
      </div>

      <div v-else>
        <div v-for="org in organization_list">
          <h4 v-if="org.id == user_org">
            <span class="text-info">{{ user_name }}</span> 마케터님은 현재
            <span class="text-primary">{{ org.org_name }} ({{ org.org_sub_name }})</span>
            에 승인대기 중 입니다.</h4>
          <p class="mt-4" v-if="org.id == user_org">관리자 승인 후 서비스 이용 가능합니다.</p>
        </div>
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
      user_org: -1,
      organization_list: []
    }),
    mounted() {
      this.check_access()

      if (this.user_obj.username == '') {
        this.user_name = '이름없음'
      } else {
        this.user_name = this.user_obj.username
      }

      // Get organization!
      axios.get(this.$store.state.endpoints.baseUrl + 'organizations/')
        .then((response) => {
          this.organization_list = response.data.data.results
        })
        .catch((error) => {
          console.log('Error occurred from get organization', error)
        })
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
          } else if (this.user_obj.access_role == 0 || this.user_obj.access_role == 1) {
            // Marketer but already got access from staff.
            this.$router.push({
              name: 'landing_list'
            })
          }
        }
      },
      org_select() {
        if (this.org_selected == -1) {
          alert('조직을 선택해주세요.')
          document.getElementById('org_list').focus()
        } else {
          this.user_org = this.org_selected
          let form = {
            email: this.user_obj.email,
            info: {
              organization: this.org_selected
            }
          }

          console.log(this.user_obj)


          // // Update actual user
          // axios.patch(this.$store.state.endpoints.baseUrl + 'users/' + '?organization=' + this.org_selected)
          axios.patch(this.$store.state.endpoints.baseUrl + 'users/' + this.user_obj.id + '/', form)
            .then((response) => {
              console.log('updated?', response.data)
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

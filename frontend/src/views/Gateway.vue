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
      organization_list: [
        {
          id: 1,
          org_name: 'LCVENTURES',
          org_sub_name: '엘씨벤처스',
          org_crn: '사업자등록번호: 220-88-91971',
          org_header: 'KWM',
          org_address: '서울 성동구 뚝섬로 1길 25 한라에코밸리 206호',
          org_tel_num: '070-8855-8390',
          org_desc: '마케팅회사 엘씨벤처스 입니다.',
          org_manage_email: 'biz@lcventures.co.kr',
          org_manage_phone: '01046111111',
          created_date: '2019-01-01',
          updated_date: '2019-02-01'
        },
        {
          id: 2,
          org_name: 'Bad company',
          org_sub_name: '경쟁사',
          org_crn: '사업자번호: 22071',
          org_header: 'Nobody',
          org_address: '서울 성동구 뚝섬로 25길 1 한라지옥밸리 602호',
          org_tel_num: '070-1234-4321',
          org_desc: '경쟁사 입니다.',
          org_manage_email: 'biz@kyunjeng.co.kr',
          org_manage_phone: '01023111111',
          created_date: '2019-01-02',
          updated_date: '2019-02-02'
        }
      ]
    }),
    mounted() {
      this.check_access()

      if (this.user_obj.username == '') {
        this.user_name = '이름없음'
      } else {
        this.user_name = this.user_obj.username
      }

      // // Get organization!
      console.error('JAYSE - Get organization has to activate')
      // axios.get(this.$store.state.endpoints.baseUrl + 'organization/')
      //   .then((response) => {
      //     this.organization_list = response.data
      //   })
      //   .catch((error) => {
      //     console.log('Error occurred from get organization', error)
      //   })
    },
    methods: {
      check_access() {
        if (!this.user_obj.failed) {
        if (this.user_obj.is_staff || this.user_obj.superuser) {
          // // Staff, Superuser push to landing list page
          // this.$router.push({
          //   name: 'landing_list'
          // })
          console.error('JAYSE - this user is staff or super so push to landing list later')
        } else if (this.user_obj.info.access_role == '0' || this.user_obj.info.access_role == '1') {
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
          this.user_obj.info.organization = this.org_selected
          this.user_org = this.org_selected
          // // Update actual user
          // axios.patch(this.$store.state.endpoints.baseUrl + 'user/' + this.user_obj.id + '/')
          //   .then((response) => {
          //     console.log(response.data)
          //   })
        }
      }
    },
    computed: {
      user_obj() {
        // Get user information
        let store_user = this.$store.state.authUser
        let user_json = {}
        if (Object.keys(store_user).length === 0 && store_user.constructor) {
          // dummy auth
          user_json = {
            'is_staff': false,
            'is_superuser': false,
            'info': {
              'access_role': 3
            },
            'failed': true
          }
        } else {
          user_json = JSON.parse(this.$store.state.authUser)
          this.user_org = user_json.info.organization
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

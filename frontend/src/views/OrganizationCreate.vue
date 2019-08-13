<template>
  <div class="main">

    <div class="text_navigation">
      <router-link to="/">홈</router-link>
      <span>></span>
      <router-link to="/organization">조직 리스트</router-link>
      <span>></span>
      <router-link to="/organization/create">조직 생성</router-link>
    </div>

    <div class="container">
      <h4>마케팅 회사를 위한 <span class="text-info">조직</span>을 생성합니다</h4>

      <form class="m-auto" v-on:submit.prevent="before_create_organization">
        <div class="form-group row">

          <label for="org_name" class="col-form-label-sm col-sm-3 mt-3">
            <span>조직 이름*</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input :class="error_label.class.name" id="org_name" name="org_name" type="text"
                   v-model="create_obj.org_name"
                   required
                   v-validate="'required'"
                   placeholder="조직 이름을 입력하세요"
                   autofocus="autofocus"
                   maxlength="100"
                   @keyup="error_check('name')">
          </div>

          <label for="org_sub" class="col-form-label-sm col-sm-3 mt-3">
            <span>상호명 (마케팅명)*</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <div class="error_label" v-if="errors.has('org_sub')">{{errors.first('org_sub')}}</div>
            <input class="form-control" id="org_sub" name="org_sub" type="text"
                   required
                   v-model="create_obj.org_sub_name"
                   placeholder="상호명을 입력하세요"
                   autofocus="autofocus"
                   maxlength="100"
            >
          </div>

          <label for="org_header" class="col-form-label-sm col-sm-3 mt-3">
            <span>대표자*</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input class="form-control" id="org_header" name="org_header" type="text"
                   required
                   v-model="create_obj.org_header"
                   placeholder="조직 대표자를 입력하세요"
                   autofocus="autofocus"
                   maxlength="100"
            >
          </div>

          <label for="org_addr" class="col-form-label-sm col-sm-3 mt-3">
            <span>주소*</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input class="form-control" id="org_addr" name="org_addr" type="text"
                   required
                   v-model="create_obj.org_address"
                   placeholder="주소를 입력하세요"
                   autofocus="autofocus"
                   maxlength="200">
          </div>

          <label for="org_corp" class="col-form-label-sm col-sm-3 mt-3">
            <span>사업자 번호*</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input :class="error_label.class.corp" id="org_corp" name="org_corp" type="text"
                   v-model="create_obj.org_crn"
                   placeholder="사업자 번호를 입력하세요"
                   autofocus="autofocus"
                   maxlength="50"
                   required
                   @keyup="error_check('corp')">
          </div>

          <label for="org_phone" class="col-form-label-sm col-sm-3 mt-3">
            <span>연락처*</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input :class="error_label.class.tel_num" id="org_phone" name="org_phone"
                   type="tel"
                   v-model="create_obj.org_tel_num"
                   placeholder="연락처를 입력하세요"
                   autofocus="autofocus"
                   maxlength="16"
                   required
                   @keyup="error_check('phone')">
          </div>

          <label for="org_desc" class="col-form-label-sm col-sm-3 mt-3">
            <span>조직설명</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input class="form-control" id="org_desc" type="text"
                   v-model="create_obj.org_desc"
                   placeholder="조직 설명을 적어주세요"
                   autofocus="autofocus"
                   maxlength="200">
          </div>

          <label for="org_manager" class="col-form-label-sm col-sm-3 mt-3">
            <span>조직 관리 마케터</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <select class="form-control col-md-12 m-auto" name="org_manager" id="org_manager"
                    v-model="create_obj.org_manager">
              <option value="-1" selected>추후에 선택합니다</option>
              <option v-for="item in marketer_list" :value="item.id">
                {{ item.username }} / {{ item.email }}
              </option>
            </select>
          </div>

        </div>
        <button type="submit" class="btn btn-primary col-12 mt-2 mb-2">조직 생성</button>
        <router-link to="/company">
          <button type="button" class="btn btn-dark col-12 mb-3">취소</button>
        </router-link>
      </form>
    </div>

  </div>
</template>

<script>
  export default {
    name: "organization_create",
    data: () => ({
      // For organization create
      error_label: {
        org_name: true,
        org_tel_num: false,
        org_corp: false,
        // org_email: false,
        class: {
          name: 'form-control',
          tel_num: 'form-control',
          // email: 'form-control'
          corp: 'form-control'
        }
      },
      create_obj: {
        org_name: '',
        org_sub_name: '',
        org_header: '',
        org_address: '',
        org_crn: '',
        org_tel_num: '',
        org_email: '',
        org_desc: '',
        org_manager: -1
      },
      marketer_list: []
    }),
    mounted() {
      // Get marketer users for set as a manager
      axios.get(this.$store.state.endpoints.baseUrl + 'users/?limit=9999999999')
        .then((response) => {
          let short = response.data.data.results
          for (let i = 0; i < short.length; i++) {
            if ([1, 3].includes(short[i].info.access_role)) {
              // marketer or guest
              if (short[i].username == '') {
                short[i].username = '이름없음'
              }
              this.marketer_list.push(short[i])
            }
          }
          // this.marketer_list = response.data.data.results
          // for (let i = 0; i < this.marketer_list.length; i++) {
          //   if (this.marketer_list[i].username == '') {
          //     this.marketer_list[i].username = '이름없음'
          //   }
          // }
        })
        .catch((error) => {
          console.log('Get user is failed', error)
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
      // Real-Time custom validation
      error_check(param) {
        if (param === 'phone') {
          // Phone validate
          // console.log('param is phone')
          if (this.create_obj.org_tel_num !== '') {
            // Allow mobile phone, internet wireless
            let regular_tel = /^(?:(010\d{4})|(01[1|6|7|8|9]\d{3,4})|(070\d{4}))(\d{4})$/
            let tel_num = this.create_obj.org_tel_num
            let test_flag = regular_tel.test(tel_num)
            if (!test_flag) {
              this.error_label.org_tel_num = true
              this.error_label.class.tel_num = 'form-control alert-danger'
            } else {
              this.error_label.org_tel_num = false
              this.error_label.class.tel_num = 'form-control alert-info'
            }
          } else {
            this.error_label.org_tel_num = false
            this.error_label.class.tel_num = 'form-control'
          }
          // /Phone validate
        } else if (param === 'name') {
          axios.get(this.$store.state.endpoints.baseUrl + 'organizations/')
            .then((response) => {
              let duplicated = false
              if (response.data.results.length) {
                for (let i = 0; i < response.data.results.length; i++) {
                  if (this.create_obj.org_name == response.data.results[i].org_name) {
                    duplicated = true
                  }
                }
              }
              if (duplicated) {
                this.error_label.org_name = true
                this.error_label.class.name = 'form-control alert-danger'
              } else if (this.create_obj.org_name === '') {
                this.error_label.org_name = true
                this.error_label.class.name = 'form-control alert-danger'
              } else {
                this.error_label.org_name = false
                this.error_label.class.name = 'form-control alert-info'
              }
            })
            .catch((error) => {
              console.log(error)
            })
          // Org name validate
          if (this.create_obj.org_name === '') {
            this.error_label.org_name = true
            this.error_label.class.name = 'form-control alert-danger'
          } else {
            this.error_label.org_name = false
            this.error_label.class.name = 'form-control alert-info'
          }
        } else if (param === 'corp') {
          if (this.create_obj.org_crn === '') {
            this.error_label.org_corp = true
            this.error_label.class.corp = 'form-control alert-danger'
          } else {
            this.error_label.org_corp = false
            this.error_label.class.corp = 'form-control alert-info'
          }
        }
      },
      before_create_organization() {
        this.$validator.validateAll()
        if (this.error_label.org_tel_num) {
          alert('전화번호 형식을 확인해주세요!')
          document.getElementById('org_phone').focus()
        } else if (this.error_label.org_name) {
          alert('조직 이름을 입력하세요!')
          document.getElementById('org_name').focus()
        } else if (this.error_label.org_corp) {
          alert('사업자번호를 입력하세요!')
          document.getElementById('org_corp').focus()
        } else {
          this.create_organization()
        }
      },
      create_organization() {
        // Create an organization myself
        if (confirm('조직을 생성하시겠습니까?')) {
          this.$store.state.pageOptions.loading = true
          axios.post(this.$store.state.endpoints.baseUrl + 'organizations/', this.create_obj)
            .then((response) => {
              alert('조직이 생성되었습니다.')
              this.$store.state.pageOptions.loading = false
              if (this.create_obj.org_manager > 0) {
                return axios.patch(this.$store.state.endpoints.baseUrl + 'users/' + this.create_obj.org_manager + '/', {
                  'info': {access_role: 0, organization: response.data.data.id}
                })
              } else {
                this.$router.currentRoute.meta.protect_leave = 'no'
                this.$router.push({
                  name: 'organization_list'
                })
              }
            })
            .then(() => {
              this.$router.currentRoute.meta.protect_leave = 'no'
              this.$router.push({
                name: 'organization_list'
              })
            })
            .catch((error) => {
              alert('조직 생성 중 오류가 발생하였습니다.')
              this.$store.state.pageOptions.loading = false
              console.log(error)
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
          // dummy block access auth
          user_json = {
            'is_staff': false,
            'is_superuser': false,
            'access_role': 3,
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

<style lang="scss">

</style>

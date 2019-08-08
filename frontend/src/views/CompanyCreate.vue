<template>
  <div class="main">
    <div class="text_navigation">
      <router-link to="/">홈</router-link>
      <span>></span>
      <router-link to="/company">업체 리스트</router-link>
      <span>></span>
      <router-link to="/company/create">업체 생성</router-link>
    </div>

    <div class="container">
      <h4>고객 회사를 위한 <span class="text-info">업체</span>를 생성합니다</h4>
      <form class="m-auto" v-on:submit.prevent="before_create_company">
        <div class="form-group row">

          <label v-if="user_obj.is_staff || user_obj.is_superuser" for="set_org"
                 class="col-form-label-sm col-sm-3 mt-3">
            <span>관리 조직 <span class="alert alert-danger p-0">(Staff Only)</span></span>
          </label>
          <div v-if="user_obj.is_staff" class="col-sm-9 mt-sm-3">
            <select name="set_org" id="set_org" class="form-control" v-model="create_obj.org_id">
              <option value="0" selected>선택하세요</option>
              <option v-for="item in organization_list" :value="item.id">
                {{ item.org_name }} / {{ item.org_sub_name }}
              </option>
            </select>
          </div>

          <label for="corp_name" class="col-form-label-sm col-sm-3 mt-3">
            <span>업체 이름*</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input :class="error_label.class.name" id="corp_name" name="corp_name" type="text"
                   v-model="create_obj.corp_name"
                   required
                   v-validate="'required'"
                   placeholder="업체 이름을 입력하세요"
                   autofocus="autofocus"
                   maxlength="100"
                   @keyup="error_check('name')">
          </div>

          <label for="corp_sub" class="col-form-label-sm col-sm-3 mt-3">
            <span>상호명 (마케팅명)</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <div class="error_label" v-if="errors.has('corp_sub')">{{errors.first('corp_sub')}}</div>
            <input class="form-control" id="corp_sub" name="corp_sub" type="text"
                   v-model="create_obj.corp_sub_name"
                   placeholder="상호명을 입력하세요"
                   autofocus="autofocus"
                   maxlength="100"
            >
          </div>

          <label for="corp_header" class="col-form-label-sm col-sm-3 mt-3">
            <span>업체 대표</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input class="form-control" id="corp_header" name="corp_header" type="text"
                   v-model="create_obj.corp_header"
                   placeholder="업체 대표를 입력하세요"
                   autofocus="autofocus"
                   maxlength="30">
          </div>

          <label for="corp_addr" class="col-form-label-sm col-sm-3 mt-3">
            <span>주소</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input class="form-control" id="corp_addr" name="corp_addr" type="text"
                   v-model="create_obj.corp_address"
                   placeholder="주소를 입력하세요"
                   autofocus="autofocus"
                   maxlength="200">
          </div>

          <label for="corp_crn" class="col-form-label-sm col-sm-3 mt-3">
            <span>사업자 번호</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input class="form-control" id="corp_crn" name="corp_crn" type="text"
                   v-model="create_obj.corp_crn"
                   placeholder="사업자 번호를 입력하세요"
                   autofocus="autofocus"
                   maxlength="50">
          </div>

          <label for="corp_phone" class="col-form-label-sm col-sm-3 mt-3">
            <span>연락처</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input :class="error_label.class.tel_num" id="corp_phone" name="corp_phone"
                   type="number"
                   v-model="create_obj.corp_num"
                   placeholder="연락처를 입력하세요"
                   autofocus="autofocus"
                   maxlength="16"
                   @keyup="error_check('phone')">
          </div>

          <label for="corp_email" class="col-form-label-sm col-sm-3 mt-3">
            <span>이메일</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input :class="error_label.class.email" id="corp_email" name="corp_email" type="email"
                   v-model="create_obj.corp_email"
                   placeholder="이메일을 입력하세요"
                   maxlength="50"
                   autofocus="autofocus"
                   v-validate="'email'"
                   @keyup="error_check('email')">
          </div>

          <label for="corp_desc" class="col-form-label-sm col-sm-3 mt-3">
            <span>업체 설명</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input class="form-control" id="corp_desc" type="text"
                   v-model="create_obj.corp_desc"
                   placeholder="업체 설명을 적어주세요"
                   autofocus="autofocus"
                   maxlength="200">
          </div>

        </div>
        <button type="submit" class="btn btn-primary col-12 mt-2 mb-2">업체 생성</button>
        <router-link to="/company">
          <button type="button" class="btn btn-dark col-12 mb-3">취소</button>
        </router-link>
      </form>
    </div>


  </div>
</template>

<script>
  export default {
    name: "company_create",
    data: () => ({
      // For company create
      organization_list: [],
      error_label: {
        corp_name: true,
        corp_tel_num: false,
        corp_email: false,
        class: {
          name: 'form-control',
          tel_num: 'form-control',
          email: 'form-control'
        }
      },
      create_obj: {
        org_id: 0,
        corp_name: '',
        corp_sub_name: '',
        corp_header: '',
        corp_address: '',
        corp_crn: '',
        corp_num: '',
        corp_email: '',
        corp_desc: ''
      },
    }),
    mounted() {
      // Get organization for admin users set org themselves
      if (this.user_obj.is_staff || this.user_obj.is_superuser) {
        axios.get(this.$store.state.endpoints.baseUrl + 'organizations/')
          .then((response) => {
            this.organization_list = response.data.data.results
          })
          .catch((error) => {
            console.log('Staff get organization is failed', error)
          })
      } else if ([0, 1].includes(this.user_obj.access_role)) {
        this.create_obj.org_id = this.user_obj.organization
      }
      // /Get org
    },
    methods: {
      error_check(param) {
        if (param === 'phone') {
          // Phone validate
          console.log('param is phone')
          if (this.create_obj.corp_num !== '') {
            // Allow mobile phone, internet wireless only
            let regular_tel = /^(?:(010\d{4})|(01[1|6|7|8|9]\d{3,4})|(070\d{4}))(\d{4})$/
            let tel_num = this.create_obj.corp_num
            let test_flag = regular_tel.test(tel_num)
            if (!test_flag) {
              this.error_label.corp_tel_num = true
              this.error_label.class.tel_num = 'form-control alert-danger'
            } else {
              this.error_label.corp_tel_num = false
              this.error_label.class.tel_num = 'form-control alert-info'
            }
          } else {
            this.error_label.corp_tel_num = false
            this.error_label.class.tel_num = 'form-control'
          }
          // /Phone validate
        } else if (param === 'email') {
          // Email validate
          if (this.create_obj.corp_email !== '') {
            if (this.$validator.errors.has('corp_email')) {
              this.error_label.corp_email = true
              this.error_label.class.email = 'form-control alert-danger'
            } else {
              this.error_label.corp_email = false
              this.error_label.class.email = 'form-control alert-info'
            }
          } else {
            this.error_label.corp_email = false
            this.error_label.class.email = 'form-control'
          }
        } else if (param === 'name') {
          axios.get(this.$store.state.endpoints.baseUrl + 'companies/')
            .then((response) => {
              let duplicated = false
              for (let i = 0; i < response.data.results.length; i++) {
                if (this.create_obj.corp_name == response.data.results[i].corp_name) {
                  duplicated = true
                }
              }
              if (duplicated) {
                this.error_label.corp_name = true
                this.error_label.class.name = 'form-control alert-danger'
              } else if (this.create_obj.corp_name === '') {
                this.error_label.corp_name = true
                this.error_label.class.name = 'form-control alert-danger'
              } else {
                this.error_label.corp_name = false
                this.error_label.class.name = 'form-control alert-info'
              }
            })
            .catch((error) => {
              console.log('get company error', error)
            })
        }
      },
      before_create_company() {
        this.$validator.validateAll()
        if (this.error_label.corp_email || this.$validator.errors.has('corp_email')) {
          alert('이메일을 확인해주세요')
          document.getElementById('corp_email').focus()
        } else if (this.error_label.corp_tel_num) {
          alert('전화번호 형식을 확인해주세요!')
          document.getElementById('corp_phone').focus()
        } else if (this.error_label.name) {
          alert('업체 이름을 입력하세요!')
          document.getElementById('corp_name').focus()
        } else {
          this.create_company()
        }
      },
      create_company() {
        // Create an organization myself
        this.$validator.validateAll()
        if (confirm('업체를 생성하시겠습니까?')) {
          this.$store.state.pageOptions.loading = true
          axios.post(this.$store.state.endpoints.baseUrl + 'companies/', this.create_obj)
            .then(() => {
              alert('업체가 생성되었습니다.')
              this.$store.state.pageOptions.loading = false
              this.$router.currentRoute.meta.protect_leave = 'no'
              this.$router.push({
                name: 'company_list'
              })
            })
            .catch((error) => {
              alert('업체 생성 중 오류가 발생하였습니다.')
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
          axios.get(this.$store.state.endpoints.baseUrl + 'users/' + user_json.id + '/')
            .then((response) => {
              if (response.data.data.info.organization) {
                user_json['organization'] = response.data.data.info.organization
              } else if (response.data.data.info.company) {
                user_json['company'] = response.data.data.info.company
              }
            })
            .catch((error) => {
              console.log('Get user info error', error)
            })
        }

        return user_json
      }
    }
  }
</script>

<style lang="scss">

</style>

<template>
  <div class="main">
    <div class="text_navigation">
      <router-link to="/">홈</router-link>
      <span>></span>
      <router-link to="/company">업체 리스트</router-link>
      <span>></span>
      <router-link to="/company/create">조직 생성</router-link>
    </div>

    <div class="container">
      <form class="m-auto" v-on:submit.prevent="create_organization">
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
                   maxlength="100">
          </div>

          <label for="org_sub" class="col-form-label-sm col-sm-3 mt-3">
            <span>상호명</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <div class="error_label" v-if="errors.has('org_sub')">{{errors.first('org_sub')}}</div>
            <input class="form-control" id="org_sub" name="org_sub" type="text"
                   v-model="create_obj.org_sub_name"
                   placeholder="상호명을 입력하세요"
                   autofocus="autofocus"
                   maxlength="100"
            >
          </div>

          <label for="org_header" class="col-form-label-sm col-sm-3 mt-3">
            <span>조직 관리자</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <select class="form-control col-md-12 m-auto" name="org_header" id="org_header"
                    v-model="create_obj.org_header">
              <option value="0" selected>추후에 선택합니다</option>
              <option v-for="item in marketer_list" :value="item.id">
                {{ item.username }} / {{ item.email }}
              </option>
            </select>
          </div>

          <label for="org_addr" class="col-form-label-sm col-sm-3 mt-3">
            <span>주소</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input class="form-control" id="org_addr" name="org_addr" type="text"
                   v-model="create_obj.org_address"
                   placeholder="주소를 입력하세요"
                   autofocus="autofocus"
                   maxlength="200">
          </div>

          <label for="org_corp" class="col-form-label-sm col-sm-3 mt-3">
            <span>사업자 번호</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input class="form-control" id="org_corp" name="org_corp" type="text"
                   v-model="create_obj.org_crn"
                   placeholder="사업자 번호를 입력하세요"
                   autofocus="autofocus"
                   maxlength="50">
          </div>

          <label for="org_phone" class="col-form-label-sm col-sm-3 mt-3">
            <span>연락처</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input :class="error_label.class.tel_num" id="org_phone" name="org_phone"
                   type="number"
                   v-model="create_obj.org_tel_num"
                   placeholder="연락처를 입력하세요"
                   autofocus="autofocus"
                   maxlength="16"
                   @keyup="error_check('phone')">
          </div>

          <label for="org_email" class="col-form-label-sm col-sm-3 mt-3">
            <span>이메일</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input :class="error_label.class.email" id="org_email" name="org_email" type="email"
                   v-model="create_obj.org_email"
                   placeholder="이메일을 입력하세요"
                   maxlength="50"
                   autofocus="autofocus"
                   v-validate="'email'"
                   @keyup="error_check('email')">
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
    name: "company_create",
    data: () => ({
      // For organization create
      error_label:{
        org_name: false,
        org_tel_num: false,
        org_email: false,
        class: {
          name: 'form-control',
          tel_num: 'form-control',
          email: 'form-control'
        }
      },
      create_obj: {
        org_name: '',
        org_sub_name: '',
        org_header: 0,
        org_address: '',
        org_crn: '',
        org_tel_num: '',
        org_email: '',
        org_desc: ''
      },
      marketer_list: []
    }),
    mounted() {
      axios.get(this.$store.state.endpoints.baseUrl + 'user')
        .then((response) => {
          this.marketer_list = response.data.results
          for (let i = 0; i < this.marketer_list.length; i ++) {
            if (this.marketer_list[i].username == '') {
              this.marketer_list[i].username = '이름없음'
            }
          }
        })
        .catch((error) => {
          console.log('Get user is failed', error)
        })
    },
    methods: {
      error_check(param) {
        if (param === 'phone') {
          // Phone validate
          console.log('param is phone')
          if (this.create_obj.org_tel_num !== '') {
            let rgTel = /^(?:(010\d{4})|(01[1|6|7|8|9]\d{3,4})|(070\d{4}))(\d{4})$/
            let strValue = this.create_obj.org_tel_num
            let test_flag = rgTel.test(strValue)
            if (!test_flag) {
              this.error_label.org_tel_num = true
              this.error_label.class.tel_num = 'form-control alert-danger'
            } else {
              this.error_label.org_tel_num = false
              this.error_label.class.tel_num = 'form-control alert-success'
            }
          } else {
            this.error_label.org_tel_num = false
            this.error_label.class.tel_num = 'form-control'
          }
        // /Phone validate
        } else if (param === 'email') {
          // Email validate
          if (this.create_obj.org_email !== '') {
            if(this.$validator.errors.has('org_email')) {
              this.error_label.org_email = true
              this.error_label.class.email = 'form-control alert-danger'
            } else {
              this.error_label.org_email = false
              this.error_label.class.email = 'form-control alert-success'
            }
          } else {
            this.error_label.org_email = false
            this.error_label.class.email = 'form-control'
          }
          // /Email validate
        }
      },
      create_organization() {
        // Create an organization myself
        this.$validator.validateAll()
        if(confirm('업체를 생성하시겠습니까?')) {
          axios.post(this.$store.state.endpoints.baseUrl + 'organization/', this.create_obj)
            .then(() => {
              alert('업체가 생성되었습니다.')
              this.$router.currentRoute.meta.protect_leave = 'no'
              this.$router.push({
                name: 'organization_list'
              })
            })
            .catch((error) => {
              console.log(error)
            })
        }
      }
    },
    computed: {
      user_obj() {
        // Get user information
        let store_user = this.$store.state.authUser
        let user_json = {}
        if (Object.keys(store_user).length === 0 && store_user.constructor) {
          // dummy block access auth
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
        }
        return user_json
      }
    }
  }
</script>

<style lang="scss">

</style>

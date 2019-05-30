<template>
  <div class="main">

    <div class="main">
      <div class="text_navigation">
        <router-link to="/">홈</router-link>
        <span>></span>
        <router-link to="/myinfo">내 정보</router-link>
      </div>
    </div>

    <div class="container">
      <form class="m-auto" v-on:submit.prevent="check">
        <div class="form-group row">

          <label for="my_id" class="col-form-label-sm col-sm-3 mt-3">이메일</label>
          <div class="col-sm-9 mt-sm-3">
            <div class="form-control border-0" id="my_id">{{ content_obj.email }}</div>
          </div>

          <label for="my_pw" class="col-form-label-sm col-sm-3 mt-3">비밀번호</label>
          <div class="col-sm-9 mt-sm-3">
            <input type="password" :class="error_label.class.password" id="my_pw"
                   v-model="or_pass"
                   maxlength="30"
                   name="id_password"
                   required
                   @keyup="error_check('password')"/>
          </div>

          <label for="my_pw2" class="col-form-label-sm col-sm-3 mt-3">비밀번호 재확인</label>
          <div class="col-sm-9 mt-sm-3">
            <div class="error_label" v-if="errors.has('password')">{{errors.first('re_password')}}</div>
            <input type="password" :class="error_label.class.password" id="my_pw2"
                   v-model="re_pass"
                   maxlength="30"
                   name="re_password"
                   required
                   @keyup="error_check('password')"/>
          </div>

          <label for="my_name" class="col-form-label-sm col-sm-3 mt-3">이름</label>
          <div class="col-sm-9 mt-sm-3">
            <div class="error_label" v-if="errors.has('full_name')">{{errors.first('full_name')}}</div>
            <input type="text" id="my_name" class="form-control" v-model="content_obj.username"
                   v-validate="'required'"
                   name="full_name"
                   maxlength="30"
                   autofocus="autofocus"
                   required/>
          </div>

          <label for="my_phone" class="col-form-label-sm col-sm-3 mt-3">전화</label>
          <div class="col-sm-9 mt-sm-3">
            <div class="error_label" v-if="errors.has('phone')">{{errors.first('phone')}}</div>
            <input type="tel" id="my_phone" :class="error_label.class.phone"
                   v-model="content_obj.info.phone_num"
                   v-validate="'numeric|max:16'"
                   name="phone"
                   autofocus="autofocus"
                   maxlength="16"
                   @keyup="error_check('phone')"/>
          </div>

          <!--<label class="col-form-label-sm col-sm-3 mt-3" for="select_org">소속</label>
          <div class="col-sm-9 mt-sm-3">
            <select v-if="access_obj.access == 1 || access_obj.access == -1" name="select_org" id="select_org"
                    class="form-control"
                    v-model="access_obj.organization">
              <option value="-1">조직을 선택하세요..</option>
              &lt;!&ndash;<option value="-2">조직을 생성하겠습니다.</option>&ndash;&gt;
              <option v-for="item in select_options" :value="item.id">{{ item.name }}</option>
            </select>
            <select v-else-if="access_obj.access == 2 || access_obj.access == -2" name="select_company"
                    id="select_company" class="form-control"
                    v-model="access_obj.company">
              <option value="-1">업체를 선택하세요..</option>
              <option v-for="item in select_options" :value="item.id">{{ item.name }}</option>
            </select>
          </div>-->

          <label for="my_join" class="col-form-label-sm col-sm-3 mt-3">가입일</label>
          <div class="col-sm-9 mt-sm-3">
            <div v-if="content_obj.date_joined" type="text" id="my_join" class="form-control border-0">
              {{ (content_obj.date_joined).substring(0, 10) }}
            </div>
            <div v-else type="text" class="form-control border-0">Loading..</div>
          </div>

        </div>

        <button type="submit" class="btn btn-primary col-12">수정</button>
      </form>
      <button type="button" class="btn btn-danger mt-2 col-12" @click="bye">탈퇴</button>
      <router-link to="/landing">
        <button type="button" class="btn btn-dark col-12 mt-2 mb-3">취소</button>
      </router-link>
    </div>
  </div>
</template>

<script>
  export default {
    name: "my_info",
    created() {
      this.$store.state.pageOptions.landing.page = 1
      this.$store.state.pageOptions.landing.option = 0
      this.$store.state.pageOptions.landing.text = ''
      this.$store.state.pageOptions.user.page = 1
      this.$store.state.pageOptions.user.option = 0
      this.$store.state.pageOptions.user.text = ''
      this.$store.state.pageOptions.organization.page = 1
      this.$store.state.pageOptions.organization.option = 0
      this.$store.state.pageOptions.organization.text = ''
      this.$store.state.pageOptions.company.page = 1
      this.$store.state.pageOptions.company.option = 0
      this.$store.state.pageOptions.company.text = ''
    },
    data: () => ({
      or_pass: '',
      re_pass: '',
      error_label: {
        email: false,
        password: false,
        name: false,
        phone: false,
        class: {
          email: 'form-control',
          password: 'form-control',
          name: 'form-control',
          phone: 'form-control'
        }
      },
      content_obj: {}
    }),
    mounted() {
      this.content_obj = this.user_obj
      console.log(this.content_obj)
    },
    methods: {
      page_init() {
        let option = this.$store.state.pageOptions

        // Init other pages options
        option.company.page = 1
        option.company.option = 0
        option.company.text = ''
        option.organization.page = 1
        option.organization.option = 0
        option.organization.text = ''
        option.landing.page = 1
        option.landing.option = 0
        option.landing.text = ''
        option.user.page = 1
        option.user.option = 0
        option.user.text = ''

        // Follow inited search options
        let offset = (this.$store.state.pageOptions.user.page - 1) * this.page_chunk
        this.temp_option = this.search_option

      },
      error_check(param) {
        if (param === 'phone') {
          if (this.create_obj.phone !== '') {
            let rgTel = /^(?:(010\d{4})|(01[1|6|7|8|9]\d{3,4})|(070\d{4}))(\d{4})$/
            let strValue = this.create_obj.phone
            let test_flag = rgTel.test(strValue)
            if (!test_flag) {
              this.error_label.phone = true
              this.error_label.class.phone = 'form-control alert-danger'
            } else {
              this.error_label.phone = false
              this.error_label.class.phone = 'form-control alert-success'
            }
          } else {
            this.error_label.phone = false
            this.error_label.class.phone = 'form-control'
          }
        } else if (param === 'password') {
          if (this.or_pass == '' || this.re_pass == '') {
            this.error_label.password = false
            this.error_label.class.password = 'form-control'
          } else {
            if (this.or_pass === this.re_pass) {
              this.error_label.password = true
              this.error_label.class.password = 'form-control alert-success'
            } else {
              this.error_label.password = false
              this.error_label.class.password = 'form-control alert-danger'
            }
          }
        } /*else if (param === 'email') {
          // Duplicated function has to add
          if (this.create_obj.email !== '') {
            // If email is not empty
            let users = []
            axios.get(this.$store.state.endpoints.baseUrl + 'user/')
              .then((response) => {

                users = response.data.results
                let email_flag = false

                if (users.length !== 0) {
                  for (let i = 0; i < users.length; i++) {
                    if (users[i].email == this.create_obj.email) {
                      email_flag = true
                    }
                  }
                }

                this.error_label.email = email_flag

                // If has error atleast one thing of check
                if (this.error_label.email || this.$validator.errors.has('email')) {
                  this.error_label.class.email = 'form-control alert-danger'
                } else if (!this.error_label.email && !this.$validator.errors.has('email')) {
                  // Nor both are clear
                  this.error_label.class.email = 'form-control alert-success'
                }
              })
              .catch((error) => {
                console.log('Email check axios failed', error)
              })

          } else {
            // If email is empty
            this.error_label.email = false
            this.error_label.class.email = 'form-control'
          }
        }*/
      },
      check() {
        // check validate first
        this.$validator.validateAll()
        if (this.password !== '' || this.re_password !== '') {
          if (this.password !== this.re_password) {
            this.pass_error = true
            alert('비밀번호를 확인하세요.')
          } else {
            this.pass_error = false
            this.content_obj.password = this.password
            this.put()
          }
        } else if (this.password === '' && this.re_password === '') {
          this.pass_error = true
          alert('비밀번호는 필수 항목입니다.')
        }
      },
      put() {
        // Are you sure?
        if (confirm('정보를 수정하시겠습니까?')) {
          axios.patch(this.$store.state.endpoints.baseUrl + 'user/' + this.user_obj.id + '/', this.content_obj)
            .then(() => {
              alert('수정되었습니다. 다시 로그인 하세요.')
              this.$store.commit('removeToken')
              this.$router.currentRoute.meta.protect_leave = 'no'
              this.$router.push({
                name: 'sign_in'
              })
            })
            .catch((error) => {
              console.log(error)
            })
        }
      },
      bye() {
        if (confirm('정말 탈퇴하시겠습니까?')) {
          if (this.user_obj.id) {
            let axios = this.$axios
            axios.delete(this.$store.state.endpoints.baseUrl + 'user/' + this.user_obj.id + '/')
              .then(() => {
                // Calculation for page_max
                alert('탈퇴되었습니다.')
                this.$store.commit('removeToken')
                this.$router.currentRoute.meta.protect_leave = 'no'
                this.$router.push({
                  name: 'sign_in'
                })
              })
              .catch((error) => {
                console.log(error)
              })
          }
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

<style scoped>
  .error_label {
    font-family: 'Nanums_regular', sans-serif;
    font-size: 14px;
    display: inline-block;
    padding: 1px 10px;
    color: #ee5151;
    border-radius: 5px;
    margin: 4px 0;
    border: 1px solid #ee5151;
    box-sizing: border-box;
  }
</style>

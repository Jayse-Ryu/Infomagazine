<template>
  <div class="main">

    <div class="text_navigation">
      <router-link to="/">홈</router-link>
      <span>></span>
      <router-link to="/users">유저 리스트</router-link>
      <span>></span>
      <router-link to="/users/create">고객 생성</router-link>
    </div>

    <div class="container">
      <h4>고객용 <span class="text-info">계정</span>을 생성합니다</h4>

      <form class="m-auto" v-on:submit.prevent="create_user">
        <div class="form-group row">

          <label for="email" class="col-form-label-sm col-sm-3 mt-3">
            <span>이메일*</span>
            <div class="error_label" v-if="error_label.email">이미 존재하는 이메일입니다!</div>
            <div class="error_label" v-else-if="errors.has('email')">이메일 형식을 확인해주세요!</div>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input :class="error_label.class.email" id="email" name="email" type="email"
                   v-model="create_obj.email"
                   placeholder="이메일을 입력하세요"
                   required
                   maxlength="50"
                   autofocus="autofocus"
                   v-validate="'email'"
                   @keyup="error_check('email')">
          </div>

          <label for="user_password" class="col-form-label-sm col-sm-3 mt-3">
            <span>비밀번호*</span>
          </label>

          <div class="col-sm-9 mt-sm-3 row pr-0">
            <div class="col-md-6 password_area">
              <input :class="error_label.class.password"
                     required
                     v-model="create_obj.password"
                     type="password"
                     placeholder="비밀번호를 입력하세요."
                     maxlength="20"
                     v-validate="'required'"
                     name="user_password"
                     id="user_password"
                     @keyup="error_check('password')">
            </div>

            <div class="col-md-6 password_area">
              <input :class="error_label.class.password"
                     required
                     v-model="re_pass"
                     type="password"
                     placeholder="비밀번호를 재입력 하세요."
                     maxlength="20"
                     v-validate="'required'"
                     name="re_password"
                     id="re_password"
                     @keyup="error_check('password')">
            </div>
          </div>

          <label for="user_name" class="col-form-label-sm col-sm-3 mt-3">
            <span>사용자 이름*</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input :class="error_label.class.name" id="user_name" name="user_name" type="text"
                   v-model="create_obj.user_name"
                   required
                   v-validate="'required'"
                   placeholder="사용자 이름을 입력하세요"
                   autofocus="autofocus"
                   maxlength="100">
          </div>

          <label for="user_phone" class="col-form-label-sm col-sm-3 mt-3">
            <span>연락처</span>
          </label>
          <div class="col-sm-9 mt-sm-3">
            <input :class="error_label.class.phone" id="user_phone" name="user_phone"
                   type="number"
                   v-model="create_obj.info.phone_num"
                   placeholder="연락처를 입력하세요"
                   autofocus="autofocus"
                   maxlength="16"
                   @keyup="error_check('phone')">
          </div>

        </div>
        <button type="submit" class="btn btn-primary col-12 mt-2 mb-2">고객 생성</button>
        <router-link to="/users">
          <button type="button" class="btn btn-dark col-12 mb-3">취소</button>
        </router-link>
      </form>
    </div>

  </div>
</template>

<script>
  export default {
    name: "user_create",
    data: () => ({
      // For organization create
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
      create_obj: {
        email: '',
        username: '',
        password: '',
        info: {
          access_role: 2,
          organization: null,
          company: null,
          phone_num: '',
        }
      }
    }),
    mounted() {

    },
    methods: {
      error_check(param) {
        if (param === 'phone') {
          if (this.create_obj.info.phone_num !== '') {
            let rgTel = /^(?:(010\d{4})|(01[1|6|7|8|9]\d{3,4})|(070\d{4}))(\d{4})$/
            let strValue = this.create_obj.info.phone_num
            let test_flag = rgTel.test(strValue)
            if (!test_flag) {
              this.error_label.phone = true
              this.error_label.class.phone = 'form-control alert-danger'
            } else {
              this.error_label.phone = false
              this.error_label.class.phone = 'form-control alert-info'
            }
          } else {
            this.error_label.phone = false
            this.error_label.class.phone = 'form-control'
          }
        } else if (param === 'password') {
          if (this.create_obj.password == '' || this.re_pass == '') {
            this.error_label.password = false
            this.error_label.class.password = 'form-control'
          } else {
            if (this.create_obj.password === this.re_pass) {
              this.error_label.password = true
              this.error_label.class.password = 'form-control alert-info'
            } else {
              this.error_label.password = false
              this.error_label.class.password = 'form-control alert-danger'
            }
          }
        } else if (param === 'email') {
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
                  this.error_label.class.email = 'form-control alert-info'
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
        }
      },
      create_user() {
        // Create an organization myself
        this.$validator.validateAll()
        if (confirm('고객 계정을 생성하시겠습니까?')) {
          this.$store.state.pageOptions.loading = true
          axios.post(this.$store.state.endpoints.baseUrl + 'user/', this.create_obj)
            .then(() => {
              alert('고객 계정이 생성되었습니다.')
              this.$store.state.pageOptions.loading = false
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

<style lang="scss" scoped>
  .password_area {
    padding: 0 0 0 15px;
  }
</style>

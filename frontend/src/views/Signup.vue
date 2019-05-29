<template>
  <div>
    <div class="main"></div>
    <div class="text_navigation">
      <router-link to="/">로그인</router-link>
      <span>></span>
      <router-link to="/signup">회원가입</router-link>
    </div>

    <!-- Login container start -->
    <div class="login_box container">
      <div class="login_border">

        <div class="logo_wrap">
          <router-link to="/">
            <div class="logo"><img src="../assets/logo3.png" alt="Logo"></div>
          </router-link>
        </div>

        <form class="login_form form-horizontal" id="LoginForm" @submit.prevent="sign_up">

          <div class="form-group block">
            <label for="email" class="col-sm-12 control-label">이메일*
              <div class="error_label" v-if="error_label.email">이미 존재하는 이메일입니다!</div>
              <div class="error_label" v-else-if="errors.has('email')">이메일 형식을 확인해주세요!</div>
            </label>
            <div class="col-sm-12">
              <input :class="error_label.class.email"
                     required
                     v-model="email"
                     type="email"
                     placeholder="이메일을 입력하세요."
                     autofocus="autofocus"
                     maxlength="100"
                     v-validate="'email'"
                     name="email"
                     id="email"
                     @change="error_check('email')">
            </div>
          </div>

          <div class="form-group row col-md-12 password_form block">
            <div class="col-md-6 password_area">
              <label for="id_password" class="control-label">비밀번호*</label>
              <div>
                <input :class="error_label.class.password"
                       required
                       v-model="password"
                       type="password"
                       placeholder="비밀번호를 입력하세요."
                       maxlength="20"
                       v-validate="'required'"
                       name="id_password"
                       id="id_password"
                       @keyup="error_check('password')">
              </div>
            </div>

            <div class="col-md-6 password_area">
              <label for="re_password" class="control-label">비밀번호 재입력*</label>
              <div>
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
          </div>

          <div class="form-group block">
            <label for="username" class="col-sm-12 control-label">사용자 이름*
              <div class="error_label" v-if="errors.has('username')">이름을 입력해주세요.</div>
            </label>
            <div class="col-sm-12">
              <input class="form-control"
                     required
                     v-validate="'required'"
                     v-model="username"
                     type="text"
                     placeholder="이름을 입력하세요."
                     autofocus="autofocus"
                     maxlength="30"
                     name="username"
                     id="username">
            </div>
          </div>

          <div class="form-group block">
            <label for="phone" class="col-sm-12 control-label">전화번호
              <div class="error_label" v-if="error_label.phone">전화번호 형식을 확인해주세요. (010~9, 070)</div>
            </label>
            <div class="col-sm-12">
              <input class="form-control"
                     v-model="phone"
                     type="number"
                     placeholder="연락처를 입력하세요."
                     autofocus="autofocus"
                     maxlength="16"
                     v-validate="'numeric|max:16'"
                     name="phone"
                     id="phone"
                     @keyup="error_check('phone')">
            </div>
          </div>

          <div class="form-group block">
            <div class="col-sm-offset-2 col click">
              <button type="submit" class="submit_btn btn btn-info col">회원가입</button>
              <button type="button" class="btn btn-dark col mt-2" @click="go_back">취소</button>
            </div>
          </div>

        </form>
      </div>

    </div>
  </div>
</template>

<script>
  export default {
    name: 'sign_up',
    data: () => ({
      account: '',
      password: '',
      re_pass: '',
      username: '',
      email: '',
      phone: '',
      select_options: [],
      error_label: {
        password: false,
        phone: false,
        email: false,
        class: {
          email: 'form-control',
          password: 'form-control'
        }
      }
    }),
    methods: {
      error_check(param) {
        if (param === 'phone') {
          if (this.phone !== '') {
            let rgTel = /^(?:(010\d{4})|(01[1|6|7|8|9]\d{3,4})|(070\d{4}))(\d{4})$/
            let strValue = this.phone
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
          if (this.password == '' || this.re_pass == '') {
            this.error_label.password = false
            this.error_label.class.password = 'form-control'
          } else {
            if (this.password === this.re_pass) {
              this.error_label.password = true
              this.error_label.class.password = 'form-control alert-success'
            } else {
              this.error_label.password = false
              this.error_label.class.password = 'form-control alert-danger'
            }
          }
        } else if (param === 'email') {
          // Duplicated function has to add
          if (this.email !== '') {
            // If email is not empty
            let users = []
            axios.get(this.$store.state.endpoints.baseUrl + 'user/')
              .then((response) => {

                users = response.data.results
                let email_flag = false

                if (users.length !== 0) {
                  for (let i = 0; i < users.length; i++) {
                    if (users[i].email == this.email) {
                      email_flag = true
                    }
                  }
                }

                this.error_label.email = email_flag

                // If has error atleast one thing of check
                if (this.error_label.email || this.$validator.errors.has('email')) {
                  this.error_label.class.email = 'form-control alert-danger'
                } else if (!this.error_label.email && !this.$validator.errors.has('email')){
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
        }
      },
      sign_up() {
        // Auto validation first
        this.$validator.validateAll()

        // Custom validation
        if (this.error_label.password != true) {
          // Check password matched
          alert('비밀번호를 확인해주세요.')
          document.getElementById('re_password').focus()
        } else if (this.error_label.phone) {
          // Check phone number validated
          alert('전화번호 형식을 확인해주세요.')
          document.getElementById('phone').focus()
        } else if (this.email == true) {
          // Check duplicated email address
          alert('이미 존재하는 이메일입니다.')
          document.getElementById('id_username').focus()
        } else {
          // Else clear, create a new user.
          let axios = this.$axios

          let formData = new FormData()
          formData.append('email', this.email)
          formData.append('password', this.password)
          formData.append('username', this.username)
          formData.append('phone', this.phone)

          // Axios config
          const config = {
            headers: {
              'Content-Type': 'application/json'
            },
            xhrFields: {
              withCredentials: true
            }
          }

          /* Do axios post */
          axios.post(this.$store.state.endpoints.baseUrl + 'user/', formData, config)
            .then(() => {
              alert('회원가입 되었습니다.')
              this.$router.currentRoute.meta.protect_leave = 'no'
              this.$router.push({
                name: 'sign_in',
              })
            })
            .catch((error) => {
              console.log(error)
              if (error.response.data.account) {
                alert(error.response.data.account)
              } else {
                alert('회원가입 중 문제가 발생하였습니다. 다시시도 해주세요.')
              }
            })
          /* /Axios post */
        }
      },
      go_back() {
        this.$router.push({
          name: 'sign_in',
        })
      }
    },
    mounted() {
      this.$parent.$data.header_flag = 0
    },
    destroyed() {
      this.$parent.$data.header_flag = 1
    }
  }
</script>

<style scoped lang="scss">

  .main {
    position: fixed;
    width: 100%;
    min-height: 100%;
    overflow: auto;
    max-width: none !important;
    top: 0;
    z-index: -1;
    background: linear-gradient(217deg, rgba(2, 0, 36, .8), rgba(255, 0, 0, 0) 70.71%),
    linear-gradient(127deg, rgba(141, 168, 185, .8), rgba(0, 255, 0, 0) 70.71%),
    linear-gradient(336deg, rgba(0, 212, 255, .8), rgba(0, 0, 255, 0) 70.71%);
  }

  .login_border {
    // max-height: 100vh;
    // min-height: 100vh;
    overflow: auto;
    background-color: rgba(255, 255, 255, 0.4);
    padding: 10vh 30px 55px;
    margin-bottom: 10vh;
    font-family: 'Nanum Gothic', 'sans-serif';
    // font-weight: bold;
    border-radius: 10px;
    box-shadow: 0px 0px 15px 5px rgba(0, 0, 0, 0.14);
  }

  .logo_wrap {
    width: 100%;

    .logo {
      width: 250px;
      margin: 10px auto;
      text-align: center;

      img {
        width: 100%;
      }
    }
  }

  .password_form {
    padding-right: 0;
    margin-bottom: 0;
  }

  .password_area {
    padding: 0 0 15px 15px;
  }

  .click {
    padding-top: 20px;
  }

  .error_label {
    font-family: 'Nanums_regular', sans-serif;
    font-size: 14px;
    display: inline-block;
    padding: 0 10px;
    color: #ee5151;
    border-radius: 5px;
    margin: 0 15px;
    border: 1px solid #ee5151;
    box-sizing: border-box;
  }

  .form-control, .btn-info {
    box-shadow: 0px 0px 10px 1px rgba(0, 0, 0, 0.14);
  }

  .text_navigation {
    margin: 1% 0 8% 15px !important;
  }

</style>

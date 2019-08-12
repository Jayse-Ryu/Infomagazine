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
                   v-model="content_obj.password"
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
            <!--<div class="error_label" v-if="errors.has('full_name')">{{errors.first('full_name')}}</div>-->
            <input type="text" id="my_name" :class="error_label.class.name"
                   v-model="content_obj.username"
                   v-validate="'required'"
                   name="full_name"
                   maxlength="30"
                   autofocus="autofocus"
                   required
                   @keyup="error_check('name')"/>
          </div>

          <label for="my_phone" class="col-form-label-sm col-sm-3 mt-3">전화</label>
          <div class="col-sm-9 mt-sm-3">
            <!--<div class="error_label" v-if="errors.has('phone')">{{errors.first('phone')}}</div>-->
            <input type="tel" id="my_phone" :class="error_label.class.phone"
                   v-model="content_obj.info.phone_num"
                   v-validate="'numeric|max:16'"
                   name="phone"
                   autofocus="autofocus"
                   maxlength="16"
                   @keyup="error_check('phone')"/>
          </div>

          <label for="my_join" class="col-form-label-sm col-sm-3 mt-3">가입일</label>
          <div class="col-sm-9 mt-sm-3">
            <div v-if="content_obj.date_joined" type="text" id="my_join" class="form-control border-0">
              {{ (content_obj.date_joined).substring(0, 10) }}
            </div>
            <div v-else type="text" class="form-control border-0">정보 없음</div>
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
      re_pass: '',
      error_label: {
        email: false,
        password: true,
        name: true,
        phone: false,
        class: {
          email: 'form-control',
          password: 'form-control',
          name: 'form-control',
          phone: 'form-control'
        }
      },
      content_obj: {
        email: '',
        username: '',
        password: '',
        info: {
          phone_num: ''
        }
      }
    }),
    mounted() {
      // this.content_obj = this.user_obj
      this.$store.state.pageOptions.loading = true
      axios.get(this.$store.state.endpoints.baseUrl + 'users/' + this.user_obj.id + '/')
        .then((response) => {
          // console.log('mounted response is ', response)
          this.content_obj = response.data.data
          this.$store.state.pageOptions.loading = false
        })
        .catch((error) => {
          this.$store.state.pageOptions.loading = false
          console.log(error)
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
        // let offset = (this.$store.state.pageOptions.user.page - 1) * this.page_chunk
        // this.temp_option = this.search_option
      },
      error_check(param) {
        if (param === 'phone') {
          if (this.content_obj.info.phone_num !== '') {
            let rgTel = /^(?:(010\d{4})|(01[1|6|7|8|9]\d{3,4})|(070\d{4}))(\d{4})$/
            let strValue = this.content_obj.info.phone_num
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
          if (this.content_obj.password == '' || this.re_pass == '') {
            this.error_label.password = true
            this.error_label.class.password = 'form-control'
          } else {
            if (this.content_obj.password === this.re_pass) {
              this.error_label.password = false
              this.error_label.class.password = 'form-control alert-info'
            } else {
              this.error_label.password = true
              this.error_label.class.password = 'form-control alert-danger'
            }
          }
        } else if (param === 'name') {
          if (this.content_obj.username === '') {
            this.error_label.name = true
            this.error_label.class.name = 'form-control alert-danger'
          } else {
            this.error_label.name = false
            this.error_label.class.name = 'form-control alert-info'
          }
        }
      },
      check() {
        // check validate first
        this.$validator.validateAll()
        if (this.error_label.password) {
          alert('비밀번호를 확인해주세요!')
          document.getElementById('my_pw2').focus()
        } else if (this.error_label.phone) {
          alert('전화번호 형식을 확인해주세요!')
          document.getElementById('my_phone').focus()
        } else if (this.error_label.name) {
          alert('이름을 입력하세요!')
          document.getElementById('my_name').focus()
        } else {
          this.put()
        }
      },
      put() {
        // Are you sure?
        if (confirm('정보를 수정하시겠습니까?')) {
          this.$store.state.pageOptions.loading = true
          axios.patch(this.$store.state.endpoints.baseUrl + 'users/' + this.user_obj.id + '/', this.content_obj)
            .then((response) => {
              console.log('user patch response?', response)
              // alert('수정되었습니다. 다시 로그인 하세요.')
              // this.$store.commit('removeToken')
              // this.$router.currentRoute.meta.protect_leave = 'no'
              // this.$router.push({
              //   name: 'sign_in'
              // })
              const payload = {
                email: this.user_obj.email,
                password: this.content_obj.password
              }

              axios.post(this.$store.state.endpoints.obtainJWT, payload)
                .then((response) => {
                  return this.$store.dispatch('obtainToken', response.data)
                  // try {
                  //   this.$cookie.set('token', response.data.token, {expires: '1D'})
                  //   this.$cookie.set('authUser', JSON.stringify(response.data.user), {expires: '1D'})
                  // } catch (error) {
                  //   console.log('set cookie error', error)
                  // }
                })
                .then(() => {
                  alert('수정되었습니다.')
                  this.$store.state.pageOptions.loading = false
                  this.$router.push({name: 'gateway'})
                })
                .catch((error) => {
                  this.$store.state.pageOptions.loading = false
                  console.log('Edit error', error)
                })
            })
            .catch((error) => {
              this.$store.state.pageOptions.loading = false
              console.log(error)
            })
        }
      },
      bye() {
        if (confirm('정말 탈퇴하시겠습니까?')) {
          if (this.user_obj.id) {
            // let axios = this.$axios
            this.$store.state.pageOptions.loading = true
            axios.delete(this.$store.state.endpoints.baseUrl + 'users/' + this.user_obj.id + '/')
              .then(() => {
                // Calculation for page_max
                alert('탈퇴되었습니다.')
                this.$store.state.pageOptions.loading = false
                this.$store.commit('removeToken')
                this.$router.currentRoute.meta.protect_leave = 'no'
                this.$router.push({
                  name: 'sign_in'
                })
              })
              .catch((error) => {
                this.$store.state.pageOptions.loading = false
                console.log(error)
              })
          }
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

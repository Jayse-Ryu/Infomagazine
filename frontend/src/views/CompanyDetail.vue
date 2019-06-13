<template>
  <div class="main">
    <div class="text_navigation">
      <router-link to="/">홈</router-link>
      <span>></span>
      <router-link to="/company">업체 리스트</router-link>
      <span>></span>
      <router-link to="/company/detail/{{}}">업체 정보</router-link>
    </div>

    <!---->

    <div class="container">
      <!-- 1. If user is this company's organization's marketer or staff, superuser -->
      <form v-if="user_obj.is_staff || user_obj.is_superuser || [0,1].includes(user_obj.info.access_role)"
            class="m-auto" v-on:submit.prevent="check_organization">

        <div class="form-group row">

          <label for="org_id" class="col-form-label-sm col-sm-3 mt-3">업체 번호</label>
          <div class="col-sm-9 mt-sm-3">
            <div class="form-control border-0" id="org_id">{{ content_obj.id }}</div>
          </div>

          <label for="org_name" class="col-form-label-sm col-sm-3 mt-3">관리조직</label>
          <div class="col-sm-9 mt-sm-3">
            <div class="form-control border-0" id="org_name">{{ content_obj.org_name }}</div>
          </div>

          <label for="com_name" class="col-form-label-sm col-sm-3 mt-3">업체 이름*</label>
          <div class="col-sm-9 mt-sm-3">
            <div class="error_label" v-if="errors.has('com_name')">이름은 필수 항목입니다.</div>
            <input type="text" :class="error_label.class.name" id="com_name" name="com_name"
                   v-model="content_obj.corp_name"
                   required
                   placeholder="업체 이름을 입력하세요"
                   autofocus="autofocus"
                   maxlength="100"
                   v-validate="'required'"
                   @keyup="error_check('name')">
          </div>

          <label for="org_sub" class="col-form-label-sm col-sm-3 mt-3">업체 상호명</label>
          <div class="col-sm-9 mt-sm-3">
            <input type="text" class="form-control" id="org_sub" name="org_sub"
                   v-model="content_obj.corp_sub_name"
                   placeholder="상호명을 입력하세요"
                   autofocus="autofocus"
                   maxlength="100">
          </div>

          <label for="org_header" class="col-form-label-sm col-sm-3 mt-3">대표자</label>
          <div class="col-sm-9 mt-sm-3">
            <input type="text" class="form-control" id="org_header"
                   v-model="content_obj.corp_header"
                   placeholder="업체 대표를 입력하세요"
                   autofocus="autofocus"
                   maxlength="20">
          </div>

          <label for="org_address" class="col-form-label-sm col-sm-3 mt-3">주소</label>
          <div class="col-sm-9 mt-sm-3">
            <input type="text" class="form-control" id="org_address"
                   v-model="content_obj.corp_address"
                   placeholder="주소를 입력하세요"
                   autofocus="autofocus"
                   maxlength="200">
          </div>

          <label for="org_corp" class="col-form-label-sm col-sm-3 mt-3">사업자번호</label>
          <div class="col-sm-9 mt-sm-3">
            <input type="text" class="form-control" id="org_corp" v-model="content_obj.corp_crn"
                   placeholder="사업자 번호를 입력하세요"
                   autofocus="autofocus"
                   maxlength="50">
          </div>

          <label for="org_phone" class="col-form-label-sm col-sm-3 mt-3">연락처</label>
          <div class="col-sm-9 mt-sm-3">
            <div class="error_label" v-if="errors.has('org_phone')">전화번호를 확인하세요</div>
            <input type="number" :class="error_label.class.phone" id="org_phone" name="org_phone"
                   v-model="content_obj.corp_num"
                   placeholder="연락처를 입력하세요"
                   autofocus="autofocus"
                   maxlength="16"
                   v-validate="'numeric|max:16'"
                   @keyup="error_check('phone')">
          </div>

          <label for="org_email" class="col-form-label-sm col-sm-3 mt-3">이메일</label>
          <div class="col-sm-9 mt-sm-3">
            <div class="error_label" v-if="errors.has('org_email')">이메일 형식을 확인하세요</div>
            <input type="email" :class="error_label.class.email" id="org_email" name="org_email"
                   v-model="content_obj.corp_email"
                   placeholder="이메일을 입력하세요"
                   maxlength="50"
                   autofocus="autofocus"
                   v-validate="'email'"
                   @keyup="error_check('email')">
          </div>

          <label for="org_desc" class="col-form-label-sm col-sm-3 mt-3">설명</label>
          <div class="col-sm-9 mt-sm-3">
            <input type="text" class="form-control" id="org_desc" v-model="content_obj.corp_desc"
                   placeholder="업체 설명을 적어주세요"
                   autofocus="autofocus"
                   maxlength="200">
          </div>

          <label for="org_create" class="col-form-label-sm col-sm-3 mt-3">생성일</label>
          <div v-if="content_obj.created_date" class="col-sm-9 mt-sm-3">
            <div type="text" class="form-control border-0" id="org_create">
              {{ (content_obj.created_date).substring(0, 10) }}
            </div>
          </div>
          <div v-else class="col-sm-9 mt-sm-3">
            <div type="text" class="form-control border-0">비어있음</div>
          </div>

          <label for="org_update" class="col-form-label-sm col-sm-3 mt-3">수정일</label>
          <div v-if="content_obj.updated_date" class="col-sm-9 mt-sm-3">
            <div type="text" class="form-control border-0" id="org_update">
              {{ (content_obj.updated_date).substring(0, 10) }}
            </div>
          </div>
          <div v-else class="col-sm-9 mt-sm-3">
            <div type="text" class="form-control border-0">비어있음</div>
          </div>

        </div>

        <!-- Section 2. If width is big -->
        <div v-if="window_width > 1000" class="list_area">
          <div>
            <div class="list-group-item  d-inline-flex justify-content-between p-1 pt-2 pb-2 text-center"
                 style="border-radius: 0; border-bottom: 0; width:100%;">
              <div class="col-2 col-sm-1">번호</div>
              <div class="col-3 col-sm-3">아이디</div>
              <div class="col-3 col-sm-3">이름</div>
              <div class="col-2">연락처</div>
              <div class="col-2 col-sm-3">관리</div>
            </div>
          </div>
          <ul class="list-group list-group-flush col-12 pr-0 text-center">
            <li v-if="user_list.length === 0"
                class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1">
              <div class="col-12 text-center">데이터가 존재하지 않습니다.</div>
            </li>
            <li v-else class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1"
                v-for="content in user_list">
              <div class="col-2 col-sm-1">{{ content.id }}</div>
              <div class="col-3 col-sm-3">
                <router-link :to="'/users/detail/' + content.user">{{ content.email }}</router-link>
              </div>
              <div class="col-3 col-sm-3">
                <router-link :to="'/users/detail/' + content.user">{{ content.username }}</router-link>
              </div>
              <div class="col-2">{{ content.phone_num }}</div>
              <div class="col-2 col-sm-3">
                <div v-if="content.access == 2 && content.user != user_obj.id">
                  <button type="button" class="btn btn-danger p-0" @click.prevent="promote('de', content.user)">
                    <div class="promote_btn">강등</div>
                  </button>
                </div>
                <div v-else-if="content.access == 2 && content.user == user_obj.id">
                  <button type="button" class="btn btn-info p-0">
                    <div class="promote_btn">본인</div>
                  </button>
                </div>
                <div v-if="content.access == -2">
                  <button type="button" class="btn btn-success p-0" @click.prevent="promote('pr', content.user)">
                    <div class="promote_btn">승인</div>
                  </button>
                </div>
              </div>
            </li>
          </ul>
        </div>

        <!-- Section 2. Else if width is small -->
        <div v-else class="list_area text-center">
          <div>
            <div class="list-group-item  d-inline-flex justify-content-between p-1 pt-2 pb-2"
                 style="border-radius: 0; border-bottom: 0; width:100%;">
              <div class="col-4">아이디</div>
              <div class="col-4">이름</div>
              <div class="col-4">관리</div>
            </div>
          </div>
          <ul class="list-group list-group-flush col-12 pr-0">
            <li v-if="user_list.length === 0"
                class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1">
              <div class="col-12 text-center">데이터가 존재하지 않습니다.</div>
            </li>
            <li v-else class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1"
                v-for="content in user_list">
              <div class="col-4">{{ content.email }}</div>
              <div class="col-4">
                <router-link :to="'/users/detail/' + content.id">{{ content.username }}</router-link>
              </div>
              <div class="col-4">
                <div v-if="content.access == 1 && content.id == original_manager">
                  <button type="button" class="btn btn-primary p-0" @click.prevent="promote('he', content.id)">
                    <div class="promote_btn">관리자</div>
                  </button>
                </div>
                <div v-else-if="content.access == 1 && content.id != original_manager && content.id != user_obj.id">
                  <button type="button" class="btn btn-danger p-0" @click.prevent="promote('de', content.id)">
                    <div class="promote_btn">강등</div>
                  </button>
                </div>
                <div v-else-if="content.access == 1 && content.id == user_obj.id">
                  <button type="button" class="btn btn-info p-0" @click.prevent="promote('me', content.id)">
                    <div class="promote_btn">본인</div>
                  </button>
                </div>
                <div v-if="content.access == -1">
                  <button type="button" class="btn btn-success p-0" @click.prevent="promote('pr', content.id)">
                    <div class="promote_btn">승인</div>
                  </button>
                </div>
              </div>
            </li>
          </ul>
        </div>

        <!-- Pagination buttons -->
        <paginate class="pagination"
                  v-model="page_current"
                  :page-count="page_max"
                  :page-range="5"
                  :margin-pages="1"
                  :click-handler="pagination"
                  :prev-text="'<'"
                  :next-text="'>'"
                  :container-class="'page-item'"
                  :page-class="'page-link'"
                  :prev-class="'page-link prev'"
                  :next-class="'page-link next'"
                  :active-class="'active'"
                  :disabled-class="'disabled'">
        </paginate>

        <!-- Submit button -->
        <div class="mt-1 mb-2">
          <button type="submit" class="btn btn-primary col">수정</button>
          <!--<button type="button">업체 삭제</button>-->
          <router-link to="/organization">
            <button class="btn btn-dark col mt-2">취소</button>
          </router-link>
        </div>
      </form>

      <!-- If no one try to access to this company -->
      <div v-else>
        <div class="m-auto text-center pt-3">권한이 없습니다.</div>
      </div>

    </div>
  </div>
</template>

<script>
  export default {
    name: "company_detail",
    data: () => ({
      error_label: {
        name: false,
        phone: false,
        email: false,
        class: {
          name: 'form-control',
          phone: 'form-control',
          email: 'form-control'
        }
      },
      page_id: 0,
      window_width: window.innerWidth,
      content_obj: [],
      marketer: [],
      original_manager: 0,
      user_list: [],
      page_current: 1,
      page_max: 0,
      page_chunk: 10,
    }),
    mounted() {
      // Window width calculator
      let that = this
      that.$nextTick(function () {
        window.addEventListener('resize', function (e) {
          that.window_width = window.innerWidth
        })
      })

      // get id from url
      this.page_id = this.$route.params.company_id * 1

      // if page int is default, push to list page
      if (this.page_id === 0) {
        this.$router.push({
          name: 'company_list'
        })
      }

      // Get Company by page_id
                  this.$store.state.pageOptions.loading = true
      axios.get(this.$store.state.endpoints.baseUrl + 'companies/' + this.page_id)
        .then((response) => {
          console.log('company response is? ', response)
          this.content_obj = response.data.data
          this.$store.state.pageOptions.loading = false
          return axios.get(this.$store.state.endpoints.baseUrl + 'user/?company_id=' + this.page_id)
        })
        .catch((error) => {
          console.log('Mount Get company error', error)
          this.$store.state.pageOptions.loading = false
        })

        .then((response) => {
          this.user_list = response.data.results
          this.$store.state.pageOptions.loading = false
        })
        .catch((error) => {
          console.log('Mount Get user list error', error)
          this.$store.state.pageOptions.loading = false
        })
    },
    methods: {
      error_check(param) {
        if (param === 'phone') {
          // Phone validate
          if (this.content_obj.corp_num !== '') {
            // Allow mobile phone, internet wireless
            let regular_tel = /^(?:(010\d{4})|(01[1|6|7|8|9]\d{3,4})|(070\d{4}))(\d{4})$/
            let tel_num = this.content_obj.corp_num
            let test_flag = regular_tel.test(tel_num)
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
          // /Phone validate
        } else if (param === 'email') {
          // Email validate
          if (this.content_obj.corp_email !== '') {
            if (this.$validator.errors.has('org_email')) {
              this.error_label.email = true
              this.error_label.class.email = 'form-control alert-danger'
            } else {
              this.error_label.email = false
              this.error_label.class.email = 'form-control alert-info'
            }
          } else {
            this.error_label.email = false
            this.error_label.class.email = 'form-control'
          }
        } else if (param === 'name') {
          // Org name validate
          if (this.content_obj.corp_name === '') {
            this.error_label.name = true
            this.error_label.class.name = 'form-control alert-danger'
          } else {
            this.error_label.name = false
            this.error_label.class.name = 'form-control alert-info'
          }
        }
      },
      refresh_organization() {
        this.page_id = this.$route.params.company_id * 1

        // if page int is default, push to list page
        if (this.page_id === 0) {
          this.$router.push({
            name: 'company_list'
          })
        }
        // get object

        // Get Company by page_id
        axios.get(this.$store.state.endpoints.baseUrl + 'companies/' + this.page_id)
          .then((response) => {
            this.content_obj = response.data
            this.original_manager = response.data.manager
            // Get access manager users by organization id
            return axios.get(this.$store.state.endpoints.baseUrl + 'user_access/' + '?organization=' + response.data.organization)
          })
          .then((response) => {
            // Filtering allowed managers
            this.marketer = []
            for (let i = 0; i < response.data.results.length; i++) {
              if (response.data.results[i].access === 1) {
                this.marketer.push(response.data.results[i])
              }
            }
          })
          .catch((error) => {
            console.log('refresh function', error)
          })
      },
      check_organization() {
        // Validate for make an organization
        this.$validator.validateAll()
        // or
        if (confirm('수정하시겠습니까?')) {
          if (this.content_obj.manager !== this.original_manager) {
            if (confirm('관리자를 교체하시겠습니까?')) {
              this.patch_organization()
            } else {
              alert('수정이 취소되었습니다.')
            }
          } else {
            this.patch_organization()
          }
        }
      },
      patch_organization() {
        // Create an organization myself
        let axios = this.$axios
        let this_url = 'companies/'
        let formData = new FormData()
        formData.append('name', this.content_obj.name)
        formData.append('manager', this.content_obj.manager)
        if (this.content_obj.sub_name) {
          formData.append('sub_name', this.content_obj.sub_name)
        }
        if (this.content_obj.header) {
          formData.append('header', this.content_obj.header)
        }
        if (this.content_obj.address) {
          formData.append('address', this.content_obj.address)
        }
        if (this.content_obj.corp_num) {
          formData.append('corp_num', this.content_obj.corp_num)
        }
        if (this.content_obj.phone) {
          formData.append('phone', this.content_obj.phone)
        }
        if (this.content_obj.email) {
          formData.append('email', this.content_obj.email)
        }
        axios.patch(this.$store.state.endpoints.baseUrl + this_url + this.page_id + '/', formData)
          .then((response) => {
            alert('수정되었습니다.')
            this.original_manager = this.content_obj.manager
            this.$store.dispatch('getAuthUser')
            this.refresh_organization()
          })
          .catch((error) => {
            console.log(error)
          })
      },
      pagination(pageNum) {
        // when page is first, max ~ max-(chunk*current)+1
        // when page is max, max-(chunk*(current-1)) ~ 1
        // when page is middle, max-(chunk*(current-1)) ~ max-(chunk*current)+1
        let offset = (pageNum - 1) * this.page_chunk
        this.calling_all_unit(offset)
      },
      calling_all_unit(page) {
        // Calling landings with new values
        let axios = this.$axios
        let offset = page
        axios.get(this.$store.state.endpoints.baseUrl + 'user/' + '?offset=' + offset + '&' + 'company' + '=' + this.$route.params.company_id * 1)
          .then((response) => {
            // Calculation for page_max
            if (response.data.count % this.page_chunk === 0) {
              this.page_max = Math.floor(response.data.count / this.page_chunk)
            } else {
              this.page_max = Math.floor(response.data.count / this.page_chunk) + 1
            }
            // Get all of users in this organization whatever allowed or not
            this.user_list = response.data.results
          })
          .catch((error) => {
            console.log('calling all unit function', error)
          })
      },
      promote(option, user) {
        // head:he me:me demote:de promote:pr
        let axios = this.$axios
        if (option == 'he') {
        } else if (option == 'me') {
        } else if (option == 'pr') {
          if (confirm('가입을 승인하시겠습니까?')) {
            let formData = new FormData()
            formData.append('access', '2')
            axios.patch(this.$store.state.endpoints.baseUrl + 'user/' + user + '/', formData)
              .then((response) => {
                alert('유저의 가입이 승인되었습니다.')
                this.calling_all_unit()
                this.refresh_organization()
              })
              .catch((error) => {
                console.log(error)
                alert('처리중 문제가 발생하였습니다.')
              })
          } else {
            alert('승인 취소됨.')
          }
        } else if (option == 'de') {
          if (confirm('유저를 강등시킵니까?')) {
            let formData = new FormData()
            formData.append('access', '-2')
            axios.patch(this.$store.state.endpoints.baseUrl + this_url + user + '/', formData)
              .then((response) => {
                alert('유저가 강등되었습니다.')
                this.calling_all_unit()
                this.refresh_organization()
              })
              .catch((error) => {
                console.log(error)
                alert('처리중 문제가 발생하였습니다.')
              })
          } else {
            alert('강등 취소됨.')
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
            'info': {
              'access_role': 3
            },
            'failed': true
          }
        } else {
          user_json = JSON.parse(local_user)
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
    padding: 1px 5px;
    color: #ee5151;
    border-radius: 5px;
    margin: 5px 0;
    border: 1px solid #ee5151;
    box-sizing: border-box;
  }

  .promote_btn {
    padding: 0 4px;
    min-width: 50px;
    font-size: 0.83em;
  }
</style>

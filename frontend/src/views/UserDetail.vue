<template>
  <div class="main">
    <div class="text_navigation">
      <router-link to="/">홈</router-link>
      <span>></span>
      <router-link to="/users">유저 리스트</router-link>
      <span>></span>
      <router-link to="/users/detail/{{}}">유저 정보</router-link>
    </div>

    <div class="container pb-4">
      <div class="form-group row">

        <label for="user_num" class="col-form-label-sm col-sm-3 mt-3">번호</label>
        <div class="col-sm-9 mt-sm-3">
          <div class="form-control border-0" id="user_num">{{ content_obj.id }}</div>
        </div>

        <label for="user_id" class="col-form-label-sm col-sm-3 mt-3">이메일</label>
        <div class="col-sm-9 mt-sm-3">
          <div class="form-control" id="user_id">{{ content_obj.email }}</div>
        </div>

        <label for="user_name" class="col-form-label-sm col-sm-3 mt-3">이름</label>
        <div class="col-sm-9 mt-sm-3">
          <div class="form-control" id="user_name" v-if="content_obj.username">
            {{ content_obj.username }}
          </div>
          <div v-else class="form-control">이름없음</div>
        </div>

        <label for="user_phone" class="col-form-label-sm col-sm-3 mt-3">연락처</label>
        <div class="col-sm-9 mt-sm-3">
          <div v-if="content_obj.info.phone_num" class="form-control" id="user_phone">
            {{ content_obj.info.phone_num }}
          </div>
          <div v-else class="form-control">없음</div>
        </div>

        <!-- Grade handler -->
        <label for="user_access" class="col-form-label-sm col-sm-3 mt-3">등급</label>
        <div class="col-sm-9 mt-sm-3 justify-content-between">

          <div v-if="[0,1].includes(content_obj.info.access_role)">
            <div class="form-control border-0 p-0" id="user_access">
              <div class="badge alert alert-success mr-3">마케터</div>
              <button v-if="content_obj.id != user_obj.id && user_obj.is_staff || user_obj.is_superuser" type="button"
                      class="btn btn-outline-danger" @click.prevent="grade_set(3)">승인취소
              </button>
              <div v-else-if="content_obj.id == user_obj.id" class="btn btn-info disabled">본인</div>
              <div v-else class="btn btn-secondary disabled">변경 권한없음</div>
            </div>
          </div>

          <div v-else-if="content_obj.info.access_role == 2">
            <div class="form-control border-0 p-0" id="user_access">
              <div class="badge alert alert-secondary mr-3">고객</div>
              <!--<button v-if="content_obj.user !== user_obj.id" type="button" class="btn btn-outline-danger"
                      @click.prevent="grade_set(2)">강등
              </button>
              <div v-else class="btn btn-secondary disabled">변경 권한없음</div>-->
            </div>
          </div>

          <div v-else-if="content_obj.info.access_role == 3">
            <div class="form-control border-0 p-0" id="user_access">
              <div class="badge alert alert-danger mr-3">미인증 마케터</div>
              <button v-if="user_obj.is_staff || user_obj.is_superuser" type="button"
                      class="btn btn-outline-primary" @click.prevent="grade_set(1)">승인
              </button>
              <div v-else class="btn btn-secondary disabled">변경 권한없음</div>
            </div>
          </div>

        </div>

        <label v-if="content_obj.info.organization" for="user_companion"
               class="col-form-label-sm col-sm-3 mt-3">소속</label>
        <label v-else-if="content_obj.info.company" for="user_companion"
               class="col-form-label-sm col-sm-3 mt-3">업체</label>
        <label v-else for="user_companion" class="col-form-label-sm col-sm-3 mt-3">업체</label>
        <div class="col-sm-9 mt-sm-3">
          <div v-if="content_obj.info.organization" class="form-control" id="user_companion">
            {{ content_obj.info.organization }}
          </div>
          <div v-else-if="content_obj.info.company" class="form-control" id="user_companion">
            {{ content_obj.info.company }}
          </div>
          <div v-else class="form-control" id="user_companion">생성예정</div>
        </div>

        <!--<label for="my_join" class="col-form-label-sm col-sm-3 mt-3">가입일</label>
        <div class="col-sm-9 mt-sm-3">
          <div v-if="content_obj.created_date" type="text" id="my_join" class="form-control border-0">
            {{ (content_obj.created_date).substring(0, 10) }}
          </div>
          <div v-else type="text" class="form-control border-0">{{ content_obj.created_date }}</div>
        </div>-->

      </div>

      <div v-if="content_obj.id !== user_obj.id">
        <!--
        &lt;!&ndash; I'm a superuser and this user is manager side &ndash;&gt;
        <div class="form-group row" v-if="user_obj.is_superuser || user_obj.is_staff">
          <label for="user_super_set" class="col-form-label-sm col-sm-3 mt-3">권한관리</label>

          &lt;!&ndash; if this user is 'NOT' staff &ndash;&gt;
          <div v-if="!content_obj.is_staff" class="col-sm-9 mt-sm-3">
            <div id="user_super_set">
              <button type="button" class="btn btn-info w-100" @click.prevent="staff_set('promote')">
                운영자로 승급
              </button>
            </div>
          </div>

          &lt;!&ndash; Or if this user 'IS' staff and im a superuser &ndash;&gt;
          <div v-else-if="content_obj.is_staff && user_obj.is_superuser" class="col-sm-9 mt-sm-3">
            <div id="user_super_set">
              <button type="button" class="btn btn-danger w-100" @click.prevent="staff_set('demote')">
                운영자 자격 박탈
              </button>
            </div>
          </div>

          &lt;!&ndash; Or if this user 'IS' staff but im staff too &ndash;&gt;
          <div v-else-if="content_obj.is_staff && !user_obj.is_superuser" class="col-sm-9 mt-sm-3">
            <div id="user_super_set">
              <button type="button" class="btn btn-secondary w-100">권한 없음</button>
            </div>
          </div>

        </div>-->

        <div v-if="user_obj.is_superuser || user_obj.is_staff">
          <button type="button" class="btn btn-outline-danger w-100 mb-sm-2 mb-md-3"
                  @click.prevent="user_delete">
            유저 삭제
          </button>
        </div>
        <div v-else-if="user_obj.info.access_role == 1 && content_obj.info.access_role == 2 && user_obj.info.organization == content_obj.info.organization"
              @click.prevent="user_delete">
          유저 삭제
        </div>

      </div>

      <div v-else>
        <button type="button" class="btn btn-primary w-100 mb-2 mb-md-3" @click.prevent="edit_my_info">
          내 정보 수정하기
        </button>
      </div>

    </div>
    <!--container-->
  </div>
</template>

<script>
  export default {
    name: "user_detail",
    data: () => ({
      content_obj: {
        id: 0,
        username: '',
        email: '',
        info: {
          access_role: 0,
          organization: 0,
          phone_num: ''
        }
      }
    }),
    mounted() {
      this.set_refresh()
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

      },
      set_refresh() {
        if (this.$route.params.user_id) {
          this.$store.state.pageOptions.loading = true
          axios.get(this.$store.state.endpoints.baseUrl + 'users/' + this.$route.params.user_id + '/')
            .then((response) => {
              // console.log('user response?', response.data.data)
              this.content_obj = response.data.data
              this.$store.state.pageOptions.loading = false
            })
            .catch((error) => {
              console.log(error)
              this.$store.state.pageOptions.loading = false
            })
        }
      },
      grade_set(option) {
        // let formData = new FormData()
        let formData = {
          info: {
            access_role: option
          }
        }
        if (confirm('유저등급을 변경하시겠습니까?')) {
          // formData.append('access', option)
          axios.patch(this.$store.state.endpoints.baseUrl + 'users/' + this.content_obj.id + '/', formData)
            .then(() => {
              this.set_refresh()
            })
            .catch((error) => {
              alert('등급변경 중 오류가 발생하였습니다.')
              console.log(error)
            })
        }
      },
      /*staff_set(option) {
        let formData = new FormData()
        if (option == 'promote') {
          if (confirm('이 유저를 운영자로 승급 시키시겠습니까?')) {
            formData.append('is_staff', '1')
            axios.patch(this.$store.state.endpoints.baseUrl + 'users/' + this.content_obj.id + '/', formData)
              .then(() => {
                this.set_refresh()
              })
              .catch((error) => {
                alert('승급 과정에서 오류가 발생하였습니다.')
                console.log(error)
              })
          }
        } else if (option == 'demote') {
          if (confirm('이 유저를 일반 유저로 강등 시키시겠습니까?')) {
            formData.append('is_staff', '0')
            axios.patch(this.$store.state.endpoints.baseUrl + 'users/' + this.content_obj.id + '/', formData)
              .then(() => {
                this.set_refresh()
              })
              .catch((error) => {
                alert('강등 과정에서 오류가 발생하였습니다.')
                console.log(error)
              })
          }
        }
      },*/
      /*user_stall(option) {
        let axios = this.$axios
        let this_url = 'users/'
        let formData = new FormData()
        if (option == 'stall') {
          formData.append('is_active', '0')
          axios.patch(this.$store.state.endpoints.baseUrl + this_url + this.content_obj.id + '/', formData)
            .then(() => {
              this.set_refresh()
            })
            .catch((error) => {
              console.log('User stall error = ', error)
            })
        } else if (option == 'restart') {
          formData.append('is_active', '1')
          axios.patch(this.$store.state.endpoints.baseUrl + this_url + this.content_obj.id + '/', formData)
            .then(() => {
              this.set_refresh()
            })
            .catch((error) => {
              console.log('User restart error = ', error)
            })
        }
      },*/
      user_delete() {
        if (confirm('이 유저를 정말 삭제하시겠습니까?')) {
          axios.delete(this.$store.state.endpoints.baseUrl + 'users/' + this.content_obj.id)
            .then(() => {
              alert('삭제되었습니다.')
              this.$router.push({
                name: 'user_list'
              })
            })
            .catch((error) => {
              alert('삭제 과정에서 오류가 발생하였습니다.')
              console.log(error)
            })
        }
      },
      edit_my_info() {
        if (confirm('정보수정 페이지로 이동할까요?')) {
          this.$router.push({
            name: 'my_info'
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
            'info': {
              'phone_num': ''
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

<style scoped>

</style>

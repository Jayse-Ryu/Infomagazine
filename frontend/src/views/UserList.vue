<template>
  <div class="main">
    <div class="text_navigation">
      <router-link to="/">홈</router-link>
      <span>></span>
      <router-link to="/users">유저 리스트</router-link>
    </div>

    <div v-if="user_obj.is_staff || user_obj.is_superuser">

      <div class="container">

        <!-- Search form -->
        <form class="container m-auto justify-content-between row p-0"
              v-on:submit.prevent="search(temp_option, temp_text)">

          <div class="w-100">
            <h4><span class="text-info">유저</span>들을 확인하세요</h4>
          </div>

          <router-link to="/users/create/" class="form-group btn btn-primary p-0 col-sm-12 col-md-1">
            <div class="create_btn_text">고객 생성</div>
          </router-link>

          <div class="form-group search_group text-center ml-auto p-0 col-sm-12 col-md-4">
            <select class="search_option" id="src_gbn" v-model="temp_option">
              <option value="0" selected>검색 옵션</option>
              <option value="1">이름</option>
              <option value="2">이메일</option>
            </select>
            <input type="text" class="search_text" v-model="temp_text" placeholder="검색">
            <button type="submit" class="search_btn">
              <img src="../assets/common/search.png"/>
            </button>
          </div>
        </form>
        <!-- /Search form -->


        <div v-if="window_width > 1000" class="list_area">
          <div class="list_header">
            <div class="list-group-item  d-inline-flex justify-content-between p-1 pt-2 pb-2 text-center"
                 style="border-radius: 0; border-bottom: 0; width:100%;">
              <!--<div class="col-1 p-0">번호</div>-->
              <div class="col-3 p-0text-center">이메일</div>
              <div class="col-3 p-0 text-center">이름</div>
              <div class="col-2 p-0 text-center">등급</div>
              <!--<div class="col-1 text-center">활성상태</div>-->
              <div class="col-2 p-0 board_centre">연락처</div>
              <div class="col-2 p-0 board_centre">생성일</div>
            </div>
          </div>
          <ul class="list_body list-group list-group-flush col-12 pr-0 text-center">

            <li v-if="content_obj.length === 0"
                class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1">
              <div class="col-12 text-center">데이터가 존재하지 않습니다.</div>
            </li>

            <li v-else class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1"
                v-for="content in content_obj">
              <!--<div class="col-1 p-0">{{ content.id }}</div>-->
              <div class="col-3 p-0 text-center">
                <router-link :to="'/users/detail/' + content.id">{{ content.email }}</router-link>
              </div>
              <div v-if="content.username" class="col-3 p-0 text-center">
                <router-link :to="'/users/detail/' + content.id">{{ content.username }}</router-link>
              </div>
              <div v-else class="col-3 p-0 text-center">
                <router-link :to="'/users/detail/' + content.id">이름없음</router-link>
              </div>

              <div v-if="user_obj.id == content.id" class="col-2 p-0 text-center">
                <div class="badge badge-dark">본인</div>
              </div>
              <div v-else-if="[0,1].includes(content.info.access_role)" class="col-2 p-0 text-center">
                <div class="badge badge-primary">마케터</div>
              </div>
              <div v-else-if="content.info.access_role == 3" class="col-2 p-0 text-center">
                <div class="badge badge-danger">미인증 마케터</div>
              </div>
              <div v-else-if="content.info.access_role == 2" class="col-2 p-0 text-center">
                <div class="badge badge-success">고객</div>
              </div>
              <div v-else class="col-2 p-0 text-center">
                <div class="badge badge-success">Nobody</div>
              </div>

              <div v-if="content.info.phone_num" class="col-2 p-0 board_centre">
                {{ content.info.phone_num }}
              </div>
              <div v-else class="col-2 p-0 board_centre">없음</div>

              <div v-if="content.created_date" class="col-2 p-0 board_centre">{{ (content.created_date).substring(0, 10)
                }}
              </div>
              <div v-else class="col-2 p-0 board_centre">정보 없음</div>
            </li>

          </ul>
        </div>

        <div v-else class="list_area">
          <div class="list_header">
            <div class="list-group-item  d-inline-flex justify-content-between p-1 pt-2 pb-2"
                 style="border-radius: 0; border-bottom: 0; width:100%;">
              <!--<div class="col-2 p-0">번호</div>-->
              <div class="col-3 p-0 text-center">계정</div>
              <div class="col-3 p-0 text-center">이름</div>
              <div class="col-4 p-0 board_centre">연락처</div>
            </div>
          </div>
          <ul class="list_body list-group list-group-flush col-12 pr-0">
            <li v-if="content_obj.length === 0"
                class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1">
              <div class="col-12 text-center">데이터가 존재하지 않습니다.</div>
            </li>
            <li v-else class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1"
                v-for="content in content_obj">
              <!--<div class="col-2 p-0">{{ content.user }}</div>-->
              <div class="col-3 p-0 text-center">
                <router-link :to="'/users/detail/' + content.id">{{ content.email }}</router-link>
              </div>

              <div v-if="content.username" class="col-3 p-0 text-center">
                <router-link :to="'/users/detail/' + content.id">{{ content.username }}</router-link>
              </div>
              <div v-else class="col-3 p-0 text-center">
                <router-link :to="'/users/detail/' + content.id">이름없음</router-link>
              </div>

              <div v-if="content.info.phone_num" class="col-4 p-0 board_centre">{{ content.info.phone_num }}</div>
              <div v-else class="col-4 p-0 board_centre">없음</div>
            </li>
          </ul>
        </div>

      </div>
      <!-- Container end -->
    </div>

    <!-- If no one try to access to this list -->
    <div v-else>
      <div class="m-auto text-center pt-3">권한이 없습니다.</div>
    </div>

    <paginate class="pagination"
              v-model="page_current"
              :page-count="page_max"
              :page-range="10"
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

  </div>
</template>

<script>
  export default {
    name: "user_list",
    data: () => ({
      // Get width
      window_width: window.innerWidth,
      // Page = options, contents
      page_current: 1,
      page_max: 0,
      page_chunk: 10,
      content_obj: [],
      temp_option: 0,
      temp_text: '',
      search_option: 0,
      search_text: '',
    }),
    mounted() {
      // Window width calculator
      let that = this
      that.$nextTick(function () {
        window.addEventListener('resize', function (e) {
          that.window_width = window.innerWidth
        })
      })

      // Init other pages options
      this.page_init()

      // Get organization list
      this.pagination(this.page_current)
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

        // Check Vuex store for this page values
        this.page_current = option.user.page
        this.temp_option = option.user.option
        this.temp_text = option.user.text
        this.search_option = option.user.option
        this.search_text = option.user.text

        // Follow inited search options
        let offset = (this.$store.state.pageOptions.user.page - 1) * this.page_chunk
        this.temp_option = this.search_option
      },
      pagination(pageNum) {
        // when page is first, max ~ max-(chunk*current)+1
        // when page is max, max-(chunk*(current-1)) ~ 1
        // when page is middle, max-(chunk*(current-1)) ~ max-(chunk*current)+1
        let offset = (pageNum - 1) * this.page_chunk
        this.calling_all_unit(offset)
      },
      search(option, text) {
        if (option !== 0 && text !== '') {
          this.page_current = 1
          this.search_option = this.temp_option
          this.search_text = text
          this.calling_all_unit()
        } else {
          this.search_option = 0
          this.search_text = ''
          this.calling_all_unit()
        }
      },
      calling_all_unit(offset) {
        // Calling landings with new values
        // let auth_filter = ''
        let search_param = ''
        let pagination = ''

        // (For Pagination check)
        // axios.get(this.$store.state.endpoints.baseUrl + 'landing/' + '?offset=' + offset + '&' + this.search_option + '=' + this.search_text)
        //   .then((response) => {
        //     // Calculation for page_max
        //     if (response.data.count % this.page_chunk === 0) {
        //       this.page_max = Math.floor(response.data.count / this.page_chunk)
        //     } else {
        //       this.page_max = Math.floor(response.data.count / this.page_chunk) + 1
        //     }
        //     this.content_obj = response.data.results
        //   })

        // const config = {
        //   headers: {
        //     'Content-Type': 'application/json'
        //   }
        // }

        if (offset) {
          pagination = '?offset=' + offset
        }
        // Set search option
        if (this.search_option == 1) {
          if (pagination) {
            search_param = '&name=' + this.search_text
          } else {
            search_param = '?name=' + this.search_text
          }
        }

        // if (this.user_obj.is_staff || this.user_obj.is_superuser) {
        //   console.log('Staff user - Get All')
        //   auth_filter = '?true'
        // } else if (this.user_obj.info.access_role == '0' || this.user_obj.info.access_role == '1') {
        //   console.log('Marketer user - Get only Org')
        //   auth_filter = '?organization=' + this.user_obj.info.organization
        // } else if (this.user_obj.info.access_role == '2') {
        //   console.log('load about com - Get only Com')
        //   auth_filter = '?company=' + this.user_obj.info.company
        // }

        this.$store.state.pageOptions.loading = true
        axios.get(this.$store.state.endpoints.baseUrl + 'users/' + pagination + search_param)
          .then((response) => {
            this.$store.state.pageOptions.loading = false
            this.content_obj = response.data.data.results
            // Calculation for page_max
            if (response.data.data.count % this.page_chunk === 0) {
              console.log(response.data.data.count)
              this.page_max = Math.floor(response.data.data.count / this.page_chunk)
            } else {
              this.page_max = Math.floor(response.data.data.count / this.page_chunk) + 1
            }
          })
          .catch((error) => {
            this.$store.state.pageOptions.loading = false
            console.log('Get landing crashed', error)
          })
      }
    },
    destroyed() {
      // Save values in the store
      this.$store.state.pageOptions.user.page = this.page_current
      this.$store.state.pageOptions.user.option = this.search_option
      this.$store.state.pageOptions.user.text = this.search_text
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
        }

        return user_json
      }
    }
  }
</script>

<style scoped lang="scss">

</style>

<template>
  <div class="main">
    <div class="text_navigation">
      <router-link to="/">홈</router-link>
      <span>></span>
      <router-link to="/landing">랜딩 리스트</router-link>
    </div>

    <!-- Search form -->
    <form class="container m-auto justify-content-between row"
          v-on:submit.prevent="search(temp_option, temp_text)">

      <div class="w-100">
        <h4><span class="text-info">랜딩페이지</span>를 확인하세요</h4>
      </div>

      <!-- Create button -->
      <router-link to="/landing/create/"
                   v-if="[0, 1].includes(user_obj.access_role) || user_obj.is_staff || user_obj.is_superuser"
                   class="form-group btn btn-primary p-0 col-sm-12 col-md-1">
        <div class="create_btn_text">생성</div>
      </router-link>

      <div class="form-group search_group ml-auto text-center p-0 col-sm-12 col-md-4">

        <select v-if="[0, 1].includes(user_obj.access_role) || user_obj.is_staff || user_obj.is_superuser"
                class="search_option" id="src_gbn" v-model="temp_option">
          <option value="0" selected>검색 옵션</option>
          <option value="1">랜딩 이름</option>
          <option value="2">업체</option>
          <option value="3">마케터</option>
        </select>

        <select v-else-if="user_obj.access_role == 2"
                class="search_option" id="src_gbn" v-model="temp_option">
          <option value="0" selected>검색 옵션</option>
          <option value="1">랜딩 이름</option>
        </select>

        <input type="text" class="search_text" v-model="temp_text" placeholder="검색">
        <button type="submit" class="search_btn">
          <img src="../assets/common/search.png"/>
        </button>
      </div>
    </form>
    <!-- /Search form -->


    <!-- Landing List -->
    <div class="container">

      <!-- List with Big width -->
      <div v-if="window_width > 1000" class="list_area">

        <!-- List table header -->
        <div class="list_header">
          <div class="list-group-item text-center d-inline-flex justify-content-between p-1 pt-2 pb-2 text-center"
               style="border-radius: 0; border-bottom: 0; width:100%;">
            <div class="col-3 p-0">업체</div>
            <div class="col-4 p-0">페이지</div>
            <div class="col-3 p-0">마케터</div>
            <div class="col-1 p-0 board_centre">조회수</div>
            <div class="col-1 p-0 board_centre">DB</div>
          </div>
        </div>
        <!-- /List table header -->

        <!-- List table body -->
        <ul class="list_body text-center list-group list-group-flush col-12 pr-0 text-center">

          <li v-if="content_obj.length === 0"
              class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1">
            <div class="col-12 text-center">데이터가 존재하지 않습니다.</div>
          </li>

          <li v-else v-for="content in content_obj"
              class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1">
            <div class="col-3 p-0 col-sm-3">{{ content.LandingInfo.landing.company_name }}</div>
            <div v-if="[0, 1].includes(user_obj.access_role) || user_obj.is_staff || user_obj.is_superuser"
                 class="col-3 p-0 col-sm-4">
              <router-link :to="'/landing/detail/' + content.LandingNum">
                {{ content.LandingInfo.landing.name }}
              </router-link>
            </div>
            <div v-else class="col-3 p-0 col-sm-4">
              <router-link :to="'/db/detail/' + content.LandingNum">
                {{ content.LandingInfo.landing.name }}
              </router-link>
            </div>
            <div class="col-3 p-0">{{ content.LandingInfo.landing.manager_name }}</div>
            <div class="col-1 p-0 board_centre">{{ content.LandingInfo.landing.views }}</div>
            <div class="col-1 p-0 board_centre">
              <router-link :to="'/db/detail/' + content.LandingNum">
                {{ content.LandingInfo.landing.collection_amount }}
              </router-link>
            </div>
          </li>
        </ul>
        <!-- /List table body -->
      </div>
      <!-- /List with Big width -->

      <!-- List with Small width -->
      <div v-else class="list_area">

        <!-- List table header -->
        <div class="list_header">
          <div class="list-group-item text-center d-inline-flex justify-content-between p-1 pt-2 pb-2"
               style="border-radius: 0; border-bottom: 0; width:100%;">
            <div class="col-2 p-0">업체</div>
            <div class="col-5 p-0">페이지</div>
            <div class="col-3 p-0">마케터</div>
            <div class="col-2 p-0">DB</div>
          </div>
        </div>
        <!-- /List table header -->

        <!-- List table body -->
        <ul class="list_body text-center list-group list-group-flush col-12 pr-0">

          <li v-if="content_obj.length === 0"
              class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1">
            <div class="col-12 p-0 text-center">데이터가 존재하지 않습니다.</div>
          </li>

          <li v-else class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1"
              v-for="content in content_obj">
            <div class="col-2 p-0">{{ content.LandingInfo.landing.company_name }}</div>
            <div v-if="[0, 1].includes(user_obj.access_role) || user_obj.is_staff || user_obj.is_superuser"
                 class="col-5 p-0">
              <router-link :to="'/landing/detail/' + content.LandingNum">
                {{ content.LandingInfo.landing.name }}
              </router-link>
            </div>
            <div v-else class="col-5 p-0">
              <router-link :to="'/landing/detail/' + content.LandingNum">
                {{ content.LandingInfo.landing.name }}
              </router-link>
            </div>
            <div class="col-3 p-0">{{ content.LandingInfo.landing.manager_name }}</div>
            <div class="col-2 p-0">
              <router-link :to="'/db/detail/' + content.LandingNum">
                {{ content.LandingInfo.landing.collection_amount }}
              </router-link>
            </div>
          </li>

        </ul>
        <!-- /List table body -->
      </div>
      <!-- /List with Small width -->

    </div>

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

  </div>
</template>

<script>
  export default {
    name: "landing_list",
    data: () => ({
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
    methods: {
      page_init() {
        let option = this.$store.state.pageOptions

        // Init other pages options
        option.company.page = 1
        option.company.option = 0
        option.company.text = ''
        option.user.page = 1
        option.user.option = 0
        option.user.text = ''
        option.organization.page = 1
        option.organization.option = 0
        option.organization.text = ''

        // Check Vuex store for this page values
        this.page_current = option.landing.page
        this.temp_option = option.landing.option
        this.temp_text = option.landing.text
        this.search_option = option.landing.option
        this.search_text = option.landing.text

        // Follow inited search options
        let offset = (this.$store.state.pageOptions.landing.page - 1) * this.page_chunk
        this.temp_option = this.search_option
      },
      pagination(pageNum) {
        // when page is first, /// max ~ max-(chunk*current)+1
        // when page is max, /// max-(chunk*(current-1)) ~ 1
        // when page is middle, /// max-(chunk*(current-1)) ~ max-(chunk*current)+1
        let offset = (pageNum - 1) * this.page_chunk
        this.calling_all_unit(offset)
      },
      search(option, text) {
        // option, text from data temp_x
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
        let auth_filter = ''
        let search_param = ''

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

        if (this.search_option == 1) {
          search_param = '&name=' + this.search_text
        } else if (this.search_option == 2) {
          search_param = '&com_name=' + this.search_text
        } else if (this.search_option == 3) {
          search_param = '&marketer=' + this.search_text
        }

        if (this.user_obj.is_staff || this.user_obj.is_superuser) {
          console.log('Staff user - Get All')
          auth_filter = '?true'
        } else if (this.user_obj.access_role == '0' || this.user_obj.access_role == '1') {
          console.log('Marketer user - Get only Org')
          auth_filter = '?organization=' + this.user_obj.organization
        } else if (this.user_obj.access_role == '2') {
          console.log('load about com - Get only Com')
          auth_filter = '?company=' + this.user_obj.company
        }

        this.$store.state.pageOptions.loading = true
        axios.get(this.$store.state.endpoints.baseUrl + 'landing/list/' + auth_filter + search_param)
          .then((response) => {
            this.$store.state.pageOptions.loading = false
            console.log('get landing response', response)
            this.content_obj = response.data.results
          })
          .catch((error) => {
            this.$store.state.pageOptions.loading = false
            console.log('Get landing crashed', error)
          })

      }
    },
    mounted() {
      // Init other pages options
      this.page_init()

      // Window width calculator
      let that = this
      that.$nextTick(function () {
        window.addEventListener('resize', function (e) {
          that.window_width = window.innerWidth
        })
      })

      // Get landing list
      this.calling_all_unit()
    },
    destroyed() {
      // Save page option values in the store
      this.$store.state.pageOptions.landing.page = this.page_current
      this.$store.state.pageOptions.landing.option = this.search_option
      this.$store.state.pageOptions.landing.text = this.search_text
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

<style scoped>

</style>

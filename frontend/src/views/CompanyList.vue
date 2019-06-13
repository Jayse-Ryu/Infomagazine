<template>
  <div class="main">
    <div class="text_navigation">
      <router-link to="/">홈</router-link>
      <span>></span>
      <router-link to="/company">업체 리스트</router-link>
    </div>

    <div v-if="user_obj.is_staff || user_obj.is_superuser || [0,1].includes(user_obj.access_role)">
      <form class="container m-auto justify-content-between row"
            v-on:submit.prevent="search(temp_option, temp_text)">

        <div class="w-100">
          <h4><span class="text-info">고객</span> 회사들을 확인하세요</h4>
        </div>

        <router-link to="/company/create/" class="form-group btn btn-primary p-0 col-sm-12 col-md-1">
          <div class="create_btn_text">생성</div>
        </router-link>

        <div class="form-group search_group ml-auto text-center p-0 col-sm-12 col-md-4">
          <select class="search_option" id="src_gbn" v-model="temp_option">
            <option value="0" selected>검색 옵션</option>
            <option value="1">업체</option>
            <option value="2">담당조직</option>
          </select>
          <input type="text" class="search_text" v-model="temp_text" placeholder="검색">
          <button type="submit" class="search_btn">
            <img src="../assets/common/search.png"/>
          </button>
        </div>
      </form>

      <div class="container">

        <div v-if="window_width > 1000" class="list_area">
          <div class="list_header">
            <div class="list-group-item  d-inline-flex justify-content-between p-1 pt-2 pb-2 text-center"
                 style="border-radius: 0; border-bottom: 0; width:100%;">
              <div class="col-1 p-0">번호</div>
              <div class="col-3 p-0">업체</div>
              <div class="col-3 p-0">상호명</div>
              <div class="col-2 p-0">연락처</div>
              <div class="col-3 p-0 board_centre">생성일</div>
            </div>
          </div>
          <ul class="list_body list-group list-group-flush col-12 pr-0 text-center">
            <li v-if="content_obj.length === 0"
                class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1">
              <div class="col-12 p-0 text-center">데이터가 존재하지 않습니다.</div>
            </li>
            <li v-else class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1"
                v-for="content in content_obj.slice().reverse()">
              <div class="col-1 p-0">{{ content.id }}</div>
              <div class="col-3 p-0">
                <router-link :to="'/company/detail/' + content.id">{{ content.corp_name }}</router-link>
              </div>
              <div class="col-3 p-0">
                <router-link :to="'/company/detail/' + content.id">{{ content.corp_sub_name }}</router-link>
              </div>
              <div v-if="content.corp_tel_num" class="col-2 p-0">{{ content.corp_tel_num }}</div>
              <div v-else-if="content.corp_email" class="col-2 p-0">{{ content.corp_email }}</div>
              <div v-else class="col-2 p-0">없음</div>
              <div class="col-3 p-0 board_centre">{{ (content.created_date).substring(0, 10) }}</div>
            </li>
          </ul>
        </div>

        <div v-else class="list_area">
          <div class="list_header">
            <div class="list-group-item text-center d-inline-flex justify-content-between p-1 pt-2 pb-2"
                 style="border-radius: 0; border-bottom: 0; width:100%;">
              <div class="col-2 p-0">번호</div>
              <div class="col-3 p-0">업체</div>
              <div class="col-4 p-0">연락처</div>
              <div class="col-3 p-0 board_centre">생성일</div>
            </div>
          </div>
          <ul class="list_body text-center list-group list-group-flush col-12 pr-0">
            <li v-if="content_obj.length === 0"
                class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1">
              <div class="col-12 p-0 text-center">데이터가 존재하지 않습니다.</div>
            </li>
            <li v-else class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1"
                v-for="content in content_obj.slice().reverse()">
              <div class="col-2 p-0">{{ content.id }}</div>
              <div class="col-3 p-0">
                <router-link :to="'/company/detail/' + content.id">{{ content.corp_name }}</router-link>
              </div>
              <div v-if="content.corp_tel_num" class="col-4 p-0">{{ content.corp_tel_num }}</div>
              <div v-else-if="content.corp_email" class="col-4 p-0">{{ content.corp_email }}</div>
              <div v-else class="col-4 p-0">없음</div>
              <div class="col-3 p-0 board_centre">{{ (content.created_date).substring(0, 10) }}</div>
            </li>
          </ul>
        </div>

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

    <!-- If no one try to access to this list -->
    <div v-else>
      <div class="m-auto text-center pt-3">권한이 없습니다.</div>
    </div>

  </div>
</template>

<script>
  export default {
    name: "company_list",
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
        option.landing.page = 1
        option.landing.option = 0
        option.landing.text = ''
        option.user.page = 1
        option.user.option = 0
        option.user.text = ''
        option.organization.page = 1
        option.organization.option = 0
        option.organization.text = ''

        // Check Vuex store for this page values
        this.page_current = option.company.page
        this.temp_option = option.company.option
        this.temp_text = option.company.text
        this.search_option = option.company.option
        this.search_text = option.company.text

        // Follow inited search options
        let offset = (this.$store.state.pageOptions.company.page - 1) * this.page_chunk
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
        } else if (option == 0 && text !== '') {
          alert('검색 옵션을 선택하세요!')
          document.getElementById('src_gbn').focus()
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
        }

        // if (this.user_obj.is_staff || this.user_obj.is_superuser) {
        //   console.log('Staff user - Get All')
        //   auth_filter = '?true'
        // } else if (this.user_obj.access_role == '0' || this.user_obj.access_role == '1') {
        //   console.log('Marketer user - Get only Org')
        //   auth_filter = '?organization=' + this.user_obj.organization
        // } else if (this.user_obj.access_role == '2') {
        //   console.log('load about com - Get only Com')
        //   auth_filter = '?company=' + this.user_obj.company
        // }

        this.$store.state.pageOptions.loading = true
        axios.get(this.$store.state.endpoints.baseUrl + 'companies/' + search_param)
          .then((response) => {
            this.$store.state.pageOptions.loading = false
            this.content_obj = response.data.data.results
          })
          .catch((error) => {
            this.$store.state.pageOptions.loading = false
            console.log('Get landing crashed', error)
          })
      }
    },
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
      this.calling_all_unit()
    },
    destroyed() {
      // Save values in the store
      this.$store.state.pageOptions.company.page = this.page_current
      this.$store.state.pageOptions.company.option = this.search_option
      this.$store.state.pageOptions.company.text = this.search_text
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

<style lang="scss">

</style>

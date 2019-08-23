<template>
  <div class="main" style="max-width: 2560px !important;">
    <div class="text_navigation" style="margin: 1% 0 15px 15px !important;">
      <router-link to="/">홈</router-link>
      <span>></span>
      <router-link to="/landing">랜딩 리스트</router-link>
      <span>></span>
      <router-link to="/db/detail">DB 정보</router-link>
    </div>

    <div class="whole_wrap">
      <!-- Selected page -->
      <section class="section">
        <div class="landing_info">
          <h5>선택된 랜딩페이지</h5>
          <div v-if="window_width > 1000" class="list_area">
            <div class="list_header">
              <div class="list-group-item text-center d-inline-flex justify-content-between p-1 pt-2 pb-2 text-center"
                   style="border-radius: 0; width:100%;">
                <div class="col-3 p-0">업체명</div>
                <div class="col-3 p-0">상호명</div>
                <div class="col-4 p-0">페이지</div>
                <div class="col-1 p-0 board_centre">조회수</div>
                <div class="col-1 p-0 board_centre">DB</div>
              </div>
            </div>
            <ul class="list_body text-center list-group list-group-flush col-12 pr-0 text-center">
              <li
                class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1 font-weight-bold border-0">
                <div class="col-3 p-0 col-sm-3">{{ landing_obj.company_name }}</div>
                <div class="col-3 p-0 col-sm-3">{{ landing_obj.company_sub_name }}</div>
                <div class="col-4 p-0 col-sm-4">{{ landing_obj.landing_info.landing.name }}</div>
                <!--<div class="col-3 p-0">{{ manager_name }}</div>-->
                <div class="col-1 p-0 board_centre" v-if="landing_obj.landing_info.views">
                  {{ landing_obj.landing_info.views }}
                </div>
                <div class="col-1 p-0 board_centre" v-else>0</div>
                <div class="col-1 p-0 board_centre" v-if="landing_obj.landing_info.db">
                  {{ landing_obj.landing_info.db }}
                </div>
                <div class="col-1 p-0 board_centre" v-else>0</div>
              </li>
            </ul>
          </div>

          <div v-else class="list_area">
            <div class="list_header">
              <div class="list-group-item text-center d-inline-flex justify-content-between p-1 pt-2 pb-2"
                   style="border-radius: 0; border-bottom: 0; width:100%;">
                <div class="col-3 p-0">업체</div>
                <div class="col-6 p-0">페이지</div>
                <div class="col-3 p-0">DB</div>
              </div>
            </div>
            <ul class="list_body text-center list-group list-group-flush col-12 pr-0">
              <li class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1 border-0">
                <div class="col-3 p-0">{{ landing_obj.company_id }}</div>
                <div class="col-6 p-0">{{ landing_obj.landing_info.landing.name }}</div>
                <div v-if="landing_obj.landing_info.db" class="col-3 p-0">
                  {{ landing_obj.landing_info.db }}
                </div>
                <div v-else class="col-3 p-0">0</div>
              </li>
            </ul>
          </div>

          <div>
            <router-link :to="'/landing/detail/' + landing_id">
              <button type="button" class="btn btn-info w-100 p-1 mt-3">랜딩정보로 돌아가기</button>
            </router-link>
          </div>

        </div>
      </section>
      <!-- /Selected page -->

      <!--<hr>

      <section class="section section_box">
        <h5>DB 개요</h5>

        <div class="list_area">
          <div class="list_header">
            <div class="list-group-item text-center d-inline-flex justify-content-between p-1 pt-2 pb-2 text-center"
                 style="border-radius: 0; width:100%;">
              <div class="col-6 p-0">디바이스 종류</div>
              <div class="col-6 p-0">IP 종류</div>
            </div>
          </div>
          <ul class="text-center list-group list-group-flush text-center">
            <li class="list-group-item list-group-item-action d-inline-flex justify-content-around p-1">
              <div class="col-6 p-0">{{ db_inspect.agent }} 가지</div>
              <div class="col-6 p-0">{{ db_inspect.ip }} 가지</div>
            </li>
          </ul>
        </div>

      </section>-->

      <hr>

      <section class="section section_box">
        <h5>DB 필터</h5>
        <div class="row">
          <div class="col-md-4">
            <datepicker class="datepicker w-100 form-control p-0"
                        placeholder="시작 날짜"
                        format="yyyy-MM-dd"
                        :highlighted="range"
                        :disabledDates="start_disabled"
                        :language="language"
                        v-model="start_time">
            </datepicker>
          </div>
          <div class="col-md-4">
            <datepicker class="datepicker w-100 form-control p-0"
                        placeholder="종료 날짜"
                        format="yyyy-MM-dd"
                        :highlighted="range"
                        :disabledDates="finish_disabled"
                        :language="language"
                        v-model="finish_time">
            </datepicker>
          </div>
          <div class="col-md-2">
            <button type="button" class="btn btn-info w-100 mb-1" @click="date_clear()">초기화</button>
          </div>
          <div class="col-md-2">
            <vue-excel type="button" class="btn btn-outline-success w-100" :data="db_vals">
              엑셀저장
            </vue-excel>
          </div>
        </div>
        <div class="row mt-3">
          <div class="col-3">
            <button type="button" class="btn btn-secondary w-100 p-0" @click="short_cut('recent3')">
              최근3일
            </button>
          </div>
          <div class="col-3">
            <button type="button" class="btn btn-secondary w-100 p-0" @click="short_cut('recent2')">
              최근2일
            </button>
          </div>
          <div class="col-3">
            <button type="button" class="btn btn-secondary w-100 p-0" @click="short_cut('yesterday')">
              어제
            </button>
          </div>
          <div class="col-3">
            <button type="button" class="btn btn-secondary w-100 p-0" @click="short_cut('today')">
              오늘
            </button>
          </div>
        </div>
      </section>

      <hr>

      <section class="section section_box">
        <h5>DB 리스트</h5>

        <div class="list_area db_list_wrap">

          <div class="list_header db_list_header">
            <div
              class="list-group-item text-center d-inline-flex justify-content-around p-1 pt-2 pb-2 text-center border-bottom-0"
              style="border-radius: 0; width:100%;">
              <div v-for="key in db_keys" :style="db_width"
                   class="p-0 d-flex align-items-center justify-content-center">{{ key }}
              </div>
              <div v-if="[0, 1].includes(user_obj.access_role) || user_obj.is_staff || user_obj.is_superuser"
                   :style="db_width" class="p-0 d-flex align-items-center justify-content-center">
                삭제
              </div>
            </div>
          </div>

          <ul class="db_list_body text-center list-group list-group-flush text-center">
            <li class="list-group-item list-group-item-action d-inline-flex justify-content-around p-1"
                v-if="db_vals.length == 0">
              <div class="p-0">데이터가 없습니다.</div>
            </li>
            <li class="list-group-item list-group-item-action d-inline-flex justify-content-around p-1"
                v-else v-for="item in db_vals">
              <div class="p-2 text-center" v-for="val in item" :style="db_width">
                <div class="d-flex align-items-center justify-content-center" style="width: 100%; height: 100%;">
                  {{ val }}
                </div>
              </div>
              <div class="p-2 text-center d-flex align-items-center justify-content-center" :style="db_width"
                   v-if="[0, 1].includes(user_obj.access_role) || user_obj.is_staff || user_obj.is_superuser">
                <button type="button" class="btn btn-sm btn-outline-danger w-100 p-1" @click="db_delete(item.ID)">
                  삭제
                </button>
              </div>
            </li>
          </ul>

        </div>

      </section>

      <!--      <div class="alert-warning">{{ db_keys }}</div>-->
      <!--<div class="alert-success">{{ db_vals }}</div>-->

    </div>
    <!-- /Container -->

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
,
<script>

  import * as lang from "vuejs-datepicker/src/locale"

  export default {
    name: "db_detail",
    data: () => ({
      window_width: window.innerWidth,
      page_current: 1,
      page_max: 0,
      page_chunk: 10,
      landing_id: '0',
      landing_obj: {
        landing_info: {
          landing: {}
        }
      },
      manager_name: '없음',
      db_list: [],
      db_keys: [],
      db_vals: [],
      db_inspect: {},
      start_time: '',
      finish_time: '',
      language: lang.ko
    }),
    mounted() {
      // Window width calculator
      let that = this
      that.$nextTick(function () {
        window.addEventListener('resize', function (e) {
          that.window_width = window.innerWidth
        })
      })
      this.get_db_list()
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
      pagination(pageNum) {
        // when page is first, max ~ max-(chunk*current)+1
        // when page is max, max-(chunk*(current-1)) ~ 1
        // when page is middle, max-(chunk*(current-1)) ~ max-(chunk*current)+1
        let offset = (pageNum - 1) * this.page_chunk
        this.get_db_list(offset)
      },
      get_db_list(offset) {

        let pagination = ''

        if (offset) {
          pagination = '?offset=' + offset
        }

        this.$store.state.pageOptions.loading = true
        this.landing_id = this.$route.params.landing_id
        axios.get(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.landing_id + '/')
          .then((response) => {
            this.landing_obj = response.data.data
            this.add_landing_info()
            return axios.get(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.landing_id + '/landing_dbs/' + pagination)
          })
          .catch((error) => {
            this.$store.state.pageOptions.loading = false
            console.log('get landing', error)
          })
          .then((response) => {
            // console.log('db gathering', response.data.data.results)
            this.landing_obj.landing_info.db = response.data.data.count
            this.db_list = response.data.data.results
            if (response.data.data.count % this.page_chunk === 0) {
              console.log(response.data.data.count)
              this.page_max = Math.floor(response.data.data.count / this.page_chunk)
            } else {
              this.page_max = Math.floor(response.data.data.count / this.page_chunk) + 1
            }
            // Call get resources after data loaded
            this.get_resources_key()
            this.db_analytics()
            if (this.landing_obj.landing_info.landing.manager > -1) {
              return axios.get(this.$store.state.endpoints.baseUrl + 'users/' + this.landing_obj.landing_info.landing.manager + '/')
            } else {
              this.manager_name = '매니저 없음'
            }
            this.$store.state.pageOptions.loading = false
          })
          .then((response) => {
            // console.log('get user res ', response)
            // this.manager_name = response.data.data.username
            this.$store.state.pageOptions.loading = false
          })
          .catch((error) => {
            this.$store.state.pageOptions.loading = false
            console.log('get db', error)
          })

      },
      add_landing_info() {
        axios.get(this.$store.state.endpoints.baseUrl + 'companies/' + this.landing_obj.company_id + '/')
          .then((response) => {
            this.landing_obj['company_name'] = response.data.data.corp_name
            this.landing_obj['company_sub_name'] = response.data.data.corp_sub_name
            let temp = JSON.stringify(this.landing_obj)
            this.landing_obj = JSON.parse(temp)
          })
          .catch((error) => {
            console.log('get comp', error)
          })
      },
      get_resources_key() {
        this.db_keys = ['ID']
        // this.db_vals = []

        // Get only obje keys for pretty list
        for (let index in this.db_list) {

          // Extract db object by index
          if (this.db_list.hasOwnProperty(index)) {
            // Set db keys from one db object
            for (let key in this.db_list[index]) {
              if (key === 'db') {
                for (let inner in this.db_list[index][key]) {
                  if (this.db_list[index][key].hasOwnProperty(inner)) {
                    if (!this.db_keys.includes(inner)) {
                      this.db_keys.push(inner)
                    }
                  }
                }
              }
            }
          }
          // ext
        }
        // // Push url and date fields to backward
        // this.db_keys.splice(this.db_keys.indexOf('url'), 1)
        // this.db_keys.push('url')
        if (this.db_keys.indexOf('신청일') > -1) {
          this.db_keys.splice(this.db_keys.indexOf('신청일'), 1)
          this.db_keys.push('신청일')
        } else {
          this.db_keys.push('신청일')
        }
        if (this.db_keys.indexOf('모델타입') > -1) {
          this.db_keys.splice(this.db_keys.indexOf('모델타입'), 1)
          this.db_keys.push('모델타입')
        } else {
          this.db_keys.push('모델타입')
        }
        if (this.db_keys.indexOf('브라우저') > -1) {
          this.db_keys.splice(this.db_keys.indexOf('브라우저'), 1)
          this.db_keys.push('브라우저')
        } else {
          this.db_keys.push('브라우저')
        }
        if (this.db_keys.indexOf('모델제조사') > -1) {
          this.db_keys.splice(this.db_keys.indexOf('모델제조사'), 1)
          this.db_keys.push('모델제조사')
        } else {
          this.db_keys.push('모델제조사')
        }
        if (this.db_keys.indexOf('모델명') > -1) {
          this.db_keys.splice(this.db_keys.indexOf('모델명'), 1)
          this.db_keys.push('모델명')
        } else {
          this.db_keys.push('모델명')
        }
        if (this.db_keys.indexOf('OS') > -1) {
          this.db_keys.splice(this.db_keys.indexOf('OS'), 1)
          this.db_keys.push('OS')
        } else {
          this.db_keys.push('OS')
        }

        this.get_resources_val()
      },
      get_resources_val() {
        let val_obj = []
        this.db_vals = []

        // Set values by keys
        for (let index in this.db_list) {
          if (this.db_list.hasOwnProperty(index)) {
            // value set by all of keys
            let month_array = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
            let date_obj = ''
            val_obj.push({})

            for (let key in this.db_list[index]) {
              if (key === 'db') {
                // Inspect by key name
                for (let i = 0; i < this.db_keys.length; i++) {
                  // If this object has this key
                  if (this.db_list[index][key].hasOwnProperty(this.db_keys[i])) {
                    // If key is created date
                    val_obj[index][this.db_keys[i]] = this.db_list[index][key][this.db_keys[i]]
                  } else if (this.db_keys[i] === 'ID') {
                    val_obj[index][this.db_keys[i]] = this.db_list[index]['id']
                  } else if (this.db_keys[i] === '신청일') {
                    date_obj = ''
                    // Epoch time string length must be 13
                    if (this.db_list[index]['registered_date'].length == 10) {
                      date_obj = new Date(this.db_list[index]['registered_date'] * 1000)
                    } else {
                      let double = Math.pow(10, this.db_list[index]['registered_date'].length - 10)
                      date_obj = new Date(this.db_list[index]['registered_date'] * (1000 / double))
                    }
                    // Make date string
                    let date_str = date_obj.getFullYear() + '-' + month_array[date_obj.getMonth()] + '-' + date_obj.getDate()

                    val_obj[index][this.db_keys[i]] = date_str
                    //Date val done
                  } else if (this.db_keys[i] === '모델타입') {
                    val_obj[index][this.db_keys[i]] = this.db_list[index]['user_agent']['viewer_type']
                  } else if (this.db_keys[i] === '브라우저') {
                    val_obj[index][this.db_keys[i]] = this.db_list[index]['user_agent']['browser_family']
                  } else if (this.db_keys[i] === '모델제조사') {
                    val_obj[index][this.db_keys[i]] = this.db_list[index]['user_agent']['device_brand']
                  } else if (this.db_keys[i] === '모델명') {
                    val_obj[index][this.db_keys[i]] = this.db_list[index]['user_agent']['device_model']
                  } else if (this.db_keys[i] === 'OS') {
                    val_obj[index][this.db_keys[i]] = this.db_list[index]['user_agent']['os_family']
                  } else {
                    // If db[index] dont have this key[i]
                    val_obj[index][this.db_keys[i]] = (' ')
                  }
                }
              }
            }// for

          }
        }

        // If calendar works, Time comparison and push data or not
        if (this.start_time != '' && this.finish_time != '') {
          let length = val_obj.length
          while (length--) {
            for (let i in val_obj) {
              let from_t = new Date(this.start_time).setHours(0, 0, 0, 0)
              let to_t = new Date(this.finish_time).setHours(0, 0, 0, 0)
              let value_t = new Date(val_obj[i]['신청일']).setHours(0, 0, 0, 0)

              if (!(from_t <= value_t && value_t <= to_t)) {
                val_obj.splice(i, 1)
              }

            }
          }

        }
        // Date filter

        this.db_vals = (val_obj)
        // set val
      },
      date_clear() {
        this.start_time = ''
        this.finish_time = ''
        this.get_resources_key()
      },
      short_cut(option) {
        if (option == 'recent3') {
          let from = new Date(new Date().setDate(new Date().getDate() - 3)).setHours(0, 0, 0, 0)
          let to = new Date().setHours(0, 0, 0, 0)
          this.start_time = new Date(from)
          this.finish_time = new Date(to)
          this.get_resources_key()
        } else if (option == 'recent2') {
          let from = new Date(new Date().setDate(new Date().getDate() - 2)).setHours(0, 0, 0, 0)
          let to = new Date().setHours(0, 0, 0, 0)
          this.start_time = new Date(from)
          this.finish_time = new Date(to)
          this.get_resources_key()
        } else if (option == 'yesterday') {
          let from = new Date(new Date().setDate(new Date().getDate() - 1)).setHours(0, 0, 0, 0)
          let to = new Date(new Date().setDate(new Date().getDate() - 1)).setHours(0, 0, 0, 0)
          this.start_time = new Date(from)
          this.finish_time = new Date(to)
          this.get_resources_key()
        } else if (option == 'today') {
          let from = new Date().setHours(0, 0, 0, 0)
          let to = new Date().setHours(0, 0, 0, 0)
          this.start_time = new Date(from)
          this.finish_time = new Date(to)
          this.get_resources_key()
        }
      },
      db_analytics() {
        let agent_all = []
        let agent_inspect = []
        let ip_all = []
        let ip_inspect = []
        for (let index in this.db_list) {
          agent_all.push(this.db_list[index]['user_agent'])
          if (!agent_inspect.includes(this.db_list[index]['user_agent'])) {
            agent_inspect.push(this.db_list[index]['user_agent'])
          }

          ip_all.push(this.db_list[index]['ip_v4_address'])
          if (!ip_inspect.includes(this.db_list[index]['ip_v4_address'])) {
            ip_inspect.push(this.db_list[index]['ip_v4_address'])
          }

        }
        // console.log('all', agent_all)
        // console.log('inspect', agent_inspect)
        // console.log('all', ip_all)
        // console.log('inspect', ip_inspect)
        this.db_inspect['agent'] = agent_inspect.length
        this.db_inspect['ip'] = ip_inspect.length
      },
      db_delete(id) {
        this.$store.state.pageOptions.loading = true
        axios.delete(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.landing_id + '/landing_dbs/' + id + '/')
          .then(() => {
            this.get_db_list()
          })
          .catch((error) => {
            this.$store.state.pageOptions.loading = false
            console.log(error)
          })
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
      },
      range() {
        let range = {
          from: this.start_time,
          to: this.finish_time
        }
        if (range.from != '' && range.to != '') {
          this.get_resources_key()
        }
        return range
      },
      start_disabled() {
        let range = {
          from: this.finish_time
        }
        return range
      },
      finish_disabled() {
        let range = {
          to: this.start_time,
        }
        return range
      },
      db_width() {
        let percent = 0
        if (this.user_obj) {
          if ([0, 1].includes(this.user_obj.access_role)) {
            percent = 100 / (this.db_keys.length + 1)
          } else if (this.user_obj.is_staff || this.user_obj.is_superuser) {
            percent = 100 / (this.db_keys.length + 1)
          } else {
            percent = 100 / this.db_keys.length
          }

        }
        // Set field width by field counts
        return 'width:' + percent + '%; word-break: break-all;'
      }
    }
  }
</script>

<style lang="scss">
  .whole_wrap {
    margin: 0 2%;
  }

  .section {
    margin: 3% auto;
  }

  .list_header {
    box-shadow: 0px 0px 10px 1px rgba(0, 0, 0, 0.14);
  }

  .list_body {
    margin-top: 10px;
    border: 0;
  }

  .db_list_wrap {
    overflow-x: auto;
  }

  .db_list_header, .db_list_body {
    min-width: 1024px;
  }

  .section_box {
    /*box-shadow: 0px 0px 10px 1px rgba(0, 0, 0, 0.14);*/
  }

  .datepicker > div:first-child {
    width: calc(100% - 2px);
    height: 100%;
    margin: 0 auto;
  }

  .datepicker input {
    width: 100%;
    height: 100%;
    border: none;
    padding: 0.45rem;
  }
</style>

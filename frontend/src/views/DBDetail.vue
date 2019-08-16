<template>
  <div class="main">
    <div class="text_navigation">
      <router-link to="/">홈</router-link>
      <span>></span>
      <router-link to="/landing">랜딩 리스트</router-link>
      <span>></span>
      <router-link to="/db/detail">DB 정보</router-link>
    </div>

    <div class="container">
      <!-- Selected page -->
      <section class="section">
        <div class="landing_info">
          <h5>선택된 랜딩페이지</h5>
          <div v-if="window_width > 1000" class="list_area">
            <div class="list_header">
              <div class="list-group-item text-center d-inline-flex justify-content-between p-1 pt-2 pb-2 text-center"
                   style="border-radius: 0; width:100%;">
                <div class="col-3 p-0">업체</div>
                <div class="col-4 p-0">페이지</div>
                <div class="col-3 p-0">담당자</div>
                <div class="col-1 p-0 board_centre">조회수</div>
                <div class="col-1 p-0 board_centre">DB</div>
              </div>
            </div>
            <ul class="list_body text-center list-group list-group-flush col-12 pr-0 text-center">
              <li
                class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1 font-weight-bold border-0">
                <div class="col-3 p-0 col-sm-3">{{ landing_obj.company_id }}</div>
                <div class="col-3 p-0 col-sm-4">{{ landing_obj.landing_info.landing.name }}</div>
                <div class="col-3 p-0">{{ manager_name }}</div>
                <div class="col-1 p-0 board_centre" v-if="landing_obj.landing_info.views">{{ landing_obj.landing_info.views }}</div>
                <div class="col-1 p-0 board_centre" v-else>0</div>
                <div class="col-1 p-0 board_centre" v-if="landing_obj.landing_info.db">{{ landing_obj.landing_info.db }}</div>
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
                <div class="col-3 p-0">{{ landing_obj.landing_info.views }}</div>
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

      <hr>

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

      </section>

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

        <div class="list_area">

          <div class="list_header">
            <div
              class="list-group-item text-center d-inline-flex justify-content-around p-1 pt-2 pb-2 text-center border-bottom-0"
              style="border-radius: 0; width:100%;">
              <div v-for="key in db_keys" :style="db_width" class="p-0">{{ key }}</div>
            </div>
          </div>

          <ul class="text-center list-group list-group-flush text-center">
            <li class="list-group-item list-group-item-action d-inline-flex justify-content-around p-1"
                v-if="db_vals.length == 0">
              <div class="p-0">데이터가 없습니다.</div>
            </li>
            <li class="list-group-item list-group-item-action d-inline-flex justify-content-around p-1"
                v-else v-for="item in db_vals">
              <div class="p-0" v-for="val in item" :style="db_width">{{ val }}</div>
            </li>
          </ul>

        </div>

      </section>

      <!--      <div class="alert-warning">{{ db_keys }}</div>-->
      <!--<div class="alert-success">{{ db_vals }}</div>-->

    </div>
    <!-- /Container -->
  </div>
</template>

<script>

  import * as lang from "vuejs-datepicker/src/locale"

  export default {
    name: "db_detail",
    data: () => ({
      window_width: window.innerWidth,
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
      get_db_list() {
        this.landing_id = this.$route.params.landing_id
        axios.get(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.landing_id + '/')
          .then((response) => {
            this.landing_obj = response.data.data
            return axios.get(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.landing_id + '/landing_dbs/?limit=999999999&offset=0')
          })
          .catch((error) => {
            console.log('get landing', error)
          })
          .then((response) => {
            console.log('db gathering', response.data.data.results)
            this.landing_obj.landing_info.db = response.data.data.count
            this.db_list = response.data.data.results
            // Call get resources after data loaded
            this.get_resources_key()
            this.db_analytics()
            if (this.landing_obj.landing_info.landing.manager > -1) {
              return axios.get(this.$store.state.endpoints.baseUrl + 'users/' + this.landing_obj.landing_info.landing.manager + '/')
            } else {
              this.manager_name = '매니저 없음'
            }
          })
          .then((response) => {
            // console.log('get user res ', response)
            // this.manager_name = response.data.data.username
          })
          .catch((error) => {
            console.log('get db', error)
          })

      },
      get_resources_key() {
        this.db_keys = []
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

        if (this.db_keys.indexOf('유입경로') > -1) {
          this.db_keys.splice(this.db_keys.indexOf('유입경로'), 1)
          this.db_keys.push('유입경로')
        } else {
          this.db_keys.push('유입경로')
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
                  } else if (this.db_keys[i] === '유입경로') {
                    val_obj[index][this.db_keys[i]] = this.db_list[index]['inflow_path']
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
      }
    },
    computed: {
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
        // Set field width by field counts
        let percent = 100 / this.db_keys.length
        return 'width:' + percent + '%; word-break: break-all;'
      }
    }
  }
</script>

<style lang="scss">
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

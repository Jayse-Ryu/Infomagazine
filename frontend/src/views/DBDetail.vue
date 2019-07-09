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
                <div class="col-3 p-0">{{ landing_obj.landing_info.landing.manager }}</div>
                <div class="col-1 p-0 board_centre">{{ landing_obj.landing_info.views }}</div>
                <div class="col-1 p-0 board_centre">{{ landing_obj.landing_info.views }}</div>
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
        <h5>Url 상태</h5>

        <div class="list_area">
          <div class="list_header">
            <div class="list-group-item text-center d-inline-flex justify-content-between p-1 pt-2 pb-2 text-center"
                 style="border-radius: 0; width:100%;">
              <div class="col-4 p-0">URL</div>
              <div class="col-4 p-0">조회수</div>
              <div class="col-4 p-0">DB 수</div>
            </div>
          </div>
          <ul class="text-center list-group list-group-flush text-center">
            <li class="list-group-item list-group-item-action d-inline-flex justify-content-around p-1">
              <div class="col-4 p-0">main_url</div>
              <div class="col-4 p-0">123</div>
              <div class="col-4 p-0">28</div>
            </li>
            <li class="list-group-item list-group-item-action d-inline-flex justify-content-around p-1">
              <div class="col-4 p-0">main_url</div>
              <div class="col-4 p-0">123</div>
              <div class="col-4 p-0">28</div>
            </li>
            <li class="list-group-item list-group-item-action d-inline-flex justify-content-around p-1">
              <div class="col-4 p-0">main_url</div>
              <div class="col-4 p-0">123</div>
              <div class="col-4 p-0">28</div>
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
            <button type="button" class="btn btn-primary w-100">적용하기</button>
          </div>
          <div class="col-md-2">
            <button type="button" class="btn btn-info w-100">엑셀저장</button>
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
              <div class="p-0 w-100">업체</div>
              <div class="p-0 w-100">페이지</div>
              <div class="p-0 w-100">담당자</div>
              <div class="p-0 w-100">조회수</div>
              <div class="p-0 w-100">DB</div>
            </div>
          </div>

          <ul class="text-center list-group list-group-flush text-center">
            <li class="list-group-item list-group-item-action d-inline-flex justify-content-around p-1"
                v-for="item in db_list">
              <!--<div class="p-0 w-100">{{ landing_obj.company_id }}</div>
              <div class="p-0 w-100">{{ landing_obj.landing_info.landing.name }}</div>
              <div class="p-0 w-100">{{ landing_obj.landing_info.landing.manager }}</div>
              <div class="p-0 w-100">{{ landing_obj.landing_info.views }}</div>
              <div class="p-0 w-100">{{ landing_obj.landing_info.views }}</div>-->
              <div>{{ item }}</div>
            </li>
          </ul>

        </div>

      </section>

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
      db_list: [
        {
          이름: '류동근',
          연락처: '01088988898',
          성별: '남자',
          지역: '서울',
          created_date: '1562231881156',
          url: 'url_1'
        },
        {
          이름: '아무개',
          연락처: '',
          성별: '남자',
          지역: '서울',
          문의사항: '테스트가 되나요?',
          created_date: '1562231281156',
          url: 'url_1'
        },
        {
          이름: '고양이',
          연락처: '01099000009',
          성별: '수컷',
          지역: '집',
          문의사항: 'ㅇ러293런ㄹㅇㄹㄴ어2',
          좋아: false,
          created_date: '1562230181156',
          url: 'url_1'
        },
        {
          이름: '강아지',
          연락처: '01083981872',
          성별: '암컷',
          지역: '우리집',
          좋아: true,
          created_date: '1552231881156',
          url: 'url_1'
        },
      ],
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
        axios.get(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.landing_id)
          .then((response) => {
            console.log(response)
            this.landing_obj = response.data.data
            this.get_resources()
          })
          .catch((error) => {
            console.log(error)
          })
      },
      get_resources() {

        let key_flag = true

        for (let index in this.db_list) {
          if (this.db_list.hasOwnProperty(index)) {

            console.log('db key', this.db_list[index])

            for (let key in this.db_list[index]) {
              if (this.db_list[index].hasOwnProperty(key)) {

                console.log('index', index)
                console.log('key', key)
                console.log('val', this.db_list[index][key])
                // if(key_flag) {
                //   console.log('db key', this.db_list[index][key])
                // } else {
                //   console.log('db val', this.db_list[index][key])
                // }
                // key_flag = !key_flag
              }
            }
          }
        }

      }
      // set_data(option) {
      //   if (option == 'from') {
      //     console.log('from?')
      //     this.calendar_range.from = this.start_time
      //   } else if (option == 'to') {
      //     console.log('to?')
      //     this.calendar_range.to = this.finish_time
      //   }
      // }
    },
    computed: {
      range() {
        let range = {
          from: this.start_time,
          to: this.finish_time
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

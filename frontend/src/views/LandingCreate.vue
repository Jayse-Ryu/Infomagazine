<template>
  <div class="main">
    <div class="text_navigation">
      <router-link to="/">홈</router-link>
      <span>></span>
      <router-link to="/landing">랜딩 리스트</router-link>
      <span>></span>
      <router-link to="/landing/create">랜딩페이지 생성</router-link>
    </div>

    <div> {{ dynamo_obj }}</div>

    <div class="container" style="margin-top: 20px;">

      <form v-on:submit.prevent="landing_check">

        <h5>기본정보</h5>
        <section_basic
          :window_width="window_width"
          :company.sync="dynamo_obj.landing_info.landing.company"
          :name.sync="dynamo_obj.landing_info.landing.name"
          :base_url.sync="dynamo_obj.landing_info.landing.base_url"
          :error_name.sync="error_label.name"
          :error_base_url.sync="error_label.base_url"
          :push_landing="push_landing"
        />

        <hr>

        <h5>DB 폼</h5>
        <section_form_control
          :form.sync="dynamo_obj.landing_info.form"
          :form_arrow.sync="form_arrow"
          :field.sync="dynamo_obj.landing_info.field"
          :push_landing="push_landing"
        />
        <section_form_detail
          :window_width="window_width"
          :epoch_time="epoch_time"
          :form_arrow.sync="form_arrow"
          :field.sync="dynamo_obj.landing_info.field"
          :push_landing="push_landing"
        />

        <hr>

        <h5>추가내용</h5>
        <section_term
          :epoch_time="epoch_time"
          :term_switch.sync="dynamo_obj.landing_info.landing.is_term"
          :image_switch.sync="dynamo_obj.landing_info.landing.image_term"
          :term.sync="dynamo_obj.landing_info.term"
          :push_landing="push_landing"
        />

        <hr>

        <h5>페이지 내용</h5>
        <section_page_source
          :window_width="window_width"
          :title.sync="dynamo_obj.landing_info.landing.title"
          :header_script.sync="dynamo_obj.landing_info.landing.header_script"
          :body_script.sync="dynamo_obj.landing_info.landing.body_script"
          :push_landing="push_landing"
        />

        <!-- Order layout component -->
        <section_layout
          :window_width="window_width"
          :epoch_time="epoch_time"
          :order.sync="dynamo_obj.landing_info.sections"
          :form.sync="dynamo_obj.landing_info.form"
          :field.sync="dynamo_obj.landing_info.field"
          :is_term.sync="dynamo_obj.landing_info.landing.is_term"
          :push_landing="push_landing"
        />

        <section_layout_opt
          :window_width.sync="window_width"
          :landing.sync="dynamo_obj.landing_info.landing"
          :push_landing="push_landing"
        />

        <hr>

        <h5>옵션</h5>
        <section_page_opt
          :landing.sync="dynamo_obj.landing_info.landing"
          :push_landing="push_landing"
        />

        <hr>

        <div class="form-group row">
          <div class="col-12">
            <button type="submit" class="btn btn-primary col-12">생성</button>
            <button type="button" class="btn btn-dark col-12 mt-2" @click="back_to_list">취소</button>
          </div>
        </div>

      </form>

    </div>

    <popup_recovery
      :user_obj="user_obj"
      :auto_flag="auto_flag"
      :company_flag="company_flag"
    />

  </div>
</template>

<script>
  import popup_recovery from '@/components/landing_create/popup_1_recovery.vue'
  import section_basic from '@/components/landing_create/section_1_basic.vue'
  import section_form_control from '@/components/landing_create/section_2_form_control.vue'
  import section_form_detail from '@/components/landing_create/section_3_form_detail.vue'
  import section_term from '@/components/landing_create/section_4_term.vue'
  import section_page_source from '@/components/landing_create/section_5_page_source.vue'
  import section_layout from '@/components/landing_create/section_6_layout.vue'
  import section_layout_opt from '@/components/landing_create/section_7_layout_opt.vue'
  import section_page_opt from '@/components/landing_create/section_8_page_opt.vue'

  export default {
    name: "landing_create",
    components: {
      popup_recovery,
      section_basic,
      section_form_control,
      section_form_detail,
      section_term,
      section_page_source,
      section_layout,
      section_layout_opt,
      section_page_opt
    },
    data: () => ({
      window_width: window.innerWidth,
      error_label: {
        name: true,
        base_url: true,
      },
      epoch_time: 0,
      form_arrow: -1,
      auto_flag: false,
      company_flag: false,
      dynamo_obj: {
        company_id: '',
        created_date: '',
        updated_date: '',
        landing_info: {
          landing: {
            manager: -1,
            name: '',
            title: null,
            header_script: null,
            body_script: null,
            base_url: '',
            is_hijack: false,
            hijack_url: null,
            is_active: true,
            is_mobile: false,
            is_banner: false,
            banner_url: null,
            banner_image: null,
            inner_db: true,
            font: -1,
            is_term: false,
            image_term: false,
            show_company: false
          },
          term: {
            title: '',
            content: '',
            image_data: ''
          },
          form: [],
          field: [],
          sections: [],
          views: 0
        }
      }
    }),
    mounted() {
      // Window width calculator
      let that = this
      that.$nextTick(function () {
        window.addEventListener('resize', function (e) {
          that.window_width = window.innerWidth
        })
      })
      this.epoch_time = (new Date).getTime()
    },
    methods: {
      landing_check() {
        // Start validate before create
        this.$validator.validateAll()
        console.log(this.user_obj)
        this.dynamo_obj.landing_info.landing.manager = this.user_obj.id

        // Empty filtering first
        if (this.dynamo_obj.landing_info.landing.company == -1) {
          alert('업체를 선택하세요!')
          document.getElementById('company_id').focus()
        } else if (this.dynamo_obj.landing_info.landing.manager == -1) {
          alert('관리자를 선택하세요!')
          document.getElementById('manager').focus()
        } else if (!this.dynamo_obj.landing_info.landing.name) {
          alert('랜딩페이지 이름을 입력하세요!')
          document.getElementById('landing').focus()
        } else if (this.duplicated_name_flag) {
          alert('랜딩페이지 이름이 이미 존재합니다!')
          document.getElementById('landing').focus()
        } else if (!this.dynamo_obj.landing_info.landing.base_url) {
          alert('메인 URL을 입력하세요!')
          document.getElementById('base_url').focus()
        } else if (this.duplicated_url_flag) {
          alert('메인 URL이 이미 존재합니다!')
          document.getElementById('base_url').focus()
        } else {
          if (this.dynamo_obj.landing_info.form.length > 0) {
            let flag = true
            for (let i = 0; i < this.dynamo_obj.landing_info.field.length; i++) {
              if (this.dynamo_obj.landing_info.field[i].name == '') {
                alert('폼 그룹의 필드 이름을 모두 입력해주세요!')
                document.getElementById('db_field').focus()
                flag = false
                return flag
              }
            }
            if (flag) {
              this.push_landing('checked')
            }
          } else {
            this.push_landing('checked')
          }
        }
      },
      push_landing(option) {
        // option first(mounted) or checked(button clicked)
        // let axios = this.$axios
        const config = {
          headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'multipart/form-data'
          }
        }
        this.dynamo_obj.company_id = this.dynamo_obj.landing_info.landing.company.toString()
        this.dynamo_obj.created_date = this.epoch_time.toString()
        // Empty objects make as Null
        for (let key in this.dynamo_obj.landing_info.landing) {
          if (this.dynamo_obj.landing_info.landing.hasOwnProperty(key)) {
            if (this.dynamo_obj.landing_info.landing[key] === '' && typeof (this.dynamo_obj.landing_info.landing[key]) != 'boolean') {
              this.dynamo_obj.landing_info.landing[key] = null
            }
            // if (key === 'name') {
            //   console.log('key is name~')
            // }
          }
        }
        for (let key in this.dynamo_obj.landing_info.form) {
          if (this.dynamo_obj.landing_info.form.hasOwnProperty(key)) {
            if (this.dynamo_obj.landing_info.form[key] === '' && typeof (this.dynamo_obj.landing_info.form[key]) != 'boolean') {
              this.dynamo_obj.landing_info.form[key] = null
            }
          }
        }
        for (let key in this.dynamo_obj.landing_info.field) {
          if (this.dynamo_obj.landing_info.field.hasOwnProperty(key)) {
            for (let j in this.dynamo_obj.landing_info.field[key]) {
              if (this.dynamo_obj.landing_info.field[key][j] === '') {
                this.dynamo_obj.landing_info.field[key][j] = null
              }
            }
          }
        }
        for (let key in this.dynamo_obj.landing_info.order) {
          if (this.dynamo_obj.landing_info.order.hasOwnProperty(key)) {
            for (let j in this.dynamo_obj.landing_info.order[key]) {
              if (this.dynamo_obj.landing_info.order[key][j] === '') {
                this.dynamo_obj.landing_info.order[key][j] = null
              }
            }
          }
        }
        for (let key in this.dynamo_obj.landing_info.term) {
          if (this.dynamo_obj.landing_info.term.hasOwnProperty(key)) {
            if (this.dynamo_obj.landing_info.term[key] === '' && typeof (this.dynamo_obj.landing_info.term[key]) != 'boolean') {
              this.dynamo_obj.landing_info.term[key] = null
            }
          }
        }

        if (option === 'checked') {
          this.dynamo_obj.updated_date = (Date.now()).toString()
          this.$store.state.pageOptions.loading = true
          console.log('landing create object is? ', this.dynamo_obj)
          axios.post(this.$store.state.endpoints.baseUrl + 'landing_pages/', this.dynamo_obj, config)
            .then(() => {
              this.$store.state.pageOptions.loading = false
              if (option == 'checked') {
                alert('랜딩이 생성되었습니다.')
                this.bye()
              }
            })
            .catch((error) => {
              if (option == 'checked') {
                alert('랜딩 생성이 실패하였습니다.')
                this.$store.state.pageOptions.loading = false
              }
              console.log(error)
            })
        } else {
          if(!this.error_label.name && !this.error_label.base_url) {
            console.log('Landing pushed! ')
            // axios.post(this.$store.state.endpoints.baseUrl + 'landing_pages/', this.dynamo_obj, config)
            //   .catch((error) => {
            //     console.log(error)
            //   })
          }
        }


      },
      bye() {
        this.$router.currentRoute.meta.protect_leave = 'no'
        this.$router.push({
          name: 'landing_list',
        })
      },
      back_to_list() {
        if (confirm('정말 취소하시겠습니까?')) {
          // let axios = this.$axios
          let landing_num = this.epoch_time
          axios.delete(this.$store.state.endpoints.baseUrl + 'landings/api/' + landing_num)
            .then(() => {
              alert('목록으로 돌아갑니다.')
              this.$router.currentRoute.meta.protect_leave = 'no'
              this.$router.push({name: 'landing_list'})
            })
            .catch((error) => {
              console.log(error)
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
            'failed': true
          }
        } else {
          user_json = JSON.parse(local_user)
        }

        return user_json
      },
    }
  }
</script>

<style lang="scss">
  hr {
    width: 100%;
  }

  /* ios switch */
  .switch {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 34px;
  }

  /* Hide default HTML checkbox */
  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }

  /* The slider */
  .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    -webkit-transition: .4s;
    transition: .4s;
  }

  .slider:before {
    position: absolute;
    content: "";
    height: 26px;
    width: 26px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    -webkit-transition: .4s;
    transition: .4s;
  }

  input:checked + .slider {
    background-color: #287BFF;
  }

  input:focus + .slider {
    box-shadow: 0 0 1px #287BFF;
  }

  input:checked + .slider:before {
    -webkit-transform: translateX(26px);
    -ms-transform: translateX(26px);
    transform: translateX(26px);
  }

  .slider.round {
    border-radius: 34px;
  }

  .slider.round:before {
    border-radius: 50%;
  }

  .term_label {
    display: inline-block;
  }

  /*====*/

  /* margin dummy div */
  .margin_div {
    display: inline-block;
    width: 4%;
  }

  @media (max-width: 768px) {
    .margin_div {
      display: none;
    }
  }

  /*==*/

  .input_one_btn {
    max-width: 720px;
    margin-right: auto;
  }

  .layout_control {
    width: 60px;
    height: 30px;
    padding: 0;
    margin: 5px 0 5px 5px;
    font-size: 19px;
    font-weight: bold;
  }

  .landing_layout {
    background-color: #dedede;
    border-radius: 4px;
    min-height: 140px;
  }

  .layout_item {
    background-color: #efefef;
    border-radius: 8px;
    overflow: hidden;
  }

  .item_area {
    width: 100%;
    height: 100%;
    transition: all 250ms ease-out;
  }

  .color_wrap {
    overflow: hidden;
  }

  .color_picker {
    position: relative;
    width: 500%;
    height: 300%;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .main_layout {
    border: 1px solid #ced4da;
    border-radius: 0.25rem;
    overflow: auto;
    transition: all 200ms ease-in-out;
  }

  .basket {
    border: 1px solid #ee5151;
    width: 1000px;
    min-height: 500px;
    overflow-x: hidden;
    overflow-y: auto;
    position: relative;
    margin: auto;
  }

  .drag_thing {
    /*position: absolute;*/
    /*display: inline-block;*/
    background-color: #eaeaea;
    border: 1px solid #818181;
  }

  .field_option_wrap {
    position: absolute;
    width: calc(100% - 10px);
    background-color: #fafafa;
    border: 1px solid #c1c1c1;
    border-radius: 8px;
    margin: auto;
    top: 40px;
    z-index: 900;
  }

  .console {
    width: 100%;
    max-width: 1000px;
    border: 1px solid #515151;
    margin: auto;
    background-color: #eaeaea;
  }

  .preview {
    width: 100%;
    margin: auto;
  }

  .video_handler {
    position: absolute;
    border-radius: 7px 0px 0px 7px;
    top: -1px;
    left: -104px;
    background-color: #515151;
    color: #e1e1e1;
    font-weight: bold;
    padding: 8px;
  }

  .video_handler_2 {
    position: absolute;
    border-radius: 0px 7px 7px 7px;
    bottom: -34px;
    right: -54px;
    background-color: #515151;
    color: #e1e1e1;
    font-weight: bold;
    padding: 8px;
  }

  .form_layout {
    position: absolute;
    width: 100%;
    height: 100%;
  }

  .form_layout_cont {
    position: relative;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    padding: 0 15px;
    overflow: auto;
    /*max-width: 750px;*/
  }

  .order_form_label {
    width: 25%;
  }

  .order_form_box {
    width: 75%;
    padding: 0 15px;
  }

  .select_company_wrap {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    background: rgba(0, 0, 0, 0.3);
    transition: 200ms visibility ease-in-out;
  }

  .company_list_box {
    background: #fff;
    padding: 25px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border: 1px solid #eaeaea;
    border-radius: 8px;
  }

  .order_form_button_image {
    width: 100%;
    height: 100%;
    max-height: 50px;
    object-fit: contain;
  }

  /* The slider itself */
  .opacity_slider {
    -webkit-appearance: none; /* Override default CSS styles */
    appearance: none;
    background: #eaeaea; /* Grey background */
    outline: none; /* Remove outline */
    opacity: 0.9; /* Set transparency (for mouse-over effects on hover) */
    -webkit-transition: .2s; /* 0.2 seconds transition on hover */
    transition: opacity .2s;
    border-radius: 5px;
    padding: 0 0.25em;
  }

  /* Mouse-over effects */
  .opacity_slider:hover {
    opacity: 1; /* Fully shown on mouse-over */
  }

  /* The slider handle (use -webkit- (Chrome, Opera, Safari, Edge) and -moz- (Firefox) to override default look) */
  .opacity_slider::-webkit-slider-thumb {
    -webkit-appearance: none; /* Override default look */
    appearance: none;
    width: 30px; /* Set a specific slider handle width */
    height: 30px; /* Slider handle height */
    background: #17a2b8; /* Green background */
    cursor: pointer; /* Cursor on hover */
    border-radius: 5px;
  }

  .opacity_slider::-moz-range-thumb {
    width: 30px; /* Set a specific slider handle width */
    height: 30px; /* Slider handle height */
    background: #17a2b8; /* Green background */
    cursor: pointer; /* Cursor on hover */
    border-radius: 5px;
  }
</style>

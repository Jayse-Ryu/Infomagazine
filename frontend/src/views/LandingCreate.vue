<template>
  <div class="main">
    <div class="text_navigation">
      <router-link to="/">홈</router-link>
      <span>></span>
      <router-link to="/landing">랜딩 리스트</router-link>
      <span>></span>
      <router-link to="/landing/create">랜딩페이지 생성</router-link>
    </div>

    <div class="container" style="margin-top: 20px;">

      <form v-on:submit.prevent="landing_check">

        <h5>기본정보</h5>
        <section_basic
          :window_width="window_width"
          :company.sync="dynamo_obj.company_id"
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
          :set_field="set_field_position"
          :push_landing="push_landing"
        />
        <section_form_detail
          :window_width="window_width"
          :page_id.sync="page_id"
          :epoch_time="epoch_time"
          :updated_date="dynamo_obj.updated_date"
          :form_arrow.sync="form_arrow"
          :field.sync="dynamo_obj.landing_info.field"
          :set_field="set_field_position"
          :push_landing="push_landing"
        />

        <!--<hr>

        <h5>기타 폼</h5>
        <section_form_control_etc
          :page_id.sync="page_id"
          :etc.sync="dynamo_obj.landing_info.etc"
          :etc_arrow.sync="etc_arrow"
          :epoch_time="epoch_time"
          :updated_date="dynamo_obj.updated_date"
          :push_landing="push_landing"
        />-->

        <hr>

        <h5>추가내용</h5>
        <section_term
          :epoch_time="epoch_time"
          :page_id.sync="page_id"
          :landing="dynamo_obj.landing_info.landing"
          :term.sync="dynamo_obj.landing_info.term"
          :updated_date="dynamo_obj.updated_date"
          :push_landing="push_landing"
        />

        <hr>

        <h5>페이지 내용</h5>
        <section_page_source
          :window_width="window_width"
          :title.sync="dynamo_obj.landing_info.landing.title"
          :header_script.sync="dynamo_obj.landing_info.landing.header_script"
          :body_script.sync="dynamo_obj.landing_info.landing.body_script"
          :tracking_info.sync="dynamo_obj.landing_info.landing.tracking_info"
          :push_landing="push_landing"
        />

        <!-- Order layout component -->
        <section_layout
          :window_width="window_width"
          :page_id.sync="page_id"
          :epoch_time="epoch_time"
          :order.sync="dynamo_obj.landing_info.sections"
          :form.sync="dynamo_obj.landing_info.form"
          :field.sync="dynamo_obj.landing_info.field"
          :etc.sync="dynamo_obj.landing_info.etc"
          :is_term.sync="dynamo_obj.landing_info.landing.is_term"
          :updated_date="dynamo_obj.updated_date"
          :set_field="set_field_position"
          :push_landing="push_landing"
        />

        <section_layout_opt
          :window_width.sync="window_width"
          :page_id.sync="page_id"
          :epoch_time="epoch_time"
          :updated_date="dynamo_obj.updated_date"
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

        <section_url_list
          :window_width="window_width"
          :page_id.sync="page_id"
          :url_list.sync="url_list"
          :del_url="del_url_list"
        />

        <hr>

        <div class="form-group row">
          <div class="col-12">
            <button type="submit" class="btn btn-primary col-12">생성</button>
            <button type="button" v-if="page_id" class="btn btn-info col-12 mt-2" @click="generate">
              파일 생성하기
            </button>
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
    import section_form_control_etc from '@/components/landing_create/section_2_1_form_control.vue'
    import section_form_detail from '@/components/landing_create/section_3_form_detail.vue'
    import section_term from '@/components/landing_create/section_4_term.vue'
    import section_page_source from '@/components/landing_create/section_5_page_source.vue'
    import section_layout from '@/components/landing_create/section_6_layout.vue'
    import section_layout_opt from '@/components/landing_create/section_7_layout_opt.vue'
    import section_page_opt from '@/components/landing_create/section_8_page_opt.vue'
    import section_url_list from '@/components/landing_create/section_9_url_list.vue'

    export default {
        name: "landing_create",
        components: {
            popup_recovery,
            section_basic,
            section_form_control,
            section_form_control_etc,
            section_form_detail,
            section_term,
            section_page_source,
            section_layout,
            section_layout_opt,
            section_page_opt,
            section_url_list
        },
        data: () => ({
            window_width: window.innerWidth,
            error_label: {
                name: true,
                base_url: true,
            },
            validation_flag: false,
            page_id: '',
            epoch_time: 0,
            form_arrow: -1,
            etc_arrow: -1,
            auto_flag: false,
            company_flag: false,
            dynamo_obj: {
                company_id: -1,
                created_date: '',
                updated_date: '',
                views: 0,
                landing_info: {
                    landing: {
                        manager: -1,
                        name: '',
                        title: null,
                        header_script: null,
                        body_script: null,
                        tracking_info: {
                            tnk: false,
                            fb: '',
                            ka: '',
                            ga: '',
                            gtm: '',
                            gdn: ''
                        },
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
                        url: '',
                        title: '',
                        content: '',
                        image_data: ''
                    },
                    form: [],
                    field: [],
                    etc: [],
                    sections: []
                }
            },
            url_list: []
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
            this.dynamo_obj.created_date = this.epoch_time.toString()
        },
        methods: {
            validation_back() {
                this.validation_flag = false

                let field = this.dynamo_obj.landing_info.field
                // console.log('temp field', field)
                // Preparing validation list
                let vali = [
                    'required',
                    'korean_only',
                    'english_only',
                    'number_only',
                    'phone_only',
                    'email',
                    'duplication_check',
                    'age_limit',
                    'value_min',
                    'value_max'
                ]

                // Get one field object
                for (let i in field) {
                    // Inspect by validation list
                    for (let key in vali) {
                        // Inspect object by a key
                        if (field[i].validation.hasOwnProperty(vali[key])) {
                            // If not value obj, push key true
                            if (vali[key] != 'value_min' && vali[key] != 'value_max') {
                                field[i].validation[vali[key]] = true
                            } else {
                                field[i].validation[vali[key]] = field[i].validation[vali[key]]
                            }
                        } else {
                            // Distinguish object default value by keys
                            let form = {}
                            if (vali[key] == 'value_min') {
                                form = {
                                    value: 0,
                                    option: 'gt'
                                }
                                field[i].validation[vali[key]] = form
                            } else if (vali[key] == 'value_max') {
                                form = {
                                    value: 120,
                                    option: 'lt'
                                }
                                field[i].validation[vali[key]] = form
                            } else {
                                field[i].validation[vali[key]] = false
                            }
                        }
                    }
                }
                let temp = JSON.stringify(this.dynamo_obj)
                this.dynamo_obj = JSON.parse(temp)

                this.validation_flag = true
            },
            set_field_position(option) {
                if (option == 'form') {
                    // Section list short name
                    let sections = this.dynamo_obj.landing_info.sections
                    // Dynamo field short name
                    let fields = this.dynamo_obj.landing_info.field

                    // Fields in section object (static data)
                    let original_fields = []
                    // Fields in dynamo object (dynamically change)
                    let dynamic_fields = []

                    // Field sign list for add
                    let for_add = []
                    // Field sign list for delete
                    let for_rem = []

                    // Get A Section
                    for (let i = 0; i < sections.length; i++) {
                        // Object lists
                        let objects = sections[i]

                        // Get A object
                        for (let j = 0; j < objects.length; j++) {
                            // If the layout object is form_group and it has a form group id
                            if (objects[j].type == 2 && objects[j].form_group_id != 0) {
                                // Init calculator list
                                original_fields = []
                                dynamic_fields = []
                                for_add = []
                                for_rem = []

                                // Set original field
                                for (let l = 0; l < objects[j].fields.length; l++) {
                                    original_fields.push(objects[j].fields[l].sign)
                                }

                                // Set dynamic field as object's form group
                                for (let k = 0; k < fields.length; k++) {
                                    if (fields[k].form_group_id == objects[j].form_group_id) {
                                        dynamic_fields.push(fields[k].sign)
                                    }
                                }

                                // ///////////Here! calculate
                                // Get fields for add
                                for (let w = 0; w < dynamic_fields.length; w++) {
                                    if (!original_fields.includes(dynamic_fields[w])) {
                                        for_add.push(dynamic_fields[w])
                                    }
                                }
                                // Get fields for remove
                                for (let q = 0; q < original_fields.length; q++) {
                                    if (!dynamic_fields.includes(original_fields[q])) {
                                        for_rem.push(original_fields[q])
                                    }
                                }
                                // ///////////Here! calculate

                                // Add fields into Object fields
                                for (let e = 0; e < for_add.length; e++) {
                                    let field_start = {
                                        sign: for_add[e],
                                        position: {
                                            x: 0,
                                            y: 0,
                                            w: 200,
                                            h: 50,
                                            z: 10
                                        }
                                    }
                                    objects[j].fields.push(field_start)
                                }

                                // Remove fields from Object fields
                                for (let r = 0; r < objects[j].fields.length; r++) {
                                    if (for_rem.includes(objects[j].fields[r].sign)) {
                                        objects[j].fields.splice(r, 1)
                                    }
                                }

                            }// is object form group?
                            else if (objects[j].type != 2 || objects[j].form_group_id == 0) {
                                // If object type is not form, and there is no form group id
                                objects[j].fields = []
                            }
                        }// get object
                    }// get section
                }
            },
            landing_check() {
                // Start validate before create
                this.$validator.validateAll()
                // console.log(this.user_obj)
                this.dynamo_obj.landing_info.landing.manager = this.user_obj.id

                // Empty filtering first
                if (this.dynamo_obj.company_id == -1) {
                    alert('업체를 선택하세요!')
                    document.getElementById('company_id').focus()
                } /*else if (this.dynamo_obj.landing_info.landing.manager == -1) {
          alert('관리자를 선택하세요!')
          document.getElementById('manager').focus()
        }*/ else if (!this.dynamo_obj.landing_info.landing.name) {
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
            field_validation() {
                this.validation_flag = false

                let type_text = ['required', 'korean_only', 'english_only', 'number_only', 'email', 'duplication_check']
                let type_num = ['required', 'number_only', 'duplication_check']
                let type_tel = ['required', 'phone_only', 'duplication_check']
                let type_scr = ['required']
                let type_chk = ['required']
                let type_date = ['required', 'age_limit', 'value_min', 'value_max']
                let type_agr = ['required']

                for (let index = 0; index < this.dynamo_obj.landing_info.field.length; index++) {
                    let field = this.dynamo_obj.landing_info.field[index]

                    if (field.type == 1) {
                        // text
                        let type = type_text
                        let replace = {}
                        for (let j = 0; j < type.length; j++) {
                            if (field.validation.hasOwnProperty(type[j])) {
                                if (field.validation[type[j]]) {
                                    replace[type[j]] = {}
                                }
                            }
                        }
                        field.validation = replace
                    } else if (field.type == 2) {
                        // num
                        let type = type_num
                        let replace = {}
                        for (let j = 0; j < type.length; j++) {
                            if (field.validation.hasOwnProperty(type[j])) {
                                if (field.validation[type[j]]) {
                                    replace[type[j]] = {}
                                }
                            }
                        }
                        field.validation = replace
                    } else if (field.type == 3) {
                        // phone
                        let type = type_tel
                        let replace = {}
                        for (let j = 0; j < type.length; j++) {
                            if (field.validation.hasOwnProperty(type[j])) {
                                if (field.validation[type[j]]) {
                                    replace[type[j]] = {}
                                }
                            }
                        }
                        field.validation = replace
                    } else if (field.type == 4) {
                        // scr
                        let type = type_scr
                        let replace = {}
                        for (let j = 0; j < type.length; j++) {
                            if (field.validation.hasOwnProperty(type[j])) {
                                if (field.validation[type[j]]) {
                                    replace[type[j]] = {}
                                }
                            }
                        }
                        field.validation = replace
                        // console.log('scr new obj', replace)
                    } else if (field.type == 5) {
                        field.validation = {}
                        if (field.default == '') {
                            if (field.list.length != 0) {
                                field.default = field.list[0]
                            }
                        }
                    } else if (field.type == 6) {
                        // chk
                        let type = type_chk
                        let replace = {}
                        for (let j = 0; j < type.length; j++) {
                            if (field.validation.hasOwnProperty(type[j])) {
                                if (field.validation[type[j]]) {
                                    replace[type[j]] = {}
                                }
                            }
                        }
                        field.validation = replace
                    } else if (field.type == 7) {
                        // date
                        let type = type_date
                        let replace = {}
                        let flag = false

                        // set flag
                        for (let j = 0; j < type.length; j++) {
                            if (field.validation.hasOwnProperty(type[j])) {
                                if (type[j] == 'age_limit') {
                                    flag = field.validation[type[j]]
                                }
                            }
                        }

                        // Flag true == age_limit is true
                        if (flag) {
                            for (let k = 0; k < type.length; k++) {
                                if (field.validation.hasOwnProperty(type[k])) {
                                    if (type[k] == 'value_min' || type[k] == 'value_max') {
                                        replace[type[k]] = field.validation[type[k]]
                                    } else {
                                        if (field.validation[type[k]]) {
                                            replace[type[k]] = {}
                                        }
                                    }
                                }
                            }
                        } else {
                            for (let k = 0; k < type.length; k++) {
                                if (field.validation.hasOwnProperty(type[k])) {
                                    if (type[k] != 'value_min' && type[k] != 'value_max') {
                                        if (field.validation[type[k]]) {
                                            replace[type[k]] = {}
                                        }
                                    }
                                }
                            }
                        }

                        field.validation = replace
                    } else if (field.type == 8) {
                        field.validation = {}
                    } else if (field.type == 9) {
                        // agr
                        let type = type_agr
                        let replace = {}
                        for (let j = 0; j < type.length; j++) {
                            if (field.validation.hasOwnProperty(type[j])) {
                                if (field.validation[type[j]]) {
                                    replace[type[j]] = {}
                                }
                            }
                        }
                        if (field.default == 'true' || field.default == 'false') {
                            field.default = JSON.parse(field.default)
                        } else {
                            field.default = true
                        }

                        field.validation = replace
                    }
                }
                this.validation_flag = false
            },
            push_landing(option) {
                // option first(mounted) or checked(button clicked)
                // let axios = this.$axios
                const config = {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }
                // Empty objects make as Null
                if (option === 'checked') {
                    this.validation_flag = true
                    this.dynamo_obj.updated_date = (Date.now()).toString()
                    this.$store.state.pageOptions.loading = true

                    // console.log('landing create object is? ', this.dynamo_obj)

                    if (!this.page_id) {
                        this.field_validation()
                        axios.post(this.$store.state.endpoints.baseUrl + 'landing_pages/', this.dynamo_obj, config)
                            .then((response) => {
                                this.$store.state.pageOptions.loading = false
                                this.page_id = response.data.data.inserted_id
                                this.validation_back()
                                alert('랜딩이 생성되었습니다.')
                                this.bye()
                            })
                            .catch((error) => {
                                alert('랜딩 생성 중 오류가 발생하였습니다.')
                                this.$store.state.pageOptions.loading = false
                                this.validation_back()
                                console.log(error)
                            })
                    } else {
                        if (this.validation_flag === true) {
                            this.field_validation()
                            axios.put(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.page_id + '/', {
                                'company_id': this.dynamo_obj.company_id,
                                'landing_info': this.dynamo_obj.landing_info
                            }, config)
                                .then(() => {
                                    alert('랜딩이 생성되었습니다.')
                                    this.$store.state.pageOptions.loading = false
                                    this.validation_back()
                                    this.bye()
                                })
                                .catch((error) => {
                                    alert('랜딩 생성 중 오류가 발생하였습니다.')
                                    console.log('Landing update fail', error)
                                    this.validation_back()
                                    this.$store.state.pageOptions.loading = false
                                })
                        }
                    }
                } else {
                    if (this.validation_flag === true) {
                        this.field_validation()
                        if (!this.page_id) {
                            axios.post(this.$store.state.endpoints.baseUrl + 'landing_pages/', this.dynamo_obj, config)
                                .then((response) => {
                                    this.page_id = response.data.data.inserted_id
                                    this.validation_back()
                                })
                                .catch((error) => {
                                    console.log('Landing update fail', error)
                                    this.validation_back()
                                })
                        } else {
                            axios.put(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.page_id + '/', {
                                'company_id': this.dynamo_obj.company_id,
                                'landing_info': this.dynamo_obj.landing_info
                            }, config)
                                .then(() => {
                                    this.validation_back()
                                })
                                .catch((error) => {
                                    this.validation_back()
                                    console.log('Landing update fail', error)
                                })
                        }
                    }
                }
            },
            back_to_list() {
                if (confirm('정말 취소하시겠습니까?')) {
                    // let axios = this.$axios
                    // let landing_num = this.epoch_time
                    axios.delete(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.page_id + '/')
                        .then(() => {
                            alert('목록으로 돌아갑니다.')
                            this.$router.currentRoute.meta.protect_leave = 'no'
                            this.$router.push({name: 'landing_list'})
                        })
                        .catch((error) => {
                            console.log(error)
                        })
                }
            },
            bye() {
                this.$router.currentRoute.meta.protect_leave = 'no'
                this.$router.push({
                    name: 'landing_list',
                })
            },
            generate() {
                if (this.dynamo_obj.landing_info.landing.base_url) {
                    if (this.validation_flag === true) {
                        this.field_validation()
                        this.$store.state.pageOptions.loading = true
                        const config = {
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        }

                        if (this.page_id) {
                            axios.put(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.page_id + '/', {
                                'company_id': this.dynamo_obj.company_id,
                                'landing_info': this.dynamo_obj.landing_info
                            }, config)
                                .then(() => {
                                    // this.validation_back()
                                    return axios.post(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.page_id + '/landing_urls/')
                                })
                                .catch((error) => {
                                    this.$store.state.pageOptions.loading = false
                                    console.log('Landing update fail', error)
                                    this.validation_back()
                                })
                                .then(() => {
                                    this.validation_back()
                                    this.get_url_list()
                                    this.$store.state.pageOptions.loading = false
                                })
                                .catch((error) => {
                                    this.validation_back()
                                    console.log(error)
                                    this.$store.state.pageOptions.loading = false
                                })
                        } else {
                            this.$store.state.pageOptions.loading = false
                        }

                        // axios.post(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.page_id + '/landing_urls/')
                        //   .then((response) => {
                        //     // console.log('created', response)
                        //     this.validation_back()
                        //     this.get_url_list()
                        //   })
                        //   .catch((error) => {
                        //     this.validation_back()
                        //     console.log(error)
                        //   })
                    }
                } else {
                    alert('메인 Url을 먼저 입력하세요!')
                    document.getElementById('base_url').focus()
                }
            },
            get_url_list() {
                axios.get(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.page_id + '/landing_urls/')
                    .then((response) => {
                        this.url_list = response.data.data
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            },
            del_url_list(key) {
                let cutter = 'https://landings.infomagazine.xyz/' + this.page_id + '/'
                let url_done = key.replace(cutter, '')

                axios.delete(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.page_id + '/landing_urls/' + url_done.split('.')[0] + '/')
                    .then((response) => {
                        this.get_url_list()
                    })
                    .catch((error) => {
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
    box-sizing: content-box;
    margin: auto;
  }

  .drag_thing {
    background-color: rgba(240, 240, 240, 0.4);
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
    box-sizing: content-box;
    background-color: #f7f7f7;
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

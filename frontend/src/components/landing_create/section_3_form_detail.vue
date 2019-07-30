<template>

  <div class="form-group row mb-0" v-if="arrow != -1">
    <label class="col-sm-3 col-form-label-sm mt-3" for="db_field">DB 필드</label>
    <form class="col-sm-9 mt-sm-3 row ml-0" v-on:submit.prevent="field_add">
      <select class="form-control col-sm-5 col-md-5" name="company" id="db_field" v-model.number="field_selected">
        <option value="-1">타입을 선택하세요</option>
        <option value="1">텍스트 입력</option>
        <option value="2">숫자 입력</option>
        <option value="3">전화번호 입력</option>
        <option value="4">선택 스크롤</option>
        <option value="5">선택 버튼</option>
        <option value="6">체크 박스</option>
        <option value="7">날짜</option>
        <option value="8">완료 버튼</option>
        <option value="9">약관 동의</option>
      </select>
      <div class="margin_div"></div>
      <input type="text" class="form-control col-sm-7 col-md-5" placeholder="필드이름" maxlength="10"
             v-model="field_temp_name">
      <div class="margin_div"></div>
      <button type="submit" class="btn btn-primary col-md-1 p-0">추가</button>
    </form>

    <label class="col-sm-3 col-form-label-sm mt-3" for="form_field_list">필드 리스트</label>
    <div class="col-sm-9 mt-sm-3 row ml-0">
      <ul class="list-group list-group-flush col-12 pr-0" id="form_field_list">
        <li class="list-group-item list-group-item-action d-inline-flex p-1 font-weight-bold">
          <div class="col-3 p-2 text-center" style="word-break: keep-all;">필드 타입</div>
          <div class="col-3 p-2 text-center" style="word-break: keep-all;">필드 이름</div>
          <div class="col-6 p-2 text-center">옵션</div>
        </li>
        <li class="list-group-item list-group-item-action d-inline-flex justify-content-between p-1"
            v-for="content in field_obj" v-if="content.form_group_id == arrow">
          <div class="col-3 p-2 text-center" v-if="content.type == 1">텍스트 입력</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 2">숫자 입력</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 3">전화번호 입력</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 4">선택 스크롤</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 5">선택 버튼</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 6">체크 박스</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 7">날짜</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 8">완료 버튼</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 9">약관 동의</div>
          <div class="col-3 p-2 text-center">{{ content.name }}</div>
          <button type="button" class="btn btn-outline-info p-0 col-3 col-sm-2 m-auto" data-toggle="collapse"
                  v-bind:href="'#collapse_option'+ content.sign" aria-expanded="false">
            설정
          </button>
          <button type="button" class="btn btn-outline-danger p-0 col-3 col-sm-2 m-auto"
                  @click="field_delete(content.sign)">
            삭제
          </button>
          <div class="field_option_wrap collapse" v-bind:id="'collapse_option'+ content.sign"
               data-parent="#form_field_list">
            <form v-on:submit.prevent="field_option_close">
              <div class="form-group row p-4 mb-0">

                <label v-if="[1, 2, 3, 4, 5, 6, 7, 9].includes(content.type * 1)"
                       class="col-sm-3 col-form-label-sm mt-3"
                       :for="'la_switch'+content.sign">라벨 켜기</label>
                <div v-if="[1, 2, 3, 4, 5, 6, 7, 9].includes(content.type * 1)" class="col-sm-9 mt-sm-3">
                  <label class="switch" :for="'la_switch'+content.sign">
                    <input type="checkbox" :id="'la_switch'+content.sign" v-model="content.label">
                    <span class="slider round"></span>
                  </label>
                </div>

                <label class="col-sm-3 col-form-label-sm mt-3" for="f_type">타입*</label>
                <div class="col-sm-9 mt-sm-3">
                  <select class="form-control" id="f_type" v-model.number="content.type">
                    <option value="1">텍스트 입력</option>
                    <option value="2">숫자 입력</option>
                    <option value="3">전화번호 입력</option>
                    <option value="4">선택 스크롤</option>
                    <option value="5">선택 버튼</option>
                    <option value="6">체크 박스</option>
                    <option value="7">날짜</option>
                    <option value="8">완료 버튼</option>
                    <option value="9">약관 동의</option>
                  </select>
                </div>

                <label class="col-sm-3 col-form-label-sm mt-3" for="f_name">필드 이름*</label>
                <div class="col-sm-9 mt-sm-3">
                  <input type="text" class="form-control" id="f_name" maxlength="10" v-model="content.name">
                </div>

                <label v-if="content.type != 5 && content.type != 6 && content.type != 8"
                       class="col-sm-3 col-form-label-sm mt-3" for="f_holder">
                  <span>안내문</span>
                  <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
                        v-tooltip="{
                              content: msg.holder,
                              placement: 'right',
                              offset: 5,
                              trigger: 'hover',
                              }">?</span>
                  <span class="question badge btn-secondary p-1 align-middle" v-else
                        v-tooltip="{
                              content: msg.holder,
                              placement: 'right',
                              offset: 5,
                              trigger: 'click',
                              }">?</span>
                </label>
                <div v-if="content.type != 5 && content.type != 6 && content.type != 8" class="col-sm-9 mt-sm-3">
                  <input type="text" class="form-control" id="f_holder" maxlength="50" v-model="content.holder">
                </div>

                <!---->
                <!---->
                <!---->
                <!--                <div class="alert-success">{{ content.validation }}</div>-->
                <!---->
                <!---->
                <!---->

                <label v-if="[1, 2, 3, 6, 7, 9].includes(content.type * 1)" class="col-sm-3 col-form-label-sm mt-3"
                       for="f_validate">
                  <span>유효성 검사</span>
                </label>
                <div v-if="[1, 2, 3, 6, 7, 9].includes(content.type * 1)" class="col-sm-9 mt-sm-3 pt-2" id="f_validate">
                  <label :for="'f_validate_1' + content.sign" class="validate_label">
                    <input type="checkbox" :id="'f_validate_1' + content.sign" v-model="content.validation.required">
                    필수
                  </label>
                  <label v-if="[1].includes(content.type * 1)" :for="'f_validate_2' + content.sign"
                         class="validate_label">
                    <input type="checkbox" :id="'f_validate_2' + content.sign" v-model="content.validation.korean_only">
                    한글만
                  </label>
                  <label v-if="[1].includes(content.type * 1)" :for="'f_validate_3' + content.sign"
                         class="validate_label">
                    <input type="checkbox" :id="'f_validate_3' + content.sign"
                           v-model="content.validation.english_only">
                    영어만
                  </label>
                  <label v-if="[1, 2].includes(content.type * 1)" :for="'f_validate_4' + content.sign"
                         class="validate_label">
                    <input type="checkbox" :id="'f_validate_4' + content.sign" v-model="content.validation.number_only">
                    숫자만
                  </label>
                  <label v-if="[3].includes(content.type * 1)" :for="'f_validate_5' + content.sign"
                         class="validate_label">
                    <input type="checkbox" :id="'f_validate_5' + content.sign" v-model="content.validation.phone_only">
                    전화번호만
                  </label>
                  <label v-if="[1].includes(content.type * 1)" :for="'f_validate_6' + content.sign"
                         class="validate_label">
                    <input type="checkbox" :id="'f_validate_6' + content.sign" v-model="content.validation.email">
                    이메일
                  </label>
                  <label v-if="[7].includes(content.type * 1)" :for="'f_validate_7' + content.sign"
                         class="validate_label">
                    <input type="checkbox" :id="'f_validate_7' + content.sign" v-model="content.validation.age_limit">
                    나이제한
                  </label>
                </div>

                <div v-if="[7].includes(content.type * 1)" class="w-100">
                  <label v-if="content.validation.age_limit" class="col-sm-3 col-form-label-sm mt-3 float-left"
                         for="limit_option">
                    <span>나이제한 옵션</span>
                  </label>

                  <div v-if="content.validation.age_limit" class="col-sm-9 mt-sm-3 float-left" id="limit_option">
                    <input type="number" class="form-control"
                           v-model.number="content.validation.value_min.value">
                    <div class="mt-2">
                      <label :for="'limit_option_min_gt' + content.sign" class="validate_label">
                        <input type="radio" :id="'limit_option_min_gt' + content.sign" value="gt"
                               v-model="content.validation.value_min.option">
                        <span>초과</span>
                      </label>
                      <label :for="'limit_option_min_gte' + content.sign" class="validate_label">
                        <input type="radio" :id="'limit_option_min_gte' + content.sign" value="gte"
                               v-model="content.validation.value_min.option">
                        <span>이상</span>
                      </label>
                    </div>
                  </div>

                  <div v-if="content.validation.age_limit" class="col-sm-3 col-form-label-sm mt-3 float-left"></div>
                  <div v-if="content.validation.age_limit" class="col-sm-9 mt-sm-3 float-left">
                    <input type="number" class="form-control"
                           v-model.number="content.validation.value_max.value">
                    <div class="mt-2">
                      <label :for="'limit_option_min_lt' + content.sign" class="validate_label">
                        <input type="radio" :id="'limit_option_min_lt' + content.sign" value="lt"
                               v-model="content.validation.value_max.option">
                        <span>미만</span>
                      </label>
                      <label :for="'limit_option_min_lte' + content.sign" class="validate_label">
                        <input type="radio" :id="'limit_option_min_lte' + content.sign" value="lte"
                               v-model="content.validation.value_max.option">
                        <span>이하</span>
                      </label>
                    </div>
                  </div>
                </div>

                <label v-if="content.type == 4 || content.type == 5 || content.type == 6"
                       class="col-sm-3 col-form-label-sm mt-3" for="f_list"><span>리스트</span>
                  <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
                        v-tooltip="{
                              content: msg.list,
                              placement: 'right',
                              offset: 5,
                              trigger: 'hover',
                            }">?</span>
                  <span class="question badge btn-secondary p-1 align-middle" v-else
                        v-tooltip="{
                              content: msg.list,
                              placement: 'right',
                              offset: 5,
                              trigger: 'click',
                              }">?</span>
                </label>
                <div v-if="content.type == 4 || content.type == 5 || content.type == 6" class="col-sm-9 mt-sm-3">
                  <button type="button" @click.prevent="field_list_add(content.sign)"
                          class="btn btn-primary pl-3 pr-3 pt-1 pb-1">추가
                  </button>
                  <div v-for="(item, index) in content.list" class="row pl-3 pr-3 pt-2 pb-2">
                    <input type="text" class="form-control col-10" v-model="content.list[index]" id="f_list">
                    <button type="button" @click.prevent="field_list_delete(content.sign, index)"
                            class="btn btn-danger col-2 p-0">삭제
                    </button>
                  </div>
                </div>

                <!-- Scroll -->
                <label v-if="[4].includes(content.type * 1)" class="col-sm-3 col-form-label-sm mt-3">
                  <span>리스트 기본값</span>
                </label>
                <div v-if="[4].includes(content.type * 1)" class="col-sm-9 mt-sm-3">
                  <select class="form-control" v-model="content.default">
                    <option value="">기본값 없음</option>
                    <option v-for="item in content.list" :value="item">{{ item }}</option>
                  </select>
                </div>

                <!-- Radio -->
                <label v-if="[5].includes(content.type * 1)" class="col-sm-3 col-form-label-sm mt-3">
                  <span>체크 기본값</span>
                </label>
                <div v-if="[5].includes(content.type * 1)" class="col-sm-9 mt-sm-3">
                  <select class="form-control" v-model="content.default">
                    <option v-for="item in content.list" :value="item">{{ item }}</option>
                  </select>
                </div>

                <label v-if="[9].includes(content.type * 1)" class="col-sm-3 col-form-label-sm mt-3">
                  <span>미리체크 여부</span>
                </label>
                <div v-if="[9].includes(content.type * 1)" class="col-sm-9 mt-sm-3">
                  <label :for="'agree_precheck_true'+content.sign" class="validate_label">
                    <input type="radio" :id="'agree_precheck_true'+content.sign" value='true'
                           v-model="content.default">
                    <span>체크</span>
                  </label>
                  <label :for="'agree_precheck_false'+content.sign" class="validate_label">
                    <input type="radio" :id="'agree_precheck_false'+content.sign" value='false'
                           v-model="content.default">
                    <span>해제</span>
                  </label>
                </div>

                <label class="col-sm-3 col-form-label-sm mt-3"
                       for="f_back">배경색</label>
                <div class="col-sm-9 mt-sm-3">
                  <div class="color_wrap form-control col">
                    <input type="color" v-model="content.back_color" class="color_picker">
                  </div>
                  <input type="text" class="form-control" id="f_back" maxlength="10" v-model="content.back_color">
                </div>

                <label class="col-sm-3 col-form-label-sm mt-3"
                       for="f_color">글씨색</label>
                <div class="col-sm-9 mt-sm-3">
                  <div class="color_wrap form-control col">
                    <input type="color" v-model="content.text_color" class="color_picker">
                  </div>
                  <input type="text" class="form-control" id="f_color" maxlength="10"
                         v-model="content.text_color">
                </div>
                <label v-if="content.type == 8"
                       class="col-sm-3 col-form-label-sm mt-3"
                       for="f_img">이미지</label>
                <div v-if="content.type == 8" class="col-sm-9 mt-sm-3">

                  <input type="file"
                         class="input_one_btn form-control col-md-11 pt-1" id="f_img"
                         placeholder="이미지" :id="'field_file_input_'+content.sign"
                         :ref="'field_file_input_' + content.sign"
                         @change="field_file_add(content.sign, $event.target.files[0])"
                         accept="image/*">

                  <div class="col-12 p-0" id="term_img_preview">
                    <div v-if="content.image_data" class="term_preview_wrap">
                      <img class="term_preview" :src="content.image_data" alt="약관 이미지 미리보기">
                    </div>
                    <div v-else class="form-control">
                      <div>등록된 파일이 없습니다</div>
                    </div>
                  </div>

                  <button type="button" class="btn btn-danger w-100 mt-1" id="f_imgg"
                          @click.prevent="field_file_delete(content.sign, $event.target)">
                    파일삭제
                  </button>

                </div>
              </div>
              <button type="button" class="btn btn-info col-12 m-auto" data-toggle="collapse"
                      v-bind:href="'#collapse_option'+ content.sign" aria-expanded="false">
                닫기
              </button>
            </form>
          </div>
        </li>
        <li v-if="field.length == 0" class="d-inline-flex justify-content-between p-1">
          <div class="col p-2 text-center bg-light">필드 없음</div>
        </li>
      </ul>
    </div>
  </div>

</template>

<script>
  export default {
    name: "section_3_form_detail",
    props: [
      'window_width',
      'page_id',
      'epoch_time',
      'updated_date',
      'form_arrow',
      'field',
      'set_field',
      'push_landing'
    ],
    data: () => ({
      msg: {
        holder: 'Place holder입니다. 텍스트 입력 전 설명 혹은, 약관의 라벨에 기입됩니다.',
        list: '선택 옵션을 선택하고 제공할 수 있습니다.'
      },
      field_obj: [],
      filtered_fields: [],
      field_selected: -1,
      field_temp_name: ''
    }),
    mounted() {
      this.init_component()
      // this.validation_back()
    },
    methods: {
      init_component() {
        // Set component object as parent's object
        this.field_obj = []
        this.field_obj = this.field
      },
      validation_back() {
        let field = this.field_obj
        // console.log(field.length)
        // Preparing validation list
        let vali = [
          'required',
          'korean_only',
          'english_only',
          'number_only',
          'phone_only',
          'email',
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
              console.log(field[i].validation)
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
          // this.dynamo_obj = this.temp_obj
          // console.log('console field ', field[i])
          this.$emit('update:field', this.field_obj)
          this.filter_change()
        }
      },
      filter_change() {
        this.filtered_fields = []
        for (let i = 0; i < this.field_obj.length; i++) {
          if (this.field_obj[i].form_group_id == this.form_arrow) {
            this.filtered_fields.push(this.field_obj[i])
          }
        }
      },
      field_add() {
        this.init_component()

        // get form group sign
        if (this.form_arrow != -1) {
          // get field type and field name
          if (this.field_selected != -1 && this.field_temp_name) {
            // if field object is not empty
            if (this.field_obj.length != 0) {
              let highest = 0
              let flag = true
              for (let i = 0; i < this.field_obj.length; i++) {
                if (this.form_arrow == this.field_obj[i].form_group_id) {
                  if (this.field_temp_name == this.field_obj[i].name) {
                    alert('이미 존재하는 필드 이름입니다.')
                    flag = false
                    return flag
                  }
                }
              }
              if (flag) {
                for (let i = 0; i < this.field_obj.length; i++) {
                  if (this.field_obj[i].sign > highest) {
                    highest = this.field_obj[i].sign
                  }
                }
              }
              this.field_obj.push({
                sign: highest + 1,
                type: this.field_selected * 1,
                label: true,
                name: this.field_temp_name,
                holder: this.field_temp_name,
                form_group_id: this.form_arrow * 1,
                back_color: '#287BFF',
                text_color: '#f0f0f0',
                validation: {
                  required: true,
                  korean_only: false,
                  english_only: false,
                  number_only: false,
                  phone_only: false,
                  email: false,
                  age_limit: false,
                  value_min: {
                    value: 0,
                    option: 'gt'
                  },
                  value_max: {
                    value: 120,
                    option: 'lt'
                  }
                },
                opacity: '10',
                list: [],
                default: '',
                image_data: null
              })
              this.$emit('update:field', this.field_obj)
              this.field_temp_name = ''
              this.filter_change()
              this.set_field('form')
              this.push_landing()
            } else {
              // if field_obj length is 0
              this.field_obj.push({
                sign: 1,
                type: this.field_selected * 1,
                label: true,
                name: this.field_temp_name,
                holder: this.field_temp_name,
                form_group_id: this.form_arrow * 1,
                back_color: '#287BFF',
                text_color: '#fafafa',
                validation: {
                  required: true,
                  korean_only: false,
                  english_only: false,
                  number_only: false,
                  phone_only: false,
                  email: false,
                  age_limit: false,
                  value_min: {
                    value: 0,
                    option: 'gt'
                  },
                  value_max: {
                    value: 120,
                    option: 'lt'
                  }
                },
                opacity: '10',
                list: [],
                default: '',
                image_data: null
              })
              this.$emit('update:field', this.field_obj)
              this.field_temp_name = ''
              this.filter_change()
              this.set_field('form')
              this.push_landing()
            }
          } else {
            alert('필드 타입과 내용을 입력하세요.')
            document.getElementById('db_field').focus()
          }
        } else {
          alert('폼 그룹을 먼저 선택하세요.')
          document.getElementById('form_group_list').focus()
        }
      },
      field_delete(id) {
        this.init_component()
        for (let i = 0; i < this.field_obj.length; i++) {
          if (this.field_obj[i].sign == id) {
            // console.log(this.field_obj.splice(i, 1))
            this.field_obj.splice(i, 1)
            this.$emit('update:field', this.field_obj)
            this.filter_change()
            this.set_field('form')
            this.push_landing()
            break
          }
        }
      },
      field_list_add(id) {
        this.init_component()
        for (let i = 0; i < this.field.length; i++) {
          if (this.field_obj[i].sign == id) {
            this.field_obj[i].list.push("")
            this.$emit('update:field', this.field_obj)
            this.filter_change()
            this.push_landing()
            break
          }
        }
      },
      field_list_delete(id, index) {
        this.init_component()
        for (let i = 0; i < this.field_obj.length; i++) {
          if (this.field_obj[i].sign == id) {
            this.field_obj[i].list.splice(index, 1)
            this.$emit('update:field', this.field_obj)
            this.filter_change()
            this.push_landing()
            break
          }
        }
      },
      field_option_close(that) {
        //
      },
      field_file_add(sign, file) {
        this.init_component()

        let key = require('../../../vue_env')

        AWS.config.update({
          region: key.BucketRegion,
          credentials: new AWS.CognitoIdentityCredentials({
            IdentityPoolId: key.IdentityPoolId
          })
        })

        let s3 = new AWS.S3(
          {
            apiVersion: '2008-10-17',
            params: {
              Bucket: key.AWS_STORAGE_BUCKET_NAME
            }
          }
        )

        for (let i = 0; i < this.field_obj.length; i++) {
          if (this.field_obj[i].sign == sign && this.field_obj[i].image_data) {

            let photokey = this.field_obj[i].image_data.replace('https://assets.infomagazine.xyz', 'assets')
            s3.deleteObject({Key: photokey}, (err, data) => {
              if (err) {
                alert('There was an error deleting your photo: ', err.message)
              } else {
                this.field_obj[i].image_data = null
                this.field_obj[i].image_url = null
              }
            })

          }
        }

        let params = {}

        params = {
          Key: 'assets/images/landing/' + this.page_id + '/field/' + file.name + '_' + Date.now(),
          ContentType: file.type,
          Body: file
        }

        s3.upload(params, (error, data) => {
          if (error) {
            console.log('S3 upload error occurred', error)
          } else {
            for (let i = 0; i < this.field_obj.length; i++) {
              if (this.field_obj[i].sign == sign) {
                this.field_obj[i].image_data = params.Key.replace('assets/', 'https://assets.infomagazine.xyz/')
              }
            }
            this.$emit('update:field', this.field_obj)
            this.push_landing()
          }
        })

      },
      field_file_delete(sign) {
        this.init_component()

        let key = require('../../../vue_env')

        AWS.config.update({
          region: key.BucketRegion,
          credentials: new AWS.CognitoIdentityCredentials({
            IdentityPoolId: key.IdentityPoolId
          })
        })

        let s3 = new AWS.S3(
          {
            apiVersion: '2008-10-17',
            params: {
              Bucket: key.AWS_STORAGE_BUCKET_NAME
            }
          }
        )

        for (let i = 0; i < this.field_obj.length; i++) {
          if (this.field_obj[i].sign == sign) {

            let photoKey = this.field_obj[i].image_data.replace('https://assets.infomagazine.xyz', 'assets')

            s3.deleteObject({Key: photoKey}, (err, data) => {
              if (err) {
                alert('There was an error deleting your photo: ', err.message)
              } else {
                // alert('Successfully deleted photo.', data)

                document.getElementById('field_file_input_' + sign).value = ''
                this.field_obj[i].image_data = null
                this.$emit('update:field', this.field_obj)
                this.push_landing()
              }
            })

          }
        }
      },
      // key_to_url(key) {
      //   if (key != null) {
      //     if (key.indexOf('assets') > -1) {
      //       let divided = key.split('/')
      //       let url = 'https://'
      //
      //       if (this.updated_date == '') {
      //         url += 'infomagazine.s3.ap-northeast-2.amazonaws.com/' + key
      //       } else {
      //         for (let i = 0; i < divided.length; i++) {
      //           if (i == 0) {
      //             url += (divided[i] + '.infomagazine.xyz')
      //             // url += ('assets' + '.infomagazine.xyz')
      //           } else {
      //             url += ('/' + divided[i])
      //           }
      //         }
      //       }
      //       return url
      //     } else {
      //       let divided = key.split('/')
      //       let url = 'https://'
      //
      //       if (this.updated_date == '') {
      //         url += 'infomagazine.s3.ap-northeast-2.amazonaws.com/assets' + key
      //       } else {
      //         for (let i = 0; i < divided.length; i++) {
      //           if (i == 0) {
      //             // url += (divided[i] + '.infomagazine.xyz')
      //             url += ('assets' + '.infomagazine.xyz')
      //           } else {
      //             url += ('/' + divided[i])
      //           }
      //         }
      //       }
      //       return url
      //     }
      //   } else {
      //     return ''
      //   }
      //
      // }
    },
    computed: {
      arrow() {
        let arrow = this.form_arrow
        this.init_component()
        return arrow
      }
    }
  }
</script>

<style lang="scss" scoped>
  .term_preview_wrap {
    display: block;
    width: 100%;
    padding: .375rem .75rem;
    font-size: 1rem;
    line-height: 1.5;
    color: #495057;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #ced4da;
    border-radius: .25rem;
    transition: border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    text-align: center;
  }

  .term_preview {
    position: relative;
    max-width: 100%;
  }

  .validate_label {
    padding: 0 10px;

    input {
      margin: 0 4px;
    }
  }
</style>

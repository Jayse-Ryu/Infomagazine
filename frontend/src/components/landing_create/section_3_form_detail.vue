<template>

  <div class="form-group row mb-0" v-if="form_arrow != -1">
    <label class="col-sm-3 col-form-label-sm mt-3" for="db_field">DB 필드</label>
    <form class="col-sm-9 mt-sm-3 row ml-0" v-on:submit.prevent="field_add">
      <select class="form-control col-sm-5 col-md-5" name="company" id="db_field" v-model="field_selected">
        <option value="-1">타입을 선택하세요</option>
        <option value="1">텍스트 입력</option>
        <option value="2">번호 입력</option>
        <option value="3">선택 스크롤</option>
        <option value="4">선택 버튼</option>
        <option value="5">체크 박스</option>
        <option value="6">날짜</option>
        <option value="7">링크 버튼</option>
        <option value="8">전화 버튼</option>
        <option value="9">완료 버튼</option>
        <option value="10">약관 동의</option>
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
            v-for="content in field" v-if="content.form_group_id == form_arrow">
          <div class="col-3 p-2 text-center" v-if="content.type == 1">텍스트 입력</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 2">번호 입력</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 3">선택 스크롤</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 4">선택 버튼</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 5">체크 박스</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 6">날짜</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 7">링크 버튼</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 8">전화 버튼</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 9">완료 버튼</div>
          <div class="col-3 p-2 text-center" v-if="content.type == 10">약관 동의</div>
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

                <label class="col-sm-3 col-form-label-sm mt-3" :for="'la_switch'+content.sign">라벨 켜기</label>
                <div class="col-sm-9 mt-sm-3">
                  <label class="switch" :for="'la_switch'+content.sign">
                    <input type="checkbox" :id="'la_switch'+content.sign" v-model="content.label">
                    <span class="slider round"></span>
                  </label>
                </div>

                <label class="col-sm-3 col-form-label-sm mt-3" for="f_type">타입*</label>
                <div class="col-sm-9 mt-sm-3">
                  <select class="form-control" id="f_type" v-model="content.type">
                    <option value="1">텍스트 입력</option>
                    <option value="2">번호 입력</option>
                    <option value="3">선택 스크롤</option>
                    <option value="4">선택 버튼</option>
                    <option value="5">체크 박스</option>
                    <option value="6">날짜</option>
                    <option value="7">링크 버튼</option>
                    <option value="8">전화 버튼</option>
                    <option value="9">완료 버튼</option>
                    <option value="10">약관 동의</option>
                  </select>
                </div>

                <label class="col-sm-3 col-form-label-sm mt-3" for="f_name">필드 이름*</label>
                <div class="col-sm-9 mt-sm-3">
                  <input type="text" class="form-control" id="f_name" maxlength="10" v-model="content.name">
                </div>

                <label v-if="content.type != 4 && content.type != 5 && content.type != 6"
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
                <div v-if="content.type != 4 && content.type != 5 && content.type != 6" class="col-sm-9 mt-sm-3">
                  <input type="text" class="form-control" id="f_holder" maxlength="50" v-model="content.holder">
                </div>

                <label v-if="content.type == 8" class="col-sm-3 col-form-label-sm mt-3" for="f_val">전화번호</label>
                <div v-if="content.type == 8" class="col-sm-9 mt-sm-3">
                  <input type="text" class="form-control" id="f_val" maxlength="12" v-model="content.value">
                </div>

                <label v-if="content.type == 7" class="col-sm-3 col-form-label-sm mt-3" for="f_link">링크</label>
                <div v-if="content.type == 7" class="col-sm-9 mt-sm-3">
                  <input type="text" class="form-control" id="f_link" maxlength="200" v-model="content.url">
                </div>

                <label v-if="content.type == 3 || content.type == 4 || content.type == 5"
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
                <div v-if="content.type == 3 || content.type == 4 || content.type == 5" class="col-sm-9 mt-sm-3">
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

                <label v-if="content.type == 7 || content.type == 8 || content.type == 9"
                       class="col-sm-3 col-form-label-sm mt-3"
                       for="f_back">배경색</label>
                <div v-if="content.type == 7 || content.type == 8 || content.type == 9" class="col-sm-9 mt-sm-3">
                  <div class="color_wrap form-control col">
                    <input type="color" v-model="content.back_color" class="color_picker">
                  </div>
                  <input type="text" class="form-control" id="f_back" maxlength="10" v-model="content.back_color">
                </div>

                <label v-if="content.type == 7 || content.type == 8 || content.type == 9"
                       class="col-sm-3 col-form-label-sm mt-3"
                       for="f_color">글씨색</label>
                <div v-if="content.type == 7 || content.type == 8 || content.type == 9" class="col-sm-9 mt-sm-3">
                  <div class="color_wrap form-control col">
                    <input type="color" v-model="content.text_color" class="color_picker">
                  </div>
                  <input type="text" class="form-control" id="f_color" maxlength="10"
                         v-model="content.text_color">
                </div>
                <label v-if="content.type == 7 || content.type == 8 || content.type == 9"
                       class="col-sm-3 col-form-label-sm mt-3"
                       for="f_img">이미지</label>
                <div v-if="content.type == 7 || content.type == 8 || content.type == 9" class="col-sm-9 mt-sm-3">
                  <input type="file" class="input_one_btn form-control col-md-11 pt-1" id="f_img"
                         placeholder="이미지" :id="'field_file_input'+content.sign"
                         :ref="'field_file_input_' + content.type" @change="field_file_add(content.sign)"
                         :value="content.image"
                         accept="image/*">
                  <button type="button" class="btn btn-danger w-100 mt-1" id="f_imgg"
                          @click.prevent="field_file_delete(content.sign)">
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
        <!--<li v-if="" class="d-inline-flex justify-content-between p-1">
          <div class="col p-2 text-center bg-light">데이터 없음</div>
        </li>-->
      </ul>
    </div>
  </div>

</template>

<script>
  export default {
    name: "section_3_form_detail",
    props: [
      'window_width',
      'form_arrow',
      'field'
    ],
    data: () => ({
      msg: {
        holder: 'Place holder입니다. 텍스트 입력 전 설명이 필요하거나 전화, 링크의 버튼에 표시할 글을 지정합니다.'
      },
      field_obj: [],
      filtered_fields: [],
      field_selected: -1,
      field_temp_name: ''
    }),
    mounted() {
      this.field_obj = this.field
    },
    methods: {
      filter_change() {
        console.log('filter changed method run')
        this.filtered_fields = []
        for (let i = 0; i < this.field_obj.length; i++) {
          if (this.field_obj[i].form_group_id == this.form_arrow) {
            this.filtered_fields.push(this.field_obj[i])
          }
        }
      },
      field_add() {
        this.field_obj = []
        this.field_obj = this.field
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
                form_group_id: this.form_arrow,
                back_color: '#287BFF',
                text_color: '#f0f0f0',
                opacity: 10,
                list: [],
                image_data: null
              })
              this.$emit('update:field', this.field_obj)

              this.field_temp_name = ''
              this.filter_change()
            } else {
              // if field_obj length is 0
              this.field_obj.push({
                sign: 1,
                type: this.field_selected * 1,
                label: true,
                name: this.field_temp_name,
                holder: this.field_temp_name,
                form_group_id: this.form_arrow,
                back_color: '#287BFF',
                text_color: '#fafafa',
                opacity: 10,
                list: [],
                image_data: null
              })
              this.$emit('update:field', this.field_obj)

              this.field_temp_name = ''
              this.filter_change()
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
        this.field_obj = []
        this.field_obj = this.field
        for (let i = 0; i < this.field_obj.length; i++) {
          if (this.field_obj[i].sign == id) {
            // console.log(this.field_obj.splice(i, 1))
            this.field_obj.splice(i, 1)
            this.$emit('update:field', this.field_obj)
            this.filter_change()
            break
          }
        }
      },
      field_list_add(id) {
        this.field_obj = []
        this.field_obj = this.field
        for (let i = 0; i < this.field.length; i++) {
          if (this.field_obj[i].sign == id) {
            this.field_obj[i].list.push("")
            this.$emit('update:field', this.field_obj)
            this.filter_change()
            break
          }
        }
      },
      field_list_delete(id, index) {
        this.field_obj = []
        this.field_obj = this.field
        for (let i = 0; i < this.field_obj.length; i++) {
          if (this.field_obj[i].sign == id) {
            this.field_obj[i].list.splice(index, 1)
            this.$emit('update:field', this.field_obj)
            this.filter_change()
            break
          }
        }
      },
      field_option_close(that) {
        //
      }
    }
  }
</script>

<style scoped>

</style>

<template>

  <div class="form-group row mb-0">

    <!--<div class="alert-info w-100">{{ form }}</div>
    <div class="alert-danger w-100 m-1" v-for="item in field">{{ item }}</div>-->

    <label class="col-sm-3 col-form-label-sm mt-3" for="form_group">DB 폼 그룹</label>
    <form class="col-sm-9 mt-sm-3 row ml-0" v-on:submit.prevent="form_group_add">
      <input type="text" class="input_one_btn form-control col-md-11" id="form_group" name="form_group"
             placeholder="폼 그룹 이름" maxlength="50" v-model="form_temp">
      <button type="submit" class="btn btn-primary col-md-1 p-0" name="form_group">추가</button>
    </form>

    <label class="col-sm-3 col-form-label-sm mt-3" for="form_group_list"></label>
    <div class="col-sm-9 mt-sm-3 row ml-0">
      <select class="input_one_btn form-control col-md-11" name="form_group_list" id="form_group_list"
              :value="form_arrow" @change="form_changed($event.target.value)">
        <option value="-1">그룹을 선택하세요</option>
        <option v-for="item in form" :value="item.sign">{{ item.name }}</option>
      </select>
      <button type="button" class="btn btn-danger col-md-1 p-0"
              @click.prevent="form_group_delete(form_selected.sign)">
        삭제
      </button>
    </div>

    <label v-if="form_selected.sign != -1" class="col-sm-3 col-form-label-sm mt-3" for="form_group_bg">
      폼 배경색
    </label>
    <div v-if="form_selected.sign != -1" class="col-sm-9 mt-sm-3 row ml-0">
      <div class="color_wrap form-control col-sm-2" id="form_group_bg">
        <input type="color" v-model="form_selected.bg_color" class="color_picker">
      </div>
      <div class="margin_div"></div>
      <input type="text" v-model="form_selected.bg_color" class="form-control col-sm-5" maxlength="10">
    </div>

    <label v-if="form_selected.sign != -1" class="col-sm-3 col-form-label-sm mt-3" for="opacity_slider">
      배경 불투명도
    </label>
    <div v-if="form_selected.sign != -1" class="col-sm-9 mt-sm-3 row ml-0">
      <div class="form-control col-sm-2">{{ form_selected.opacity * 10 }}%</div>
      <div class="margin_div"></div>
      <div class="slide_container col-sm-5 form-control border-0 p-0">
        <input class="opacity_slider w-100 h-100" id="opacity_slider" type="range" min="0" max="10" value="10"
               v-model="form_selected.opacity">
      </div>
    </div>

    <label v-if="form_selected.sign != -1" class="col-sm-3 col-form-label-sm mt-3" for="form_group_col">
      폼 폰트색
    </label>
    <div v-if="form_selected.sign != -1" class="col-sm-9 mt-sm-3 row ml-0">
      <div class="color_wrap form-control col-sm-2" id="form_group_col">
        <input type="color" v-model="form_selected.tx_color" class="color_picker">
      </div>
      <div class="margin_div"></div>
      <input type="text" v-model="form_selected.tx_color" class="form-control col-sm-5" maxlength="10">
    </div>
  </div>

</template>

<script>
  export default {
    name: "section_2_form_control",
    props: [
      'form',
      'form_arrow',
      'field',
      'set_field',
      'push_landing'
      // 'form_selected'
    ],
    data: () => ({
      form_obj: [],
      form_temp: '',
      form_selected: {sign: -1, tx_color: '#313131', bg_color: '#fafafa', opacity: '10'},
      temp_field: []
    }),
    mounted() {
      this.form_init()
    },
    methods: {
      form_init() {
        this.form_obj = []
        this.form_obj = this.form
      },
      form_changed(id) {
        this.form_init()
        this.$emit('update:form_arrow', id)
        if (id == -1) {
          this.form_selected = {sign: -1, tx_color: '#313131', bg_color: '#fafafa', opacity: '10'}
        } else {
          for (let i = 0; i < this.form_obj.length; i++) {
            if (this.form_obj[i].sign == id) {
              this.form_selected = this.form_obj[i]
            }
          }
        }
      },
      form_group_add() {
        this.form_init()
        if (this.form_temp) {
          let len = this.form_obj.length
          let flag = true
          if (len) {
            for (let i = 0; i < len; i++) {
              if (this.form_obj[i].name === this.form_temp) {
                alert('폼 그룹 이름이 이미 존재합니다.')
                flag = false
                return flag
              }
            }
            if (flag) {
              let highest = 0
              for (let i = 0; i < len; i++) {
                if (this.form_obj[i].sign > highest) {
                  highest = this.form_obj[i].sign
                }
              }
              this.form_obj.push({
                sign: highest + 1,
                name: this.form_temp,
                bg_color: '#fafafa',
                tx_color: '#313131',
                opacity: '10'
              })
              this.form_temp = ''
              this.$emit('update:form', this.form_obj)
              alert('폼 그룹이 생성되었습니다.')
              this.push_landing()
            }
          } else {
            this.form_obj.push({
              sign: 1,
              name: this.form_temp,
              bg_color: '#fafafa',
              tx_color: '#313131',
              opacity: '10'
            })
            this.form_temp = ''
            this.$emit('update:form', this.form_obj)
            alert('폼 그룹이 생성되었습니다.')
            this.push_landing()
          }
        } else {
          alert('폼 그룹 이름을 입력하세요!')
        }
      },
      form_group_delete(id) {
        this.form_init()
        if (id !== -1) {
          if (confirm('이 폼그룹을 삭제하시겠습니까?')) {
            this.form_init()
            this.form_obj = this.form_obj.filter(el => el.sign != id)
            // this.form_arrow = -1
            this.$emit('update:form_arrow', -1)
            this.$emit('update:form', this.form_obj)
            this.form_selected = {sign: -1, tx_color: '#313131', bg_color: '#fafafa', opacity: '10'}
            // Field objs delete also
            this.field_work(id)
            // this.push_landing()
          }
        } else {
          alert('그룹을 먼저 선택하세요.')
        }
      },
      field_work(id) {
        this.form_init()
        this.temp_field = []
        this.temp_field = this.field
        this.temp_field = this.temp_field.filter(el => el.form_group_id != id)
        this.$emit('update:field', this.temp_field)
        this.set_field('form')
        this.push_landing()
      }
    }
  }
</script>

<style scoped>

</style>
